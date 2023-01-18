# Usage
https://i.imgur.com/t3MX46M.png

# Console
https://i.imgur.com/t8koC6S.png

# Delivered contents

``` json
    {
      "Type" : "Notification",
      "MessageId" : "2023301a-1a24-528f-aae4-6c5b3e4ebe63",
      "TopicArn" : "arn:aws:sns:us-west-2:024726604032:AshtonTest",
      "Message" : "{\"foo\": \"bar\"}",
      "Timestamp" : "2023-01-17T22:33:14.087Z",
      "SignatureVersion" : "1",
      "Signature" : "lkgFqfZqfGR2YDoxvhoFTZ26Hm3FFwYOtIRPviEi53KJd3D0kSJMo8yITx0xc2KW4byPM3+9uL4mS5udTB6PqcnXpYMe6pm10de8sYucGFSHCWpfj6Rq0dIergHFoL2a03f8jRpSL1wcJfutkP0+Tvtsw4lqOtjjqCv0DcV8k9thLWrCSABMIBW52Xi+c6gSk4mseilud63FG/bqYCzSrDC3s8wHehrRD49qf5WS5Fa/I8nWAgz0yCOT/obdtucHRWkkB0OzMHICVyJFtBdPrxgNYDEJnEfBiXHOSfI48b7fCSzNL0WKCz8lTzyaE0MuHDLc7hWX2tEWnSKyt8jmxw==",
      "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
      "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:024726604032:AshtonTest:f1abc4f3-7665-4968-b39c-8a4c6f082d9b",
      "MessageAttributes" : {
        "SDLCEnv" : {"Type":"String","Value":"PROD"},
        "CirrusVersion" : {"Type":"String","Value":"v1.1.0"}
      }
    }
```

``` json
    {
      "Type" : "Notification",
      "MessageId" : "78dfd581-54c7-56dc-9903-89c070ad0a30",
      "TopicArn" : "arn:aws:sns:us-west-2:024726604032:AshtonTest",
      "Message" : "{\"foo\": \"bar\"}",
      "Timestamp" : "2023-01-17T22:33:14.134Z",
      "SignatureVersion" : "1",
      "Signature" : "2v+nzp6rJR0xOoG+29YH/cBrPx7Mg+nKpljyhaH0esJKBxwaaJJSTBg6t4AG7zHaG7pvbp0BAOJ7jaBR0a+yywJJ5YUNAEHSDGcPGeM9zxpJoy3vyjM8bfZs1vozhwrEoY0HVtstm07n4Xsv+aiApY5sn1EI8l10Vua8eCB/w7tAs+0Q9wmj2EvYwSA8QsIQQR0he2m4o2boXRO15mL576qNup63SagX60f9zQRYxL7PJhXiBjY5yy8w1OUWK358W56fwnWDUXCJt7/MWINRKQatWuHs++x7yCK+jElahQNOA47vh/XQKHC1UjZEUL8rAxO7Gw3BOEfJyHnp1s+ZOw==",
      "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
      "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:024726604032:AshtonTest:f1abc4f3-7665-4968-b39c-8a4c6f082d9b",
      "MessageAttributes" : {
        "SDLCEnv" : {"Type":"String","Value":"DEV"},
        "CirrusVersion" : {"Type":"String","Value":"v2.1.0"}
      }
    }
```

# Delivered contents, compressed

``` json
{
  "Type" : "Notification",
  "MessageId" : "51d30d25-3e6b-581d-b983-516719bd5810",
  "TopicArn" : "arn:aws:sns:us-west-2:024726604032:AshtonTest",
  "Message" : "KLUv/SAOcQAAeyJmb28iOiAiYmFyIn0=",
  "Timestamp" : "2023-01-18T17:00:06.376Z",
  "SignatureVersion" : "1",
  "Signature" : "i1j9dsF3sStXPISS0/aNm40d9uUH/v7M1kDaFVltdIpZlkfSZNjP9+2J8gvxzRTHQrySS7Syo1LK93/fkicLHLRsQcl3FjzOqaidvzqMOZ7Q7HrZ7mcPiTkDLC13VWOKOm+p8YDxo+1SR54aCXMy7EtwwORUkakwsqdmpjRjNefrMJMHgZwTuzm/aFlBO1hIb69e1TrzEDRW1Zgx5WyyMReWyo/fIG5AMreGU2qsUdfTOD5rz9r1iT0vYLLz7FIW+8GWxA8WhLEu8Fp42r5mYPUgmYvOyMWQOMwuA+mM5rpaqSjdh3AQ1NhGFu2ZBm97FfdyXoCf7F4B0nSor2NUiQ==",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
  "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:024726604032:AshtonTest:f1abc4f3-7665-4968-b39c-8a4c6f082d9b",
  "MessageAttributes" : {
    "SDLCEnv" : {"Type":"String","Value":"DEV"},
    "CirrusVersion" : {"Type":"String","Value":"v2.1.0"}
  }
}
```

``` json
{
  "Type" : "Notification",
  "MessageId" : "5623b23e-dcfc-5444-a6c5-ee7cfb2a3449",
  "TopicArn" : "arn:aws:sns:us-west-2:024726604032:AshtonTest",
  "Message" : "{\"foo\": \"bar\"}",
  "Timestamp" : "2023-01-18T17:00:06.324Z",
  "SignatureVersion" : "1",
  "Signature" : "zr9Za7P29Vwd4AnllQ64qn6Z6yHvCLPAv+4iWd1er6LD2J+9Qm7tG2KzkueWlkRrrFxJIbl+S3imYoZw0FQl396Lml5tFhsuXjAqNpOEWR7Y2yZaVB4veym/NWtikli8dHL8/cGBXnZ/4LG5s5Hq9iHca2XXThb/cMr0Vnl5GrtTytWiXE6W6f7HLSxc5pK0oYrpf76goXGaynOKBaw8Z8ekg12byTXtaNQpYUImbKkI6MsHdEITvS1SiA4AK5Radan5gDNOWWqqvYuQO8R5MX+fNha/Y0ryjCFo95t65o4guULqTpOCZB5c3kpyJOeiOx3Qx9erMpSxFcZf1gcPRA==",
  "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-56e67fcb41f6fec09b0196692625d385.pem",
  "UnsubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-west-2:024726604032:AshtonTest:f1abc4f3-7665-4968-b39c-8a4c6f082d9b",
  "MessageAttributes" : {
    "SDLCEnv" : {"Type":"String","Value":"PROD"},
    "CirrusVersion" : {"Type":"String","Value":"v1.1.0"}
  }
}
```
