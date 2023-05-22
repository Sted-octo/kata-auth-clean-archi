package main

import (
	"log"
	"net/http"
	"serenityapi/Controllers"
	"serenityapi/Infra"

	"github.com/julienschmidt/httprouter"
)

func main() {
	router := httprouter.New()
	router.GET("/", Controllers.Welcome)
	router.POST("/api/auth", Infra.AuthenticationControllerInjector)
	err := http.ListenAndServe(":9090", router)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
