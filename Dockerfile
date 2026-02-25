# Use lightweight nginx to serve static files
FROM nginx:alpine

# Copy the static website into nginx's default serving directory
COPY frontend/ /usr/share/nginx/html/

# Expose port 80 for HTTP traffic
EXPOSE 80

# Start nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]