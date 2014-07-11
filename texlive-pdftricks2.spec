# revision 31016
# category Package
# catalog-ctan /graphics/pdftricks2
# catalog-date 2013-06-10 19:13:25 +0200
# catalog-license gpl2
# catalog-version 1.01
Name:		texlive-pdftricks2
Version:	1.01
Release:	7
Summary:	Use pstricks in pdfTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pdftricks2
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks2.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of processing documents (that
contain pstricks graphics specifications. The package is
inspired by pdftricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pdftricks2/pdftricks2.sty
%doc %{_texmfdistdir}/doc/latex/pdftricks2/README
%doc %{_texmfdistdir}/doc/latex/pdftricks2/pdftricks2-doc.pdf
%doc %{_texmfdistdir}/doc/latex/pdftricks2/pdftricks2-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
