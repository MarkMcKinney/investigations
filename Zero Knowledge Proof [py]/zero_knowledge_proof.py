from random import SystemRandom
'''
Private Config
'''
secret = 11271989 # Secret value only known to the prover — let's say it's a shared friend's birthday (MMDDYYYY)

'''
Public Config
'''
p = 23 # Prime
g = 5 # Generator of the group modulo p
'''
Private generation
'''
encoded_secret = pow(g,secret,p) # South of truth and what we'll be comparing to

'''
Step 1: Commitment (Prover)
The prover must "commit" to their private answer which will be turned into public "encoded" version.
'''
def generateCommitmentValue():
    # Generate a random nonce ("number used once")
    gen = SystemRandom()
    nonce = gen.randrange(p)
    commitment_value = pow(g,nonce,p)
    return commitment_value, nonce

'''
Step 2: Challenge (Verifier)
The Prover stores the commitment_value, and then the Verifier generates and sends a challenge value based on the public Prime.
'''
def generateChallenge(commitment_value):
    gen = SystemRandom()
    challenge_value = gen.randrange(p)
    return challenge_value # Send to Prover

'''
Step 3: Response (Prover)
Prover sends the response to the challenge to the Verifier
'''
def generateResponse(challenge_value, nonce):
    response_value = nonce + challenge_value * secret
    return response_value # Send the response value back to the Verifier

'''
Step 3: Verification (Verifier)
Verifier confirms if the Prover's knows the correct answer/secret.
'''
def verify(encoded_secret, response_value, challenge_value):
    if pow(g,response_value,p) == (commitment_value * pow(encoded_secret, challenge_value, p)) % p:
        print(pow(g,response_value,p), (commitment_value * pow(encoded_secret, challenge_value, p)) % p)
        return True
    else:
        return False

commitment_value, nonce = generateCommitmentValue()
challenge_value = generateChallenge(commitment_value)
response_value = generateResponse(challenge_value, nonce)
print(verify(encoded_secret, response_value, challenge_value))