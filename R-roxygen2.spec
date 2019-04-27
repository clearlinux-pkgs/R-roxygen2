#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-roxygen2
Version  : 6.1.1
Release  : 69
URL      : https://cran.r-project.org/src/contrib/roxygen2_6.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/roxygen2_6.1.1.tar.gz
Summary  : In-Line Documentation for R
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-roxygen2-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-stringi
Requires: R-xml2
BuildRequires : R-Rcpp
BuildRequires : R-brew
BuildRequires : R-commonmark
BuildRequires : R-desc
BuildRequires : R-devtools
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : R-pkgload
BuildRequires : R-purrr
BuildRequires : R-stringi
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
# roxygen2 <img src="man/figures/logo.png" align="right" />
[![Travis build status](https://travis-ci.org/klutometis/roxygen.svg?branch=master)](https://travis-ci.org/klutometis/roxygen)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/roxygen2)](https://cran.r-project.org/package=roxygen2)
[![Coverage status](https://codecov.io/gh/klutometis/roxygen/branch/master/graph/badge.svg)](https://codecov.io/github/klutometis/roxygen?branch=master)
> all' hileth', Hephaiste; didou d'areten te kai olbon.*
> --Homer, 7th century BCE

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
export SOURCE_DATE_EPOCH=1552956427

%install
export SOURCE_DATE_EPOCH=1552956427
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library roxygen2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
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
R CMD check --no-manual --no-examples --no-codoc  roxygen2 || :


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
/usr/lib64/R/library/roxygen2/help/figures/logo.png
/usr/lib64/R/library/roxygen2/help/paths.rds
/usr/lib64/R/library/roxygen2/help/roxygen2.rdb
/usr/lib64/R/library/roxygen2/help/roxygen2.rdx
/usr/lib64/R/library/roxygen2/html/00Index.html
/usr/lib64/R/library/roxygen2/html/R.css
/usr/lib64/R/library/roxygen2/tests/testthat.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-2.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-3.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-4.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-5.txt
/usr/lib64/R/library/roxygen2/tests/testthat/collate/belt.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/jacket.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/pants.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/shirt.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/shoes.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/socks.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/tie.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/undershorts.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/watch.R
/usr/lib64/R/library/roxygen2/tests/testthat/description-example.txt
/usr/lib64/R/library/roxygen2/tests/testthat/description-example_2.txt
/usr/lib64/R/library/roxygen2/tests/testthat/empty/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/empty/R/empty-package.R
/usr/lib64/R/library/roxygen2/tests/testthat/escapes.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/helper-env.R
/usr/lib64/R/library/roxygen2/tests/testthat/helper-pkg.R
/usr/lib64/R/library/roxygen2/tests/testthat/helper-test.R
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/empty.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/with-header.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/without-header.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/man-roxygen/UCase.R
/usr/lib64/R/library/roxygen2/tests/testthat/man-roxygen/lcase.r
/usr/lib64/R/library/roxygen2/tests/testthat/man-roxygen/reg.ex.R
/usr/lib64/R/library/roxygen2/tests/testthat/man-roxygen/values.R
/usr/lib64/R/library/roxygen2/tests/testthat/no-desc/NAMESPACE
/usr/lib64/R/library/roxygen2/tests/testthat/no-desc/R/no-description.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-2.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-example-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-Rbuildignore.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-Rd-inherit.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-collate.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-eval.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-namespace.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-nice-name.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-format.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-package.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-rc.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-s3.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-s4.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-parse-block.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-parse.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-alias.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-backref.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-data.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-describein.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-doctype.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-examples.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-family.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-field.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-introduction.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-keyword.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-markdown-escaping.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-markdown-links.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-markdown-on-off.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-markdown.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-name.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-package.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-param.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-raw.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-section.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-slot.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-template.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-usage.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rdComplete.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-reexport.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-safety.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-select_args.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-topic.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-utf8.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-utils.R
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateNoIncludes/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateNoIncludes/NAMESPACE
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateNoIncludes/R/a.r
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateNoIncludes/R/b.r
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateOverwrite/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateOverwrite/R/a.r
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateOverwrite/R/b.r
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateParse/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateParse/R/b.r
/usr/lib64/R/library/roxygen2/tests/testthat/testCollateParse/R/c.r
/usr/lib64/R/library/roxygen2/tests/testthat/testEagerData/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testEagerData/R/a.r
/usr/lib64/R/library/roxygen2/tests/testthat/testEagerData/data/a.rda
/usr/lib64/R/library/roxygen2/tests/testthat/testLazyData/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testLazyData/NAMESPACE
/usr/lib64/R/library/roxygen2/tests/testthat/testLazyData/R/a.r
/usr/lib64/R/library/roxygen2/tests/testthat/testLazyData/data/a.rda
/usr/lib64/R/library/roxygen2/tests/testthat/testNonASCII/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testNonASCII/R/a.r
/usr/lib64/R/library/roxygen2/tests/testthat/testRbuildignore/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testRbuildignore/R/a.R
/usr/lib64/R/library/roxygen2/tests/testthat/testRbuildignore/R/ignore_me.R
/usr/lib64/R/library/roxygen2/tests/testthat/testUtf8Escape/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testUtf8Escape/R/a.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/roxygen2/libs/roxygen2.so
/usr/lib64/R/library/roxygen2/libs/roxygen2.so.avx2
