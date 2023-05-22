package Usecases

import "serenityapi/Domain"

type Mock_UserByNameLoader struct{}

func (l *Mock_UserByNameLoader) Load(name string) *Domain.User {
	if name == "dexter" {
		return &Domain.User{Name: "dexter", Password: "killer"}
	}
	return nil
}
