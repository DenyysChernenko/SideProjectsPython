rule trojan_generic
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

rule suspicious_script
{
    strings:
        $script = "Invoke-Expression"
        $cmd = "cmd.exe /c"

    condition:
        all of them
}
