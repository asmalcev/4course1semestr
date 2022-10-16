login=network-testing
password=network12345

email_from=i59514@voenmeh.ru
email_to=senenjaqsy@vk.com

echo $login | base64
echo $password | base64

# From: $email_from
# To: $email_to
# Subject: Say hello


# openssl s_client -connect smtp.trashmail.com:465 -quiet <<EOF
# helo localhost
# auth login
# $(echo $login | base64)
# $(echo $password | base64)
# mail from: $email_from
# rcpt to: $email_from
# data
# Hello
# .

# quit
# EOF