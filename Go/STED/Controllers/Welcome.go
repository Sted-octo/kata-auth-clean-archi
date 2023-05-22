package Controllers

import (
	"fmt"
	"net/http"

	"github.com/julienschmidt/httprouter"
)

func Welcome(w http.ResponseWriter, r *http.Request, ps httprouter.Params) {
	fmt.Fprintf(w, "SenerityApi, Welcome !")
}
