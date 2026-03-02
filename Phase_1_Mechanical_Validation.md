# Phase 1 – Mechanical Validation (Post-Collection)

Date: [Insert Date]
Goal: Prove mechanical stability + oil pressure behavior before any power/rpm changes.

---

## ✅ Day 0: Collection / First Start Checks

Before driving hard:
- Confirm coolant level + overflow bottle level
- Confirm oil level (engine cold, flat ground)
- Check for fuel smell / leaks (engine bay + under car)
- Check for loose battery terminals
- Check for abnormal noises (chain rattle, metallic tick, header leak)

Cold start observation:
- Smoke? (white/blue)
- Idle stability after ~60–90 sec
- Any misfire / hunting / stalling

---

## ✅ Warm-Up Protocol (Every time)

- Start → idle 30–60 sec only
- Drive gently until coolant is stable
- DO NOT exceed ~4,000 rpm until oil is warm (if no oil temp gauge, be conservative: 10–15 minutes normal driving)

---

## ✅ Oil Pressure Targets (Guidelines)

These are not absolute, but "sanity bands" for a built K24 with Type R pump:

Hot idle (after a drive):
- Expected: ~15–30 psi
- Red flag: <10 psi consistently (stop and investigate)

4,000 rpm cruise (fully warm):
- Expected: ~45–70 psi (varies by relief spring / clearances)
- Red flag: does not rise with rpm, or fluctuates badly

High rpm (WOT pull):
- Expected: smooth rise with rpm, no sudden dip near redline
- Red flag: pressure drop at high rpm / after repeated pulls (possible aeration / pickup / oil level issue)

Note:
- Pressure “number” matters less than “shape”: it must rise smoothly and remain stable.

---

## ✅ First Drive Validation (No Hero Pulls)

Step 1: 10–15 min normal driving
- Check temps stable
- Check oil pressure normal behavior
- Listen for exhaust leaks / rattles

Step 2: One medium pull (3rd gear) 3,000 → 6,500 rpm
- Smooth? Any breakup?
- Oil pressure stable?
- No knock noise?

Step 3: If Step 2 clean → one pull to 7,500 rpm
- Stop if any breakup / misfire / oil pressure dip

Do NOT go to 8,500 on day 1 unless everything is confirmed stable.

---

## ✅ Link ECU Logging Checklist (Minimum)

Log these channels (or observe live if no logging yet):
- RPM
- TPS (throttle position)
- MAP (or vacuum)
- Lambda / AFR (if available)
- Injector duty cycle
- Ignition timing
- Coolant temp
- IAT (intake air temp)
- Battery voltage
- Knock level / knock control activity (if configured)
- Oil pressure (if wired into ECU; otherwise note from gauge)

---

## ✅ Fuel System Validation (Because you can’t see fuel pressure in cabin)

Since fuel pressure gauge is in engine bay:
- Confirm base fuel pressure once (engine idling)
- Confirm it increases with vacuum reference if using reg referenced to manifold (if applicable)
- Watch injector duty: target keep <90% at redline

If injector duty approaches 95–100%:
- Stop high-rpm pulls
- Plan injectors upgrade + retune

---

## ✅ Oil & Filter First Service (Baseline Cleanout)

Plan:
- Replace oil with Penrite HPR 5 5W-40 (already purchased)
- New quality filter (OEM Honda recommended)
- Optional: cut open old filter to inspect for glitter/metal

First interval:
- 800–1,500 km baseline interval
- Then recheck oil condition and decide long-term oil (possible upgrade to racing 10W-40 if temps/pressure justify)

---

## ✅ Hard Stop Conditions (Do NOT continue driving)

Stop and investigate if:
- Oil pressure drops suddenly at rpm
- Oil pressure becomes unstable / fluttering under load
- New loud valvetrain noise appears after a pull
- Coolant temp climbs uncontrollably
- Misfire/breakup appears near higher rpm (especially 7k+)
- Fuel smell / visible leak

---

## ✅ Phase 1 Exit Criteria (Green Light for Phase 2)

Proceed to Phase 2 (rpm or injector changes) ONLY if:
- Oil pressure behavior is stable and repeatable
- Engine pulls cleanly to current 8,500 soft limit
- No abnormal heat behavior
- Injector duty confirmed with margin (<90% preferred)
- No evidence of metal contamination in first oil change

---

## 🔜 Phase 2 (Planned Next Decisions)

- Set limiter strategy: 8,500 soft / 8,800 hard (only after validation)
- Consider injector upgrade to 550cc (if duty margin is tight)
- Consider fuel pressure sensor into Link for real-time monitoring
- Header change (4-2-1 → 4-1) only if dyno/logs show power still climbing at 8.5k and worth extending
