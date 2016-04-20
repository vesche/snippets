# poopdb
This is a small, odd little database created for personal use. It isn't finished, currently contains major security flaws, and definitley should not be used for anything serious. Poopdb is a hybrid database/file system. Databases are folders, data within databases are stored in files like `foo.data`. All data is stored in a very simple `key:value` format on seperate lines. Everything lives within `/opt/poopdb`. You can use the database via the cli (poopctl) or api (poopapi).  

## get going
`git clone https://github.com/vesche/poopdb`  
`cd poopdb`  
`sudo chmod +x install.sh`  
`sudo ./install.sh`  
`sudo /opt/poopdb/./poopctl`  

## cli commands
`show dbs` - show databases  
`use foo` - select a database, creates if doesn't exist  
`show datas` - shows data files in selected database  
`add foo.data` - create a new data file  
`del foo.data` - remove a data file  
`read foo.data` - show contents of a data file  
`clear` - clear screen  
`help` - display help text  
`quit` - exit cli  

## api
Primitive driver for working with poopdb.  
```
import poopapi  
poopapi.insert('db', 'foo.data', k, v)
```

## todo
- use parser library in cli  
- daemon  
- linux security checks  
