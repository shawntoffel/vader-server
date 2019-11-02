# vader-server

http.server for [VADER](https://github.com/cjhutto/vaderSentiment) sentiment analysis. 

Accepts POST requests on the base url and replies with the valence dict return value from the polarity_scores method.
```
{
    "text": "http servers are great!"
}
```

Example:

```
curl -X POST -H "Content-Type: application/json" -d '{"text":"http servers are great!"}' http://localhost:8080

{"neg": 0.0, "neu": 0.406, "pos": 0.594, "compound": 0.6588}
```
