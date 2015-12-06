%global modname pysegbase

Name:           python-%{modname}
Version:        1.1.2
Release:        1%{?dist}
Summary:        3D graph cut segmentation

License:        BSD
URL:            https://pypi.python.org/pypi/pysegbase
Source0:        https://github.com/mjirik/pysegbase/archive/%{version}/%{modname}-%{version}.tar.gz
# https://github.com/mjirik/pysegbase/pull/31
Patch0:         0001-py3-QString.patch
Patch1:         0002-py3-assertCountEqual.patch
Patch2:         0003-py3-fix-test_multiscale_gc_seg-with-division.patch
Patch3:         0004-dicom-in-upstream-now-pydicom.patch
Patch4:         0005-py3-absolute_import.patch
Patch5:         0006-py3-print_function.patch
Patch6:         0007-py3-dict-methods.patch
Patch7:         0008-py3-xrange-range.patch
Patch8:         0009-py3-raw_input-input.patch
Patch9:         0010-py3-setup.py-mention-py3-support.patch
BuildArch:      noarch

%description
Segmentation tools based on the graph cut algorithm.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel Cython
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy python2-scipy
Requires:       python2-numpy python2-scipy
%else
BuildRequires:  numpy scipy
Requires:       numpy scipy
%endif
BuildRequires:  python2-nose
BuildRequires:  python-qt4
BuildRequires:  python2-pydicom
BuildRequires:  python2-dill
Requires:       python-qt4
Requires:       python2-pydicom
Requires:       python2-scikit-image python-scikit-learn
Requires:       python2-dill
Requires:       python2-yaml

%description -n python2-%{modname}
Segmentation tools based on the graph cut algorithm.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-Cython
BuildRequires:  python3-numpy python3-scipy
BuildRequires:  python3-nose
BuildRequires:  python3-qt4
BuildRequires:  python3-pydicom
BuildRequires:  python3-dill
Requires:       python3-numpy python3-scipy
Requires:       python3-qt4
Requires:       python3-pydicom
Requires:       python3-scikit-image python3-scikit-learn
Requires:       python3-dill
Requires:       python3-yaml

%description -n python3-%{modname}
Segmentation tools based on the graph cut algorithm.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

sed -i '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python2_sitelib}/%{modname}/*.py
sed -i '1{\@^#!/usr/bin/env python@d}' %{buildroot}%{python3_sitelib}/%{modname}/*.py

%check
pushd tests
  PYTHONPATH=%{buildroot}%{python2_sitelib} nosetests-%{python2_version} -v -e test_external_fv_with_save
  PYTHONPATH=%{buildroot}%{python3_sitelib} nosetests-%{python3_version} -v -e test_external_fv_with_save
popd

%files -n python2-%{modname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.1.2-1
- Initial package
