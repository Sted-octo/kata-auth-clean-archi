package Infra

import (
	"net/http"
	"serenityapi/Controllers"
	"serenityapi/DataProviders"
	"serenityapi/Usecases"

	"github.com/julienschmidt/httprouter"
)

func AuthenticationControllerInjector(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	var loader Usecases.IUserByNameLoader = new(DataProviders.UserByNameLoader)
	Controllers.Authentication(w, r, ps, loader)
}
