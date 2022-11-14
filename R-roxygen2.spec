#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-roxygen2
Version  : 7.2.2
Release  : 108
URL      : https://cran.r-project.org/src/contrib/roxygen2_7.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/roxygen2_7.2.2.tar.gz
Summary  : In-Line Documentation for R
Group    : Development/Tools
License  : MIT
Requires: R-roxygen2-lib = %{version}-%{release}
Requires: R-R6
Requires: R-brew
Requires: R-cli
Requires: R-commonmark
Requires: R-cpp11
Requires: R-desc
Requires: R-digest
Requires: R-knitr
Requires: R-pkgload
Requires: R-purrr
Requires: R-rlang
Requires: R-stringi
Requires: R-stringr
Requires: R-withr
Requires: R-xml2
BuildRequires : R-R.methodsS3
BuildRequires : R-R.oo
BuildRequires : R-R6
BuildRequires : R-brew
BuildRequires : R-cli
BuildRequires : R-commonmark
BuildRequires : R-cpp11
BuildRequires : R-desc
BuildRequires : R-digest
BuildRequires : R-knitr
BuildRequires : R-markdown
BuildRequires : R-pkgload
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-rmarkdown
BuildRequires : R-stringi
BuildRequires : R-stringr
BuildRequires : R-withr
BuildRequires : R-xml2
BuildRequires : buildreq-R

%description
collation field using specially formatted comments. Writing
    documentation in-line with code makes it easier to keep your
    documentation up-to-date as your requirements change. 'roxygen2' is
    inspired by the 'Doxygen' system for C++.

%package lib
Summary: lib components for the R-roxygen2 package.
Group: Libraries

%description lib
lib components for the R-roxygen2 package.


%prep
%setup -q -n roxygen2
cd %{_builddir}/roxygen2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668454756

%install
export SOURCE_DATE_EPOCH=1668454756
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/roxygen2/DESCRIPTION
/usr/lib64/R/library/roxygen2/INDEX
/usr/lib64/R/library/roxygen2/LICENSE
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
/usr/lib64/R/library/roxygen2/doc/index-crossref.R
/usr/lib64/R/library/roxygen2/doc/index-crossref.Rmd
/usr/lib64/R/library/roxygen2/doc/index-crossref.html
/usr/lib64/R/library/roxygen2/doc/index.html
/usr/lib64/R/library/roxygen2/doc/namespace.R
/usr/lib64/R/library/roxygen2/doc/namespace.Rmd
/usr/lib64/R/library/roxygen2/doc/namespace.html
/usr/lib64/R/library/roxygen2/doc/rd-formatting.R
/usr/lib64/R/library/roxygen2/doc/rd-formatting.Rmd
/usr/lib64/R/library/roxygen2/doc/rd-formatting.html
/usr/lib64/R/library/roxygen2/doc/rd-other.R
/usr/lib64/R/library/roxygen2/doc/rd-other.Rmd
/usr/lib64/R/library/roxygen2/doc/rd-other.html
/usr/lib64/R/library/roxygen2/doc/rd.R
/usr/lib64/R/library/roxygen2/doc/rd.Rmd
/usr/lib64/R/library/roxygen2/doc/rd.html
/usr/lib64/R/library/roxygen2/doc/reuse.R
/usr/lib64/R/library/roxygen2/doc/reuse.Rmd
/usr/lib64/R/library/roxygen2/doc/reuse.html
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
/usr/lib64/R/library/roxygen2/roxygen2-tags.yml
/usr/lib64/R/library/roxygen2/tests/testthat.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-2.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-3.R
/usr/lib64/R/library/roxygen2/tests/testthat/Rd-example-4.txt
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/block.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/collate.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/markdown-code.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/markdown-link.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/markdown-state.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/markdown.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/namespace.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/object-format.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/object-import.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/object-package.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/object-r6.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-describe-in.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-examples.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-find-link-files.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-include-rmd.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-inherit.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-markdown.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-r6.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-raw.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-section.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-template.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd-usage.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/rd.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/roxygenize-setup.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/select-args.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/tag-parser.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/tag.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/topics.md
/usr/lib64/R/library/roxygen2/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/roxygen2/tests/testthat/collate/belt.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/jacket.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/pants.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/shirt.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/shoes.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/socks.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/tie.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/undershorts.R
/usr/lib64/R/library/roxygen2/tests/testthat/collate/watch.R
/usr/lib64/R/library/roxygen2/tests/testthat/empty/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/empty/R/empty-package.R
/usr/lib64/R/library/roxygen2/tests/testthat/escapes.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/example.Rmd
/usr/lib64/R/library/roxygen2/tests/testthat/helper-test.R
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/empty.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/with-header.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/made-by-roxygen/without-header.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/man-roxygen/values.R
/usr/lib64/R/library/roxygen2/tests/testthat/no-desc/NAMESPACE
/usr/lib64/R/library/roxygen2/tests/testthat/no-desc/R/no-description.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-2.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-A.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-B.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3-C.Rd
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-block-3.R
/usr/lib64/R/library/roxygen2/tests/testthat/roxygen-example-1.R
/usr/lib64/R/library/roxygen2/tests/testthat/templates/man-roxygen/UCase.R
/usr/lib64/R/library/roxygen2/tests/testthat/templates/man-roxygen/lcase.r
/usr/lib64/R/library/roxygen2/tests/testthat/templates/man/roxygen/templates/new-path.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-block.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-collate.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-load.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-code.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-link.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown-state.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-markdown.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-namespace.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-defaults.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-format.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-from-call.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-import.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-package.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-r6.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-rc.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-object-s3.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/DESCRIPTION
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/man/roxygen/meta.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/meta-character.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-options/meta-error.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-package_files.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-parse.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-backref.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-describe-in.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-examples.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-family.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-find-link-files.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-rd-include-rmd.R
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
/usr/lib64/R/library/roxygen2/tests/testthat/test-roxygenize-setup.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-safety.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-select-args.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-tag-metadata.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-tag-parser.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-tag.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-tokenize.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-topic.R
/usr/lib64/R/library/roxygen2/tests/testthat/test-topics.R
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
