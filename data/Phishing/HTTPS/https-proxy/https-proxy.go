// Copyright (c) 2017 Ernest Micklei
//
// MIT License
//
// Permission is hereby granted, free of charge, to any person obtaining
// a copy of this software and associated documentation files (the
// "Software"), to deal in the Software without restriction, including
// without limitation the rights to use, copy, modify, merge, publish,
// distribute, sublicense, and/or sell copies of the Software, and to
// permit persons to whom the Software is furnished to do so, subject to
// the following conditions:
//
// The above copyright notice and this permission notice shall be
// included in all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
// MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
// NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
// LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
// OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
// WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

package main

import (
	"flag"
	"log"
	"net"
	"net/http"
	"net/http/httputil"
	"net/url"
)

var (
	oFrontAddress   = flag.String("front", ":443", "listening address")
	oBackAddress    = flag.String("back", "localhost:8080", "forwarding to backend address")
	oSSLCertificate = flag.String("cert", "", "(cert.pem) SSL certificate location")
	oSSLKey         = flag.String("key", "", "(key.pem) SSL key location")
	oStripPrefix    = flag.String("stripprefix", "", "path element to strip from the HTTP request")
	oVerbose        = flag.Bool("v", false, "verbose logging")
)

func main() {
	flag.Parse()
	proxy := httputil.NewSingleHostReverseProxy(&url.URL{
		Scheme: "http",
		Host:   *oBackAddress,
	})
	director := proxy.Director
	proxy.Director = func(req *http.Request) {
		director(req)
		req.Host = req.URL.Host
	}
	handler := xforwarder(proxy)
	if len(*oStripPrefix) > 0 {
		log.Println("install prefix handler", *oStripPrefix)
		handler = http.StripPrefix(*oStripPrefix, handler)
	}
	log.Println("listening on", *oFrontAddress)
	if len(*oSSLCertificate) > 0 {
		log.Println("accepting HTTPS traffic")
		log.Fatalln(http.ListenAndServeTLS(*oFrontAddress, *oSSLCertificate, *oSSLKey, handler))
	}
	log.Println("accepting non-TLS HTTP traffic")
	log.Fatalln(http.ListenAndServe(*oFrontAddress, handler))
}

func xforwarder(handler http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if clientIP, _, err := net.SplitHostPort(r.RemoteAddr); err == nil {
			r.Header.Set("X-Forwarded-For", clientIP)
		}
		r.Header.Set("X-Forwarded-Host", r.Host)
		r.Header.Set("X-Forwarded-Proto", "https")
		handler.ServeHTTP(w, r)
		if *oVerbose {
			// simple access log entry
			log.Printf("---- %s %s %v\n", r.Method, r.URL.String(), r.Header)
		}
	})
}
