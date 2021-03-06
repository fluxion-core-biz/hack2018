# Basic diagram

Basic diagrams.

## Requirement

[Pegmatite Chrome Plugin]:https://chrome.google.com/webstore/detail/pegmatite/jegkfbnfbfnohncpcfcimepibmhlkldo
[Pegmatite Chrome Plugin]

## Guide

[PlantUML Guide]:http://plantuml.com/ja/guide
[PlantUML Guide]

## Basic Sequence

```uml:sequence

@startuml
skinparam handwritten true
skinparam backgroundColor #EEEBDC

!define send(a,b,c) a->b : c

autonumber

actor User as user
participant "Client\n(Android)" as client
participant "Job" as job
participant "REST-Server\n(flask)" as rest
participant "Azure-OCR" as azure

user ->> client: Perform prescription capturing
client -> client: Taking a prescription (jpg)
client ->> rest: Req: POST with Image (Base64)

create job
rest -> job: create job location
job -> job: state in progress

rest -->> client: Res: POST location = job
rest -> rest: Decode image (Base64 -> jpg)
rest ->> azure: Req: OCR with Image (jpg)

opt monitor
client ->> job: Req: GET (poling)
job -->> client: Res: GET state = in progress
... : ...
end opt

azure -->> rest: Res: OCR result with JSON

rest -> rest: Morphological analysis by MeCab
note right
形態素解析処理
end note

rest -> rest: Grouping extraction elements (JSON)
note right
List (薬剤名, 飲み方, 日数, 薬剤写真URL)
end note

rest ->> job: Update result with JSON
job -> job: state of completion

client ->> job: Req: GET (poling)
job -->> client: Res: GET state = completed result = JSON

client -> client: Register in the calendar

client ->> job: Req: DEL
job -->> client: Res: DEL

destroy job


@enduml
```
