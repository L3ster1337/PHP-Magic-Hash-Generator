# Usage
Magic hash generator for Type Juggling test. Usage e.g
`python3 xpl.py`

# Understanding the problem

Vulnerable hash example:
```
larry     | 0e656540908354891055044945395170 
```
Imagine the above user case. If a hash starting with *0e* is compared directly via *==*, in PHP, followed by numbers, the function is vulnerable to loose comparison. So, an attacker could test a lot of character combinations to reach the Authentication Bypass. You can check below a vulnerable snippet comparison

Loose Comparison:
```php
  if ($row = mysqli_fetch_assoc($result)) {
        if (pw_hash($password) == $row["password"]){
            return True;
        }
    }
    return False;
```

Hash function:
```php
function pw_hash($password){
    $salt = 'it6z';
    $hash = md5($salt . $password);
    return $hash;
}
```  

Running xpl.py, you can check the result as follow:

Found: xa7ah => 0e841056898366720026571892032475

It means that, using *xa7ah* as password, you are able to login to larry's account.




