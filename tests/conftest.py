import sys
import types
import pytest

@pytest.fixture(autouse=True)
def stub_dependencies(monkeypatch):
    fpdf_mod = types.ModuleType('fpdf')
    class DummyFPDF:
        def add_page(self):
            pass
        def add_font(self, *args, **kwargs):
            pass
        def set_font(self, *args, **kwargs):
            pass
        def set_margins(self, *args, **kwargs):
            pass
        def multi_cell(self, *args, **kwargs):
            pass
        def set_draw_color(self, *args, **kwargs):
            pass
        def line(self, *args, **kwargs):
            pass
        def output(self, *args, **kwargs):
            pass
        y = 0
    fpdf_mod.FPDF = DummyFPDF
    monkeypatch.setitem(sys.modules, 'fpdf', fpdf_mod)

    docx_mod = types.ModuleType('docx')
    class DummyDocxDocument:
        def add_heading(self, *args, **kwargs):
            pass
        def add_paragraph(self, *args, **kwargs):
            pass
        def save(self, *args, **kwargs):
            pass
    docx_mod.Document = DummyDocxDocument
    monkeypatch.setitem(sys.modules, 'docx', docx_mod)

    import KindleClippings
    monkeypatch.setattr(KindleClippings, 'args', types.SimpleNamespace(format='txt'), raising=False)
