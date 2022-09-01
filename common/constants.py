r"""
 ____  _                           ____  _                                             _
|  _ \(_) __ _ _ __   __ _  ___   |  _ \| | __ _ _   _  __ _ _ __ ___  _   _ _ __   __| |
| | | | |/ _` | '_ \ / _` |/ _ \  | |_) | |/ _` | | | |/ _` | '__/ _ \| | | | '_ \ / _` |
| |_| | | (_| | | | | (_| | (_) | |  __/| | (_| | |_| | (_| | | | (_) | |_| | | | | (_| |
|____// |\__,_|_| |_|\__, |\___/  |_|   |_|\__,_|\__, |\__, |_|  \___/ \__,_|_| |_|\__,_|
    |__/             |___/                       |___/ |___/

    https://github.com/yingzhuo/DjangoPlayground
"""
from django_sugar import web

# JWT签名公钥
_RSA_PUBLIC = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzy9/cj6YTwuc/5aVj7ER
mhmLIRe/g6EUqWyDKyvggIs0oCWQtBUY2MOasmlOnMgmWeKtNT+4l5vcio7lFLN+
6AL5FFS1LnPRk7syfnUjorg8yEegAODkZtjDoVLw0BP47K6TLoGYo+HR9hTTDGSP
MxjnlxA63X5slg3trYT80IOYVVW6sYW3qCbgrXRc5/RQfWh4wC3AL2gj1MEujDCM
HPxJUtAzX5nq5LYHso3fXMYIQJ8G3kFSmJ2TWv5ZYIAzKUqJPiztO4IvGcGTESaz
vgeJgYAV0BL6tZf6cPIBCWafVsZ6OF/oikmvzPYLG/mVvdI+DUhBUcVu5XBYb9CX
EwIDAQAB
-----END PUBLIC KEY-----
"""

# JWT签名私钥
_RSA_PRIVATE = """
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-256-CBC,127218E254D8E2FC17047781D78D59A9

911vesiNkVKt0BjgnMn4u2/syRiqEMh0N6+CWxiyVnJn0JPnVaomuoGKfTwWuUzW
Qysn0nft7oyinZ18Vg/l9A0eSJ0hxpfvclTRB5P1vLWxa58U2wfy5jIlUQKoUlUL
R23dVTb6Fn3n9LZneg9d2azPvH//0zTakDbhjefhwegdCg9bFNqyxzLdf0az4+Ac
+Rx9zpdSl7ERD2Qb7T4at9sGDmn8cdy8AGXtsZNfN/zG9IkCohcpi50/KqycsXXu
g0mpG3ejItf8SAp5xDF8o1lWfwgrh/0SYWZRDwuBkZtLSiCe+GkYrW8Jb2qnPInB
UFNaZKL9k7ZOPRC2AE3L04W6AFJaPBPrMR6R7QVX50Uu4V2Bas6H0tl8DE2z9cDd
gVbk5cTZkERpqKyrHGQNYHR7NWYTlIVKD+vrP/4et/xkFQ8cDtPLPCVzUKF1CDUk
KdMW2zCilnUUy1xhYbs+Wl94bz2Es5vzABVuQ1Av2YM9dBIju+QMQS7mIJg/2Ny6
wC47IJfetQ2L8fE1lc6TT2aRZp21Wfa1BKwWqJOcFSHC32NY8dX8GSAoLUKpkbbT
rLnuYaewti/R7FqZrSAGK+cZhZBEIcGXsxOl84x7pgkL9DE24+RkjNCaBQ3+JwsB
kbMo8f4DMJCUscdkxOuPNppEBPfzRTyjuFi9SIwZAx0NBhaGRtxpNQFR69vfH2ut
az8cXY4DmwNUcBqLXEjysGowReBeqCHgoOQtzwiGJYCgX1R6TWoo6zGHKjbRIUhj
NL2NwRSA8K2btU+aFPubeJ3bWh6CtgddEN4m8eTMoe6By1RxK+XAkY+8GxJdy3oL
oDw2BZPAsK11vkmxXl7AIJjzMnhMy4Jv6DaTQoTv0GPU2ujcb9MrjQwEQCC/c/ia
RAP2U+7UrFFWwTuDbTWDhA4qi+sPU9ERc0geShBpTz6uyaJ4a++aU3drHCGWXJIw
pafRvAUlGnVp3N+ineqqdK5yBzcPeqOpP/fHx40/Chawn14pK85qttPhoOVKGBB0
H5JMW8ffayFxmx6NawfnufBDDlPb2TrLGrd8gjljoYY0Cvtg7NhEFtGbeWb2tB73
nhPlreFzeG2xyXUieyLZtcp0QykJkVWURqMZJ7wEZluYDsn+dAyHgfee2kG+aZhH
U/z/JJlzFsot+MdfqXrHewnUcgzN64KL2FHo7Xrgd6ul+NLYcYIapTMrUugnJzc/
aDOXQz+BJIE4S88BLMbwruTJXpKPRgd+JRB4EVNX9KrQlWn+tKMhpSDv+xyTKoGb
2krZCrY38/jjodrWtWE/dV3OLk4dv1e1kLxX/jiQN7LChl0hUTGHv9SApsVkjvgp
0SZR9aRB1LknzdtK+HgOeGaf1e7Tu2WhFTtaBG7ZjbSoa2OgwQ/1zhpm9J4q373c
lkUK5912AVcXWPScGj4NKEigvIn5I5oOMyVNTWqybYCRqtM0ZW3fbKfmOSySFXuy
XcjYEsk3VDwPPtVoa+uyG8V8t74Eau6xsM1ZM2F+jfLgijMc23n0Igk7RZCUFNss
Wv76+swBZv/Tp1Hg18nKMm7DjpAHNap1Jg97XeMeemXsxjRtt/VQATo42GnH54lH
-----END RSA PRIVATE KEY-----
"""

# JWT签名私钥密码
_RSA_PRIVATE_PASSPHRASE = 'DjangoPlayground'

# JWT签名算法密钥与KEY
JWT_SECRET_KEY = web.RsaAlgorithm('PS384',
                                  public_key=_RSA_PUBLIC,
                                  private_key=_RSA_PRIVATE,
                                  passphrase=_RSA_PRIVATE_PASSPHRASE)
