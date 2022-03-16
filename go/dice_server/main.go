package main

import (
	"encoding/json"
	"math/rand"
	"net/http"
	"strconv"
	"strings"
)

type results struct {
	Count  int   `json:"count"`
	Sides  int   `json:"sides"`
	Values []int `json:"values"`
}

func roll(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)

	v := []int{}

	// data := make(map[string]int)
	a, _ := strconv.Atoi(strings.Split(req.URL.Path, "/")[1])
	b, _ := strconv.Atoi(strings.Split(req.URL.Path, "/")[2])
	for i := 0; i < a; i++ {
		v = append(v, rand.Intn(b))
	}
	data := results{
		Count:  a,
		Sides:  b,
		Values: v,
	}
	json.NewEncoder(w).Encode(data)
}

func main() {
	http.HandleFunc("/", roll)
	http.ListenAndServe(":8090", nil)
}
