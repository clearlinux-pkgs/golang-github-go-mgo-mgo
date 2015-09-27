Name     : golang-github-go-mgo-mgo 
Version  : 2015.06.03
Release  : 1
URL      : https://github.com/go-mgo/mgo/archive/r2015.06.03.tar.gz
Source0  : https://github.com/go-mgo/mgo/archive/r2015.06.03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : go
BuildRequires : mongodb-bin

%description
The MongoDB driver for Go
-------------------------
Please go to [http://labix.org/mgo](http://labix.org/mgo) for all project details.

%prep
%setup -q -n mgo-r2015.06.03

%build

%install
%global gopath /usr/lib/golang
%global library_path github.com/gorilla/context
install -d -p %{buildroot}/%{gopath}/src/%{library_path}/
cp -pav *.go %{buildroot}/%{gopath}/src/%{library_path}/

# copy directories
for file in ./* ; do
    if [ -d $file ]; then
        cp -rpav $file %{buildroot}%{gopath}/src/%{library_path}/
    fi
done

# Requires supervisord
# %check 
# mkdir -p src/gopkg.in
# ln -s ../../ src/gopkg.in/mgo.v2
# export GOPATH=$(pwd):%{gopath}
# make startdb
# go test -gocheck.v
# make stopdb

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/gorilla/context/auth.go
/usr/lib/golang/src/github.com/gorilla/context/auth_test.go
/usr/lib/golang/src/github.com/gorilla/context/bson/LICENSE
/usr/lib/golang/src/github.com/gorilla/context/bson/bson.go
/usr/lib/golang/src/github.com/gorilla/context/bson/bson_test.go
/usr/lib/golang/src/github.com/gorilla/context/bson/decode.go
/usr/lib/golang/src/github.com/gorilla/context/bson/encode.go
/usr/lib/golang/src/github.com/gorilla/context/bulk.go
/usr/lib/golang/src/github.com/gorilla/context/bulk_test.go
/usr/lib/golang/src/github.com/gorilla/context/cluster.go
/usr/lib/golang/src/github.com/gorilla/context/cluster_test.go
/usr/lib/golang/src/github.com/gorilla/context/doc.go
/usr/lib/golang/src/github.com/gorilla/context/export_test.go
/usr/lib/golang/src/github.com/gorilla/context/gridfs.go
/usr/lib/golang/src/github.com/gorilla/context/gridfs_test.go
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sasl.c
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sasl.go
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sasl_windows.c
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sasl_windows.go
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sasl_windows.h
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sspi_windows.c
/usr/lib/golang/src/github.com/gorilla/context/internal/sasl/sspi_windows.h
/usr/lib/golang/src/github.com/gorilla/context/internal/scram/scram.go
/usr/lib/golang/src/github.com/gorilla/context/internal/scram/scram_test.go
/usr/lib/golang/src/github.com/gorilla/context/log.go
/usr/lib/golang/src/github.com/gorilla/context/queue.go
/usr/lib/golang/src/github.com/gorilla/context/queue_test.go
/usr/lib/golang/src/github.com/gorilla/context/raceoff.go
/usr/lib/golang/src/github.com/gorilla/context/raceon.go
/usr/lib/golang/src/github.com/gorilla/context/saslimpl.go
/usr/lib/golang/src/github.com/gorilla/context/saslstub.go
/usr/lib/golang/src/github.com/gorilla/context/server.go
/usr/lib/golang/src/github.com/gorilla/context/session.go
/usr/lib/golang/src/github.com/gorilla/context/session_test.go
/usr/lib/golang/src/github.com/gorilla/context/socket.go
/usr/lib/golang/src/github.com/gorilla/context/stats.go
/usr/lib/golang/src/github.com/gorilla/context/suite_test.go
/usr/lib/golang/src/github.com/gorilla/context/syscall_test.go
/usr/lib/golang/src/github.com/gorilla/context/syscall_windows_test.go
/usr/lib/golang/src/github.com/gorilla/context/testdb/client.pem
/usr/lib/golang/src/github.com/gorilla/context/testdb/dropall.js
/usr/lib/golang/src/github.com/gorilla/context/testdb/init.js
/usr/lib/golang/src/github.com/gorilla/context/testdb/server.pem
/usr/lib/golang/src/github.com/gorilla/context/testdb/setup.sh
/usr/lib/golang/src/github.com/gorilla/context/testdb/supervisord.conf
/usr/lib/golang/src/github.com/gorilla/context/testdb/wait.js
/usr/lib/golang/src/github.com/gorilla/context/testserver/export_test.go
/usr/lib/golang/src/github.com/gorilla/context/testserver/testserver.go
/usr/lib/golang/src/github.com/gorilla/context/testserver/testserver_test.go
/usr/lib/golang/src/github.com/gorilla/context/txn/chaos.go
/usr/lib/golang/src/github.com/gorilla/context/txn/debug.go
/usr/lib/golang/src/github.com/gorilla/context/txn/dockey_test.go
/usr/lib/golang/src/github.com/gorilla/context/txn/flusher.go
/usr/lib/golang/src/github.com/gorilla/context/txn/mgo_test.go
/usr/lib/golang/src/github.com/gorilla/context/txn/sim_test.go
/usr/lib/golang/src/github.com/gorilla/context/txn/tarjan.go
/usr/lib/golang/src/github.com/gorilla/context/txn/tarjan_test.go
/usr/lib/golang/src/github.com/gorilla/context/txn/txn.go
/usr/lib/golang/src/github.com/gorilla/context/txn/txn_test.go
