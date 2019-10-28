#!/bin/bash

set -x

curl -X GET  'http://127.0.0.1:5000/genes?name=brc&species=homo_sapiens'
wait

curl -X GET  'http://127.0.0.1:5000/genes?name=brc2&species=homo_sapiens'
wait

curl -X GET  'http://127.0.0.1:5000/genes?name=BRC'
wait

curl -X GET  'http://127.0.0.1:5000/genes?name=br'
wait

curl -X POST  'http://127.0.0.1:5000/genes?name=brc2'
wait

curl -X PUT  'http://127.0.0.1:5000/genes?name=brc2'
wait

curl -X PATCH  'http://127.0.0.1:5000/genes?name=brc2'
