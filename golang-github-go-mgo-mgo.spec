Name     : golang-github-go-mgo-mgo 
Version  : 2015.06.03
Release  : 4
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
%global library_path gopkg.in/mgo.v2
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
/usr/lib/golang/src/gopkg.in/mgo.v2/auth.go
/usr/lib/golang/src/gopkg.in/mgo.v2/auth_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/bson/LICENSE
/usr/lib/golang/src/gopkg.in/mgo.v2/bson/bson.go
/usr/lib/golang/src/gopkg.in/mgo.v2/bson/bson_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/bson/decode.go
/usr/lib/golang/src/gopkg.in/mgo.v2/bson/encode.go
/usr/lib/golang/src/gopkg.in/mgo.v2/bulk.go
/usr/lib/golang/src/gopkg.in/mgo.v2/bulk_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/cluster.go
/usr/lib/golang/src/gopkg.in/mgo.v2/cluster_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/doc.go
/usr/lib/golang/src/gopkg.in/mgo.v2/export_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/gridfs.go
/usr/lib/golang/src/gopkg.in/mgo.v2/gridfs_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sasl.c
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sasl.go
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sasl_windows.c
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sasl_windows.go
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sasl_windows.h
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sspi_windows.c
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/sasl/sspi_windows.h
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/scram/scram.go
/usr/lib/golang/src/gopkg.in/mgo.v2/internal/scram/scram_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/log.go
/usr/lib/golang/src/gopkg.in/mgo.v2/queue.go
/usr/lib/golang/src/gopkg.in/mgo.v2/queue_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/raceoff.go
/usr/lib/golang/src/gopkg.in/mgo.v2/raceon.go
/usr/lib/golang/src/gopkg.in/mgo.v2/saslimpl.go
/usr/lib/golang/src/gopkg.in/mgo.v2/saslstub.go
/usr/lib/golang/src/gopkg.in/mgo.v2/server.go
/usr/lib/golang/src/gopkg.in/mgo.v2/session.go
/usr/lib/golang/src/gopkg.in/mgo.v2/session_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/socket.go
/usr/lib/golang/src/gopkg.in/mgo.v2/stats.go
/usr/lib/golang/src/gopkg.in/mgo.v2/suite_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/syscall_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/syscall_windows_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/client.pem
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/dropall.js
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/init.js
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/server.pem
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/setup.sh
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/supervisord.conf
/usr/lib/golang/src/gopkg.in/mgo.v2/testdb/wait.js
/usr/lib/golang/src/gopkg.in/mgo.v2/testserver/export_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/testserver/testserver.go
/usr/lib/golang/src/gopkg.in/mgo.v2/testserver/testserver_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/chaos.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/debug.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/dockey_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/flusher.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/mgo_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/sim_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/tarjan.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/tarjan_test.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/txn.go
/usr/lib/golang/src/gopkg.in/mgo.v2/txn/txn_test.go
