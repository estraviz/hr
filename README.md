# Building a Command Line Tool with Python

## Description

Create a tool to export a system's user information into formats that can be used by other departments. The command will be able to export user names, IDs, home directories, and shells as either JSON or CSV. This command will not include information about system users. By default, the command will display the information as JSON to Stdout, but the `--format` flag will allow a person to specify `csv` as an alternative export type. Additionally, a file can be specified by using the `--path` flag. Here are the various ways that the tool can be used:

```
 $ hr --format=csv --path=path/to/users.csv
 $ hr --path=path/to/users.json
 $ hr
 [
   {
      "name": "cloud_user",
      "id": 1002,
      "home": "/home/cloud_user",
      "shell": "/bin/bash"
   },
   {
      "name": "kevin",
      "id": 1003,
      "home": "/home/kevin",
      "shell": "/bin/zsh"
   },
]
$ hr --format=csv
name,id,home,shell
cloud_user,1002,/home/cloud_user,/bin/bash
kevin,1003,/home/kevin,/bin/zsh
```
