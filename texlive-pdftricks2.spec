%global tl_name pdftricks2
%global tl_revision 31016

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.01
Release:	%{tl_revision}.1
Summary:	Use PSTricks in pdfTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pdftricks2
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftricks2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means of processing documents (that contain
pstricks graphics specifications. The package is inspired by pdftricks

