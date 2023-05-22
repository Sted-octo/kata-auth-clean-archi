package Controllers

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
	"serenityapi/Presenters"
	"serenityapi/Usecases"

	"github.com/julienschmidt/httprouter"
)

func Authentication(w http.ResponseWriter, r *http.Request, ps httprouter.Params, loader Usecases.IUserByNameLoader) {
	dec := json.NewDecoder(r.Body)
	var user UserDto
	for {

		if err := dec.Decode(&user); err == io.EOF {
			break
		} else if err != nil {
			log.Fatal(err)
		}
	}

	token, err := Usecases.UserAccessChecker(user.User, loader)
	if err != nil {
		http.Error(w, "Access denied", http.StatusUnauthorized)
		return
	}

	json.NewEncoder(w).Encode(Presenters.JwtToken{Token: token})
}
