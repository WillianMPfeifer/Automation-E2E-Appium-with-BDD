from utils.logger import LoggerManager 
from utils.driver_factory import DriverFactory
import os
import shutil
from datetime import datetime
import pdb

def before_all(context):
    _clean_evidence_folder()

    context.logger = LoggerManager.setup_logger()
    context.logger.info("\n🚀 START: Iniciando execução da Suíte de Testes")

def before_scenario(context, scenario):
    context.logger.info(f"\n🎬 Iniciando cenário: {scenario.name}")
    
    context.driver = DriverFactory.get_driver(context.logger)

def after_step(context, step):
    if step.status == "failed":
        context.logger.error(f"❌ Falha no passo: '{step.name}'")
        _capture_evidence(context, step.name) 
        
        # MODO DEBUG (Descomente a linha abaixo quando quiser investigar um bug)
        context.logger.warning("⏸️ Pausando execução para Debug... Verifique o terminal!")
        pdb.post_mortem(step.exc_traceback)

def after_scenario(context, scenario):
    status_str = str(scenario.status).lower()

    if "failed" in status_str or "error" in status_str:
        context.logger.error(f"❌ O cenário terminou com problema! Status: {scenario.status}")
        context.logger.error("📸 Coletando evidências...")
        
        if not hasattr(context, 'evidence_captured'):
            _capture_evidence(context, scenario.name)
        
    elif "passed" in status_str:
        context.logger.info("✅ Cenário finalizado com sucesso.")
    
    else:
        context.logger.warning(f"⚠️ Cenário finalizado com status atípico: {scenario.status}")

    if hasattr(context, 'driver') and context.driver:
        context.logger.info("🏁 Encerrando sessão do Appium...")
        context.driver.quit()

def _clean_evidence_folder():
    evidence_dir = "reports/evidence"
    
    if os.path.exists(evidence_dir):
        try:
            shutil.rmtree(evidence_dir)
            print(f"🧹 Pasta de evidências limpa: {evidence_dir}")
        except Exception as e:
            print(f"⚠️ Erro ao limpar pasta de evidências: {e}")
    
    os.makedirs(evidence_dir, exist_ok=True)

def _capture_evidence(context, name_suffix):    
    if not hasattr(context, 'driver') or not context.driver:
        return

    context.evidence_captured = True 

    evidence_dir = "reports/evidence"
    if not os.path.exists(evidence_dir):
        os.makedirs(evidence_dir)

    safe_name = "".join([c if c.isalnum() else "_" for c in str(name_suffix)])
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    screenshot_path = f"{evidence_dir}/{safe_name}_{timestamp}.png"
    try:
        context.driver.save_screenshot(screenshot_path)
        context.logger.info(f"📸 Screenshot salvo em: {screenshot_path}")
    except Exception as e:
        context.logger.warning(f"⚠️ Falha ao salvar screenshot: {e}")

    source_path = f"{evidence_dir}/{safe_name}_{timestamp}.xml"
    try:
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(context.driver.page_source)
        context.logger.info(f"📄 Page Source salvo em: {source_path}")
    except Exception as e:
        context.logger.warning(f"⚠️ Falha ao salvar page source: {e}")