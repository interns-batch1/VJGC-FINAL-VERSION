filepath = r"c:\Users\Admin\vjgc-final\vjs-website\static\css\custom.css"
with open(filepath, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Truncate at line 2650 (index 2649)
# Wait, let's find the actual line index for .serif-heading properties
target_index = -1
for i, line in enumerate(lines):
    if ".serif-heading {" in line:
        target_index = i + 4 # Skip properties
        break

if target_index != -1:
    lines = lines[:target_index]
    # Ensure it ends with a closing brace
    if "}" not in lines[-1]:
        lines.append("}\n")
    
    clean_code = """
.muted-desc {
    color: #666;
    font-size: 14px;
    line-height: 1.5;
    margin-bottom: 0;
}

@media (max-width: 992px) {
  .footer-main {
    grid-template-columns: 1fr 1fr;
    gap: 40px;
  }
}

@media (max-width: 768px) {
  .footer-main {
    grid-template-columns: 1fr;
    gap: 30px;
  }
  .footer-column {
    border-left: none;
    padding-left: 0;
  }
  .bottom-inner {
    flex-direction: column;
    gap: 20px;
    text-align: center;
  }
  .legal-links {
    flex-wrap: wrap;
    justify-content: center;
    gap: 10px 20px;
  }
}

/* ===== SCROLL TO TOP BUTTON ===== */
.vjs-scroll-top-btn {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #A2D732 0%, #1A4137 100%);
  border: none;
  border-radius: 50%;
  color: white;
  font-size: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 99999;
  opacity: 0;
  visibility: hidden;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  transform: translateY(20px);
}

.vjs-scroll-top-btn.visible {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.vjs-scroll-top-btn:hover {
  transform: translateY(-5px) scale(1.05);
  box-shadow: 0 15px 40px rgba(162, 215, 50, 0.4);
  color: #fff;
}

.vjs-scroll-top-btn i {
  line-height: 1;
}

@media (max-width: 768px) {
  .vjs-scroll-top-btn {
    width: 50px;
    height: 50px;
    bottom: 20px;
    right: 20px;
    font-size: 20px;
  }
}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(lines)
        f.write(clean_code)
    print("Successfully repaired custom.css")
else:
    print("Could not find truncation point")
