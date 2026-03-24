docker run --network=proselyte-backend-network --name nginx-server -p 8070:8080 \
-v /mnt/c/Users/user/projects/my-web-site/proselyte-nginx-sources/nginx.conf:/etc/nginx/nginx.conf \
-d nginx
