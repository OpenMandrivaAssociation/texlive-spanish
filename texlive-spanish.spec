# revision 24229
# category Package
# catalog-ctan /language/spanish/babel/base
# catalog-date 2011-10-06 19:10:39 +0200
# catalog-license lppl
# catalog-version 5.0k
Name:		texlive-spanish
Version:	5.0k
Release:	13
Summary:	Spanish in Babel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/spanish/babel/base
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanish.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spanish.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This bundle provides an upgrade of the Spanish support provided
by the LaTeX standard package babel. Note that separate support
is provided for those who wish to typeset Spanish as written in
Mexico.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/spanish/README
%doc %{_texmfdistdir}/doc/latex/spanish/romanidx.sty
%doc %{_texmfdistdir}/doc/latex/spanish/spanish.ldf
%doc %{_texmfdistdir}/doc/latex/spanish/spanish.pdf
%doc %{_texmfdistdir}/doc/latex/spanish/spanish2.html
#- source
%doc %{_texmfdistdir}/source/latex/spanish/spanish.dtx
%doc %{_texmfdistdir}/source/latex/spanish/spanish.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.0k-2
+ Revision: 756090
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.0k-1
+ Revision: 719560
- texlive-spanish
- texlive-spanish
- texlive-spanish
- texlive-spanish

