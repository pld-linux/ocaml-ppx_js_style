#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Code style checker for Jane Street Packages
Summary(pl.UTF-8):	Sprawdzanie stylu kodu dla pakietów Jane Street
Name:		ocaml-ppx_js_style
Version:	0.14.1
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_js_style/tags
Source0:	https://github.com/janestreet/ppx_js_style/archive/v%{version}/ppx_js_style-%{version}.tar.gz
# Source0-md5:	2d79afa4f954aeafb81b64ecfc11c3fb
URL:		https://github.com/janestreet/ppx_js_style
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-octavius-devel
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
ppx_js_style is an identity ppx rewriter that enforces Jane Street
coding styles.

This package contains files needed to run bytecode executables using
ppx_js_style library.

%description -l pl.UTF-8
ppx_js_style to identycznościowy moduł przepisujący ppx, wymuszający
styl kodowania Jane Street.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_js_style.

%package devel
Summary:	Code style checker for Jane Street Packages - development part
Summary(pl.UTF-8):	Sprawdzanie stylu kodu dla pakietów Jane Street - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-octavius-devel
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_js_style library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_js_style.

%prep
%setup -q -n ppx_js_style-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_js_style/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_js_style

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/ppx_js_style
%attr(755,root,root) %{_libdir}/ocaml/ppx_js_style/ppx.exe
%{_libdir}/ocaml/ppx_js_style/META
%{_libdir}/ocaml/ppx_js_style/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_js_style/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_js_style/*.cmi
%{_libdir}/ocaml/ppx_js_style/*.cmt
%{_libdir}/ocaml/ppx_js_style/*.cmti
%{_libdir}/ocaml/ppx_js_style/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_js_style/ppx_js_style.a
%{_libdir}/ocaml/ppx_js_style/*.cmx
%{_libdir}/ocaml/ppx_js_style/*.cmxa
%endif
%{_libdir}/ocaml/ppx_js_style/dune-package
%{_libdir}/ocaml/ppx_js_style/opam
