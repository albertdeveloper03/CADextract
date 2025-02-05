# ui

Requirements: 
* python, version: 3.7, https://www.python.org/downloads/ 
* pip3 install redis flask PyPDF2 bs4 
* start redis service 
 
Requirements in more detail: 
* redis, version 5.0.9 (downloaded via pip3)
* flask, version: 1.1.1 (downloaded via pip3) 
* PyPDF2, version: 1.26.0 (downloaded via pip3)
* beautifulsoup4 (bs4), version: 4.8.0 (downloaded via pip3) 
 
 
Adapting the paths in views.py: 
* path = path to project directory 
* db_params = redis configuration (e.g. localhost) 
* path_extraction = path to extraction tool directory  
* path_image = directory where uploaded images are stored 
 
 
Adapting the paths and setting the parameters 
For the web application, four paths have to be set.  
The first path is called ”path” and refers to the project directory. The other one is 
called ”path extraction” and refers to the directory of the extraction tool, as this tool is 
called by the web application. The path where the image, which is used for vizualisation 
in the browser, is set in the variable ”path image”. Lastly, the configuration for ”redis” 
has to be set in ”db params”.  
 
 
Additionally, the regulatory documents that can be provided have to be put into the folder ”app/static/isos”. 
Otherwise, no additional information can be provided, as regulatory documents are 
copyright protected and can not be put publicly on the repository.  
 
No input parameters for the application itself are needed, as the user will input the PDF file using the browser. 
 
If all these requirements are met, the web application can be run by entering ”python -m flask run” 
at the command line while being in the project directory. 
