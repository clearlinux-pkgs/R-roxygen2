#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-roxygen2
Version  : 6.0.1
Release  : 57
URL      : https://cran.r-project.org/src/contrib/roxygen2_6.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/roxygen2_6.0.1.tar.gz
Summary  : In-Line Documentation for R
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-roxygen2-lib
Requires: R-brew
Requires: R-commonmark
Requires: R-desc
BuildRequires : R-brew
BuildRequires : R-commonmark
BuildRequires : R-desc
BuildRequires : R-devtools
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : clr-R-helpers

%description
field using specially formatted comments. Writing documentation in-line
    with code makes it easier to keep your documentation up-to-date as your
    requirements change. 'Roxygen2' is inspired by the 'Doxygen' system for C++.

%package lib
Summary: lib components for the R-roxygen2 package.
Group: Libraries

%description lib
lib components for the R-roxygen2 package.


%prep
%setup -q -c -n roxygen2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502419950

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502419950
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library roxygen2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library roxygen2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library roxygen2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/roxygen2/DESCRIPTION
/usr/lib64/R/library/roxygen2/INDEX
/usr/lib64/R/library/roxygen2/Meta/Rd.rds
/usr/lib64/R/library/roxygen2/Meta/features.rds
/usr/lib64/R/library/roxygen2/Meta/hsearch.rds
/usr/lib64/R/library/roxygen2/Meta/links.rds
/usr/lib64/R/library/roxygen2/Meta/nsInfo.rds
/usr/lib64/R/library/roxygen2/Meta/package.rds
/usr/lib64/R/library/roxygen2/Meta/vignette.rds
/usr/lib64/R/library/roxygen2/NAMESPACE
/usr/lib64/R/library/roxygen2/NEWS.md
/usr/lib64/R/library/roxygen2/R/roxygen2
/usr/lib64/R/library/roxygen2/R/roxygen2.rdb
/usr/lib64/R/library/roxygen2/R/roxygen2.rdx
/usr/lib64/R/library/roxygen2/doc/collate.R
/usr/lib64/R/library/roxygen2/doc/collate.Rmd
/usr/lib64/R/library/roxygen2/doc/collate.html
/usr/lib64/R/library/roxygen2/doc/formatting.R
/usr/lib64/R/library/roxygen2/doc/formatting.Rmd
/usr/lib64/R/library/roxygen2/doc/formatting.html
/usr/lib64/R/library/roxygen2/doc/index.html
/usr/lib64/R/library/roxygen2/doc/markdown.R
/usr/lib64/R/library/roxygen2/doc/markdown.Rmd
/usr/lib64/R/library/roxygen2/doc/markdown.html
/usr/lib64/R/library/roxygen2/doc/namespace.R
/usr/lib64/R/library/roxygen2/doc/namespace.Rmd
/usr/lib64/R/library/roxygen2/doc/namespace.html
/usr/lib64/R/library/roxygen2/doc/rd.R
/usr/lib64/R/library/roxygen2/doc/rd.Rmd
/usr/lib64/R/library/roxygen2/doc/rd.html
/usr/lib64/R/library/roxygen2/doc/rdkeywords.R
/usr/lib64/R/library/roxygen2/doc/rdkeywords.Rmd
/usr/lib64/R/library/roxygen2/doc/rdkeywords.html
/usr/lib64/R/library/roxygen2/doc/roxygen2.R
/usr/lib64/R/library/roxygen2/doc/roxygen2.Rmd
/usr/lib64/R/library/roxygen2/doc/roxygen2.html
/usr/lib64/R/library/roxygen2/help/AnIndex
/usr/lib64/R/library/roxygen2/help/aliases.rds
/usr/lib64/R/library/roxygen2/help/paths.rds
/usr/lib64/R/library/roxygen2/help/roxygen2.rdb
/usr/lib64/R/library/roxygen2/help/roxygen2.rdx
/usr/lib64/R/library/roxygen2/html/00Index.html
/usr/lib64/R/library/roxygen2/html/R.css
/usr/lib64/R/library/roxygen2/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/roxygen2/libs/roxygen2.so
/usr/lib64/R/library/roxygen2/libs/roxygen2.so.avx2
