package main

import (
	"database/sql"
	"fmt"
	_ "github.com/mattn/go-sqlite3"
)

type data_sql struct{
	server string
	data string
}

func initialize(db *sql.DB) {
	_, err := db.Exec("CREATE TABLE data_table (id int auto_increment, server text null, data text null)")
	if err != nil {
		fmt.Println("Create error")
	}
	result, err := db.Exec("INSERT INTO data_table (server, data) VALUES ('Localh0st', '{\"Temporary\" : \"Json value\"}')")
	if err != nil {
		panic(err)
	}
	fmt.Println("result: ", result)
}

func main() {
	db, err := sql.Open("sqlite3", "info.db")
	if err != nil {
		panic(err)
	}
	defer db.Close()
	initialize(db)
	rows, err := db.Query("SELECT server, data FROM data_table")
	if err != nil {
		fmt.Println("error selecting: ", err)
	}
	defer rows.Close()
	data := []data_sql{}
	for rows.Next() {
		data_entry := data_sql{}
		err := rows.Scan(&data_entry.server, &data_entry.data)
		if err != nil {
			fmt.Println("Error scaning from select row: ", err)
			continue
		}
		data = append(data, data_entry)
	}
	fmt.Println("SELECTED: ")
	for _, d := range data {
		fmt.Println(d.server, d.data)
	}


}

