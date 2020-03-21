REDIS_HOME="/home/redis"
REDIS_COMMANDS="/home/redis/redis.git/src"      # The location of the redis binary
REDIS_MASTER_IP="172.16.0.180"                  # Redis MASTER ip
REDIS_MASTER_PORT="6379"                        # Redis MASTER port

#
# We perform a simple query that should return a few results :-p

ERROR_MSG=`redis-cli PING`

#
# Check the output for PONG.
#
if [ "$ERROR_MSG" != "PONG" ]
then
        # redis is down, return http 503
        echo -e "HTTP/1.1 503 Service Unavailable\r\n"
        echo -e "Content-Type: Content-Type: text/plain\r\n"
        echo -e "\r\n"
        echo -e "Redis is *down*.\r\n"
        echo -e "\r\n"
else
        # redis is fine, return http 200
        echo -e "HTTP/1.1 200 OK\r\n"
        echo -e "Content-Type: Content-Type: text/plain\r\n"
        echo -e "\r\n"
        echo -e "Redis is running.\r\n"
        echo -e "\r\n"
fi