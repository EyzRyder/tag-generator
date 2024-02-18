package main

import (
	"fmt"
	"log"
	"net/http"
    "encoding/json"
)

func main(){
    fmt.Println("Http server running")

    basePath := func (w http.ResponseWriter, r *http.Request){
        fmt.Print("HelloWorld")
    }
    helloPath := func (w http.ResponseWriter, r *http.Request){
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode("HelloWorld")
    }

    http.HandleFunc("/",basePath)
    http.HandleFunc("/hello",helloPath)

    fmt.Println("http://localhost:3333")
    log.Fatal(http.ListenAndServe(":3333",nil))
}
