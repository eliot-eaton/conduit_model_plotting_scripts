import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# Parameters — modify these values
# ============================================================
n_wi = 12


beta_v = 0.0
beta_b = 1.5e6  

wi_x_min = 1e5
wi_x_max = 1e8
num_points = 10000

# ============================================================
# Calculate the functions
# ============================================================
wi_x = np.logspace(
    np.log10(wi_x_min),
    np.log10(wi_x_max),
    num_points
)

ratio_power = (wi_x / 5e6) ** n_wi

S_wi = ratio_power / (1.0 + ratio_power)

beta_eff = beta_v + (beta_b - beta_v) * S_wi

wi_x_reference = [1e6, 1e5, 1e7]
beta_eff_reference = [
    beta_v + (beta_b - beta_v) * ((wi_x_ref / 5e6) ** n_wi) / (1.0 + (wi_x_ref / 5e6) ** n_wi)
    for wi_x_ref in wi_x_reference
]

S_wi_nonnav = (5e6/wi_x)**-n_wi
beta_eff_nonnav = beta_v + (beta_b - beta_v) * S_wi_nonnav

wi_c = 5e6
# ============================================================
# Plot
# ============================================================
fig, axes = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

# Plot S_Wi
axes[0].semilogx(
    wi_x,
    
    S_wi,
    linewidth=2,
    label=r"$S_{Wi}$"
)
axes[0].semilogx(
    wi_x,
    S_wi_nonnav,
    linewidth=2,
    label=r"$S_{Wi}$ non nav "
)

axes[0].axvline(
    wi_c,
    linestyle="--",
    label=fr"$Wi_c={wi_c:g}$"
)

axes[0].set_ylabel(r"$S_{Wi}$")
axes[0].set_title("Switching function")
axes[0].set_ylim(-0.05, 1.05)
axes[0].grid(True, which="both", alpha=0.3)
axes[0].legend()

# Plot beta_eff
axes[1].loglog(
    wi_x,
    beta_eff,
    linewidth=2,
    label=r"$\beta_{\mathrm{eff}}$"
)
axes[1].loglog(
    wi_x,
    beta_eff_nonnav,
    linewidth=2,
    label=r"$\beta_{\mathrm{eff}}$"
)
for wi_x_ref, beta_ref in zip(wi_x_reference, beta_eff_reference):
    axes[1].axhline(
        beta_ref,
        linestyle=":",
        linewidth=1.5,
        label=fr"$\beta_{{\mathrm{{eff}}}}(Wi_x={wi_x_ref:g})$"
    )

axes[1].axvline(
    wi_c,
    linestyle="--",
    label=fr"$Wi_c={wi_c:g}$"
)

axes[1].set_xlabel(r"$Wi_x$")
axes[1].set_ylabel(r"$\beta_{\mathrm{eff}}$")
axes[1].set_title("Effective beta")
axes[1].grid(True, which="both", alpha=0.3)
axes[1].legend()

plt.tight_layout()
plt.show()

# ============================================================
# Print useful values
# ============================================================
S_at_wi_c = 0.5
beta_at_wi_c = beta_v + (beta_b - beta_v) * S_at_wi_c

print(f"S_Wi at Wi_x = Wi_c: {S_at_wi_c}")
print(f"beta_eff at Wi_x = Wi_c: {beta_at_wi_c}")
for wi_x_ref, beta_ref in zip(wi_x_reference, beta_eff_reference):
    print(f"beta_eff at Wi_x = {wi_x_ref:g}: {beta_ref}")


def flc2hs(x, d):
    x = np.asarray(x, dtype=float)
    y = np.zeros_like(x)
    
    # Define the three piecewise regions
    low_mask = x < -d
    high_mask = x > d
    trans_mask = (x >= -d) & (x <= d)
    
    # Assign values
    y[low_mask] = 0.0
    y[high_mask] = 1.0
    
    # 5th-degree smooth polynomial for the transition zone
    u = x[trans_mask] / d
    y[trans_mask] = 0.5 + (15/16)*u - (5/8)*(u**3) + (3/16)*(u**5)
    
    return y
