
reg delete "HKCU\Environment" /v FLASK_ENV /f

reg delete "HKCU\Environment" /v FLASK_APP /f


REG delete "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /F /V FOO

