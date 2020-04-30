
### Automatic importer  
- As a user `I want` to import videos and photos from a removable storage `so that I` can automatically organise my projects  
    - Acceptance criteria: 
        - The removable storage has to be found automatically

- As a user `I want` to register a project name `so that I` can easily find them later   
    - Acceptance criteria:
        - The name of the project should be given as an argument

- As a user `I want` to have my files organised by date and file-type `so that I` can easily find them later   
    - Acceptance criteria:
        - The media files should be imported into a folder with the following path structure `{root}/{year}/{projectName}` with subfolders `Video/` and `Photo/`
    
- As a user `I want` to be able to use the program with one simple terminal command `so that I` use the program more intuitively.
    - Acceptance criteria:
        - The terminal command should be structured in the following structure `{import}"{space}"{projectName}`

- As a user `I want` to be able to specify multiple sd-cards `so that I` don't have to change the code every time I want to import from a new volume.
    - Acceptance criteria:
        - Every different sd card name should be specified within the code.
        - The program shouldn't look for files on my SSD's, but only on my sd cards

- As a user `I want` to be able to automatically transcode screen-recordings `so that I` don't have to use the gui of handbrake to transcode.    
    - Acceptance criteria:   
        - The program should be controllable via one simple terminal command.
        - The transcoded files should be delivered in an export folder.
        - The autoimporter should check the export folder for importing the new screen footage.
        - The original screen-recording files should be backed-up on a specified volume
        
