package DataProviders

import "serenityapi/Domain"

type UserByNameLoader struct{}

func (l *UserByNameLoader) Load(name string) *Domain.User {
	if name == "dexter" {
		return &Domain.User{Name: "dexter", Password: "killer"}
	}
	return nil
}
