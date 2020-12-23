# Classifications

Using the `/api/transaction/{TXID}/script` endpoint you can get the parsed script with its classification.

Every script object has the same base structure

```
{
  "opcode_str":string,
  "opcodes":[
    {
      "code":string,
      "data":[string]
    }
  ],
  "classifier":{
    "classification":string
  }
}
```

The aformentioned endpoint will return data in the following structure:

```
{
  "txid": string",
  "input_scripts": [script],
  "output_scripts": [script]
}
```

if the script is an input script, it might have some extra properties.

```
{
  "opcode_str":string,
  "opcodes":[
    {
      "code":string,
      "data":[string]
    }
  ],
  "classifier":{
    "classification":string
  },
  
  // extra for input scripts
  "prevout": optional script,
  "inner_redeemscript_asm": optional script,
  "inner_witnessscript_asm": optional script,
}
```

It might be that only a subset (or none) of these extra keys are present.  
If a script is present in one of these attributes, it can be assumed that it is of the aformentioned script type.

# Optional data attribute
The classifier object of a script might contain an extra data attribute.
The presence and structure of this object depends on the classification.

 * **unknown** - optional `{"type": "coinbase"}` to indicate a coinbase transaction
 * **checkmultisig** - `[number, number]` to indicate an "x out of y" multisig transaction
 * **null_data_unspendable** - optional `{"protocol": string}` - only present if the protocol is known. Protocol will be a human-readable string.

# Classifiers

The following is a list of all possible classifications

 * **unknown**
 * **checkmultisig**
 * **null_data_unspendable**
 * **pay_to_publick_key_hash**
 * **pay_to_public_key**
 * **pay_to_script_hash**
 * **pay_to_witness_public_key_hash**
 * **pay_to_witness_script_hash**
