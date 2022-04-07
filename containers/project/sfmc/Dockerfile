FROM ubuntu
RUN mkdir sfmc
COPY . ./sfmc
WORKDIR /sfmc
RUN ls -R > file_list.txt
CMD cat file_list.txt
