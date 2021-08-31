import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char # k-anonymity model
    res = requests.get(url)

    if res.status_code != 200:
        print(f'Error fetching: {res.status_code}, check the API.')
    else:
        return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines()) # tuple where each element is an array that contains hash tail and leaks count  
    
    for hash, count in hashes:
        if hash == hash_to_check:
            return count
    
    return 0

def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # sha1 obj to hexadecimal string then upper to agree with the API

    first5_chars, tail = sha1_password[:5], sha1_password[5:] # first five elements of the hash and the rest

    response = request_api_data(first5_chars) # API will response with all the hashes beginning with 'first5_chars'
    
    leaks_count = get_password_leaks_count(response, tail) # it'll check if bewteen all the hashes returned, there is match with the tail

    return leaks_count

def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'{password} was found {count} times..., you should change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
        
    return 'All done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
