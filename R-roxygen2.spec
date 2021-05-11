#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-roxygen2
Version  : 7.1.1
Release  : 91
URL      : https://cran.r-project.org/src/contrib/roxygen2_7.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/roxygen2_7.1.1.tar.gz
Summary  : In-Line Documentation for R
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-roxygen2-lib = %{version}-%{release}
Requires: R-R6
Requires: R-Rcpp
Requires: R-brew
Requires: R-commonmark
Requires: R-desc
Requires: R-digest
Requires: R-knitr
Requires: R-pkgload
Requires: R-purrr
Requires: R-rlang
Requires: R-stringi
Requires: R-stringr
Requires: R-xml2
BuildRequires : R-R6
BuildRequires : R-Rcpp
BuildRequires : R-brew
BuildRequires : R-commonmark
BuildRequires : R-desc
BuildRequires : R-digest
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : R-pkgload
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-stringi
BuildRequires : R-stringr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
and collation field using specially formatted comments. Writing
    documentation in-line with code makes it easier to keep your
    documentation up-to-date as your requirements change. 'Roxygen2' is
    inspired by the 'Doxygen' system for C++.

%package lib
Summary: lib components for the R-roxygen2 package.
Group: Libraries

%description lib
lib components for the R-roxygen2 package.


%prep
%setup -q -c -n roxygen2
cd %{_builddir}/roxygen2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620764451

%install
export SOURCE_DATE_EPOCH=1620764451
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc roxygen2 || :


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
/usr/lib64/R/library/roxygen2/doc/extending.R
/usr/lib64/R/library/roxygen2/doc/extending.Rmd
/usr/lib64/R/library/roxygen2/doc/extending.html
/usr/lib64/R/library/roxygen2/doc/index.html
/usr/lib64/R/library/roxygen2/doc/namespace.R
/usr/lib64/R/library/roxygen2/doc/namespace.Rmd
/usr/lib64/R/library/roxygen2/doc/namespace.html
/usr/lib64/R/library/roxygen2/doc/rd-formatting.R
/usr/lib64/R/library/roxygen2/doc/rd-formatting.Rmd
/usr/lib64/R/library/roxygen2/doc/rd-formatting.html
/usr/lib64/R/library/roxygen2/doc/rd.R
/usr/lib64/R/library/roxygen2/doc/rd.Rmd
/usr/lib64/R/library/roxygen2/doc/rd.html
/usr/lib64/R/library/roxygen2/doc/roxygen2.R
/usr/lib64/R/library/roxygen2/doc/roxygen2.Rmd
/usr/lib64/R/library/roxygen2/doc/roxygen2.html
/usr/lib64/R/library/roxygen2/help/AnIndex
/usr/lib64/R/library/roxygen2/help/aliases.rds
/usr/lib64/R/library/roxygen2/help/figures/logo.png
/usr/lib64/R/library/roxygen2/help/figures/test-figure-1.png
/usr/lib64/R/library/roxygen2/help/paths.rds
/usr/lib64/R/library/roxygen2/help/roxygen2.rdb
/usr/lib64/R/library/roxygen2/help/roxygen2.rdx
/usr/lib64/R/library/roxygen2/html/00Index.html
/usr/lib64/R/library/roxygen2/html/R.css
/usr/lib64/R/library/roxygen2/tests/testthat.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-2.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-3.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-4.txt
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
/usr/lib64/R/library/roxygen2/tests/testthat/helper-pkg.R
/usr/lib64/R/library/roxygen2/tests/testthat/helper-test.R
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/empty.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/with-header.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/without-header.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/man-roxygen/values.R
/usr/lib64/R/library/roxygen2/tests/testthat/markdown-code-errors.txt
/usr/lib64/R/library/roxygen2/tests/testthat/no-desc/NAMESPACE
/usr/lib64/R/library/roxygen2/tests/testthat/no-desc/R/no-description.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-2.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-A.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-B.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-C.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-warnings.txt
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-example-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/templates/man-roxygen/UCase.R
/usr/lib64/R/library/roxygen2/tests/testthat/templates/man-roxygen/lcase.r
/usr/lib64/R/library/roxygen2/tests/testthat/templates/man/roxygen/templates/new-path.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-block-print.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-block.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-collate.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-load.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-code.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-link.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-state.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-table.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-namespace.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-defaults.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-format-r4.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-format.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-format.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-from-call.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-import.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-import.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-package-author.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-package.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-rc.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-s3.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-usage-wrap-new.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-usage-wrap-old.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-options.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/man/roxygen/meta.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/meta-character.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/meta-error.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-package_files.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-parse.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-backref.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-describe-in.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-examples-dontrun-escape-2.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-examples-dontrun-escape.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-examples-interleave.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-examples.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-family.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-includermd.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-inherit-dots-inherit.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-inherit-dots-multi.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-inherit-dots.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-inherit-link.txt
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-inherit.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-markdown-escaping.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-markdown.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-name-alias.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-params.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-r6.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-raw.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-s4.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-section.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-simple.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-template.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-usage.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-safety.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-select-args.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-tag.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-tokenize.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-topic.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-utils-io.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-utils-rd.R
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
/usr/lib64/R/library/roxygen2/tests/testthat/testNamespace/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/testNamespace/NAMESPACE
/usr/lib64/R/library/roxygen2/tests/testthat/testNamespace/R/a.r
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
/usr/lib64/R/library/roxygen2/libs/roxygen2.so.avx512
