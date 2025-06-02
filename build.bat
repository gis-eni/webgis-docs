@echo on
cd .\de\datalinq
call .\make.bat html
robocopy /MIR .\build\html .\..\..\app\de\datalinq

@echo on
cd .\..\webgis
call .\make.bat html
robocopy /MIR .\build\html .\..\..\app\de\webgis

@echo on
cd ".\..\webgis-cloud"
call .\make.bat html
robocopy /MIR .\build\html .\..\..\app\cloud

@echo on
cd .\..\webgis-dev
call .\make.bat html
robocopy /MIR .\build\html .\..\..\app\dev

@echo on
cd .\..\webgis-manual
call .\make.bat html
robocopy /MIR .\build\html .\..\..\app\manual

