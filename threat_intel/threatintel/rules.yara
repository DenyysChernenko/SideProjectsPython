rule Trojan_Generic
{
    meta:
        author = "alex"
        description = "Detects generic trojan"

    strings:
        $a = "badstring"
        $b = "evilpattern"

    condition:
        any of them
}

rule Suspicious_Script
{
    strings:
        $script = "Invoke-Expression"
        $cmd = "cmd.exe /c"

    condition:
        all of them
}
