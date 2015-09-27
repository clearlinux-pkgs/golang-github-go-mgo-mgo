Name     : golang-github-go-mgo-mgo 
Version  : 2015.06.03
Release  : 2
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
%global library_path github.com/go-mgo/mgo
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
/usr/lib/golang/src/github.com/go-mgo/mgo/auth.go
/usr/lib/golang/src/github.com/go-mgo/mgo/auth_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/bson/LICENSE
/usr/lib/golang/src/github.com/go-mgo/mgo/bson/bson.go
/usr/lib/golang/src/github.com/go-mgo/mgo/bson/bson_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/bson/decode.go
/usr/lib/golang/src/github.com/go-mgo/mgo/bson/encode.go
/usr/lib/golang/src/github.com/go-mgo/mgo/bulk.go
/usr/lib/golang/src/github.com/go-mgo/mgo/bulk_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/cluster.go
/usr/lib/golang/src/github.com/go-mgo/mgo/cluster_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/doc.go
/usr/lib/golang/src/github.com/go-mgo/mgo/export_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/gridfs.go
/usr/lib/golang/src/github.com/go-mgo/mgo/gridfs_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sasl.c
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sasl.go
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sasl_windows.c
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sasl_windows.go
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sasl_windows.h
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sspi_windows.c
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/sasl/sspi_windows.h
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/scram/scram.go
/usr/lib/golang/src/github.com/go-mgo/mgo/internal/scram/scram_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/log.go
/usr/lib/golang/src/github.com/go-mgo/mgo/queue.go
/usr/lib/golang/src/github.com/go-mgo/mgo/queue_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/raceoff.go
/usr/lib/golang/src/github.com/go-mgo/mgo/raceon.go
/usr/lib/golang/src/github.com/go-mgo/mgo/saslimpl.go
/usr/lib/golang/src/github.com/go-mgo/mgo/saslstub.go
/usr/lib/golang/src/github.com/go-mgo/mgo/server.go
/usr/lib/golang/src/github.com/go-mgo/mgo/session.go
/usr/lib/golang/src/github.com/go-mgo/mgo/session_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/socket.go
/usr/lib/golang/src/github.com/go-mgo/mgo/stats.go
/usr/lib/golang/src/github.com/go-mgo/mgo/suite_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/syscall_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/syscall_windows_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/client.pem
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/dropall.js
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/init.js
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/server.pem
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/setup.sh
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/supervisord.conf
/usr/lib/golang/src/github.com/go-mgo/mgo/testdb/wait.js
/usr/lib/golang/src/github.com/go-mgo/mgo/testserver/export_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/testserver/testserver.go
/usr/lib/golang/src/github.com/go-mgo/mgo/testserver/testserver_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/chaos.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/debug.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/dockey_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/flusher.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/mgo_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/sim_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/tarjan.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/tarjan_test.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/txn.go
/usr/lib/golang/src/github.com/go-mgo/mgo/txn/txn_test.go
