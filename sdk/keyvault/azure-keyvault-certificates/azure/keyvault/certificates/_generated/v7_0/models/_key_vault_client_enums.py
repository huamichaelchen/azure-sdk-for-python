# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ActionType(str, Enum):
    """The type of the action.
    """

    email_contacts = "EmailContacts"
    auto_renew = "AutoRenew"

class DeletionRecoveryLevel(str, Enum):
    """Reflects the deletion recovery level currently in effect for keys in the current vault. If it
    contains 'Purgeable' the key can be permanently deleted by a privileged user; otherwise, only
    the system can purge the key, at the end of the retention interval.
    """

    purgeable = "Purgeable"
    recoverable_purgeable = "Recoverable+Purgeable"
    recoverable = "Recoverable"
    recoverable_protected_subscription = "Recoverable+ProtectedSubscription"

class JsonWebKeyCurveName(str, Enum):
    """Elliptic curve name. For valid values, see JsonWebKeyCurveName.
    """

    p256 = "P-256"  #: The NIST P-256 elliptic curve, AKA SECG curve SECP256R1.
    p384 = "P-384"  #: The NIST P-384 elliptic curve, AKA SECG curve SECP384R1.
    p521 = "P-521"  #: The NIST P-521 elliptic curve, AKA SECG curve SECP521R1.
    p256_k = "P-256K"  #: The SECG SECP256K1 elliptic curve.

class JsonWebKeyEncryptionAlgorithm(str, Enum):
    """algorithm identifier
    """

    rsa_oaep = "RSA-OAEP"
    rsa_oaep256 = "RSA-OAEP-256"
    rsa1_5 = "RSA1_5"

class JsonWebKeyOperation(str, Enum):
    """JSON web key operations. For more information, see JsonWebKeyOperation.
    """

    encrypt = "encrypt"
    decrypt = "decrypt"
    sign = "sign"
    verify = "verify"
    wrap_key = "wrapKey"
    unwrap_key = "unwrapKey"

class JsonWebKeySignatureAlgorithm(str, Enum):
    """The signing/verification algorithm identifier. For more information on possible algorithm
    types, see JsonWebKeySignatureAlgorithm.
    """

    ps256 = "PS256"  #: RSASSA-PSS using SHA-256 and MGF1 with SHA-256, as described in https://tools.ietf.org/html/rfc7518.
    ps384 = "PS384"  #: RSASSA-PSS using SHA-384 and MGF1 with SHA-384, as described in https://tools.ietf.org/html/rfc7518.
    ps512 = "PS512"  #: RSASSA-PSS using SHA-512 and MGF1 with SHA-512, as described in https://tools.ietf.org/html/rfc7518.
    rs256 = "RS256"  #: RSASSA-PKCS1-v1_5 using SHA-256, as described in https://tools.ietf.org/html/rfc7518.
    rs384 = "RS384"  #: RSASSA-PKCS1-v1_5 using SHA-384, as described in https://tools.ietf.org/html/rfc7518.
    rs512 = "RS512"  #: RSASSA-PKCS1-v1_5 using SHA-512, as described in https://tools.ietf.org/html/rfc7518.
    rsnull = "RSNULL"  #: Reserved.
    es256 = "ES256"  #: ECDSA using P-256 and SHA-256, as described in https://tools.ietf.org/html/rfc7518.
    es384 = "ES384"  #: ECDSA using P-384 and SHA-384, as described in https://tools.ietf.org/html/rfc7518.
    es512 = "ES512"  #: ECDSA using P-521 and SHA-512, as described in https://tools.ietf.org/html/rfc7518.
    es256_k = "ES256K"  #: ECDSA using P-256K and SHA-256, as described in https://tools.ietf.org/html/rfc7518.

class JsonWebKeyType(str, Enum):
    """JsonWebKey Key Type (kty), as defined in https://tools.ietf.org/html/draft-ietf-jose-json-web-
    algorithms-40.
    """

    ec = "EC"  #: Elliptic Curve.
    ec_hsm = "EC-HSM"  #: Elliptic Curve with a private key which is not exportable from the HSM.
    rsa = "RSA"  #: RSA (https://tools.ietf.org/html/rfc3447).
    rsa_hsm = "RSA-HSM"  #: RSA with a private key which is not exportable from the HSM.
    oct = "oct"  #: Octet sequence (used to represent symmetric keys).

class KeyUsageType(str, Enum):

    digital_signature = "digitalSignature"
    non_repudiation = "nonRepudiation"
    key_encipherment = "keyEncipherment"
    data_encipherment = "dataEncipherment"
    key_agreement = "keyAgreement"
    key_cert_sign = "keyCertSign"
    c_rl_sign = "cRLSign"
    encipher_only = "encipherOnly"
    decipher_only = "decipherOnly"

class SasTokenType(str, Enum):
    """The type of SAS token the SAS definition will create.
    """

    account = "account"
    service = "service"
