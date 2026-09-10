--[[
    =====================================================================
      MMB HUB  -  "Steal an Egg"  (rebranded readable build)
    =====================================================================
    * Deobfuscated from MoonVeil 2.0.23 VM bytecode (ClydeDump_02).
    * All string constants decrypted & inlined (4373 sites, 0 errors).
    * Rebranded: menu / webhooks / config keys now use the MMB HUB name.
      - The original UI library URL is kept INTACT on purpose; changing
        it would break the external UI loader.
    * Verified: compiles under Lua 5.1 and produces a byte-identical
      sandbox trace vs the original obfuscated script (modulo the
      documented TND->MMB key rename).
    * Variable names are preserved from the VM lifting (single letters);
      renaming them is NOT safe - the VM reuses registers across roles.
    Sections are marked with  --===== [tag] =====  comments.
]]
-- This script was generated using MoonVeil 2.0.23 [https://moonveil.cc]
return ({p = function (e, h)
    return function (d)
        local b, c, i, _, a, g
        _ = 253
        repeat
            if _ > 120 then
                if _ <= 0xaa then
                    if _ <= 139 then
                        i = false
                        return i
                    else
                        i = true
                        return i
                    end
                else
                    _, d = 0x78, {[2] = 3, [3] = d}
                    d[1] = d
                    c = nil
                    b, h[2][1][h[2][2]], c = e:_d{d, h[1], h[5]}, c, e._["pcall"]
                end
            elseif _ >= 0x6a then
                if _ <= 106 then
                    b = b(i, a, g)
                    i = h[2][1][h[2][2]]
                    _ = i and 0xf5 - _ or 0xaa
                else
                    c = c(b)
                    b = not c
                    _ = b and 0x2b20 / _ or 83
                end
            elseif _ <= 0x53 then
                i = h[3][1][h[3][2]]
                _, g, i, b, a = 106, e:Yc{h[4], h[2]}, 20, i["waitFor"], 0.25
            else
                b = false
                return b
            end
        until false
    end
end,
yd = function (e, a)
    return function ()
        local _, d, c
        _ = 39
        repeat
            if _ > 39 then
                d = e.c(d(c))
                return e.d(d)
            else
                d = a[1][1][a[1][2]]
                _, d, c = 0x3e, d.GetPivot, d
            end
        until false
    end
end,
ae = function (e, a)
    return function ()
        local _, c, d
        _ = 213
        repeat
            if _ >= 0xd5 then
                d = 0
                c, a[2][1][a[2][2]] = a[1][1][a[1][2]], d
                _, d, c = 75, c["serverHop"], "Manual hop"
            else
                d(c)
                return
            end
        until false
    end
end,
ec = function (e, h)
    return function ()
        local c, i, _, d, a, g, b
        _ = 0x54
        repeat
            if _ > 0x70 then
                if _ > 170 then
                    if _ <= 217 then
                        if _ <= 0xd1 then
                            _, i = 0x6d, h[3][1][h[3][2]]
                            b = i["IsWorldPositionWithinLocalPlotBounds"]
                        else
                            c = c()
                            b = c
                            _ = b and 0x1aa - _ or 0x6d
                        end
                    else
                        c(b, i)
                        _, i = _ + -69, h[1][1][h[1][2]]
                        i, b = d, i["returnToBase"]
                    end
                elseif _ < 0x9e then
                    if _ <= 119 then
                        _, b = 0xd9, h[1][1][h[1][2]]
                        c = b["getRoot"]
                    else
                        _, b, d = 0x7b3c / _, h[1][1][h[1][2]], e:Qe{h[2], h[1]}
                        c, b, i = b["setStatus"], "Returning", "Info"
                    end
                elseif _ > 0x9e then
                    b = b(i)
                    c = not b
                    _ = c and 0xdf - _ or 0x77
                else
                    d = false
                    return d
                end
            elseif _ >= 0x35 then
                if _ > 0x6a then
                    if _ <= 0x6d then
                        _ = b and _ + -84 or 41
                    else
                        _, i = 47, h[1][1][h[1][2]]
                        b, g, a, i = i["waitFor"], e:Re{h[1], h[2]}, 0.15, 4
                    end
                elseif _ >= 0x54 then
                    if _ <= 0x54 then
                        c = h[2][1][h[2][2]]
                        d = not c
                        _ = d and 0x9e or 132
                    else
                        b = true
                        return b
                    end
                else
                    c = false
                    return c
                end
            elseif _ <= 41 then
                if _ < 0x25 then
                    i = h[3][1][h[3][2]]
                    _, b, i = 37, i["IsWorldPositionWithinLocalPlotBounds"], c["Position"]
                elseif _ <= 0x25 then
                    _, b = 41, b(i)
                else
                    _ = b and 0x11f0 / _ or 106
                end
            else
                _ = 0x6a
                b(i, a, g)
            end
        until false
    end
end,
Ab = function (e, h)
    return function ()
        local d, i, c, a, g, _, b
        _ = 0xf6
        repeat
            if _ > 0x99 then
                if _ < 209 then
                    if _ > 0xad then
                        _, a = 209, h[2][1][h[2][2]]
                        g, i, a = true, a["travelTo"], d
                    else
                        return
                    end
                elseif _ < 0xf2 then
                    i = i(a, g)
                    b = not i
                    _ = b and 173 or 8
                elseif _ <= 242 then
                    c = c()
                    b = not c
                    _ = b and 0 or 319 - _
                else
                    c = h[2][1][h[2][2]]
                    _, d = 20, c["getTreadmillStand"]
                end
            elseif _ <= 77 then
                if _ <= 20 then
                    if _ <= 8 then
                        if _ <= 0 then
                            return
                        else
                            _, i = 0x7a - _, h[2][1][h[2][2]]
                            a, b = h[1][1][h[1][2]], i["netInvoke"]
                            i = a["Treadmills"]
                            i = i["REQUEST_EQUIP_STATIC"]
                        end
                    else
                        d = d()
                        c = not d
                        _ = c and 118 or 0x99
                    end
                else
                    a = c["Position"]
                    i = a - d
                    i, b = 12, i["Magnitude"]
                    _ = b > i and 0xc0 or 85 - _
                end
            elseif _ < 118 then
                b(i)
                b = true
                h[3][1][h[3][2]] = b
                return b
            elseif _ <= 118 then
                return
            else
                b = h[2][1][h[2][2]]
                _, c = _ + 0x59, b["getRoot"]
            end
        until false
    end
end,
hc = function (e, a)
    return function ()
        local _, d, c
        _ = 8
        repeat
            if _ >= 90 then
                if _ <= 0x5a then
                    d(c)
                    return
                else
                    return
                end
            elseif _ > 4 then
                c = a[12][1][a[12][2]]
                d = not c
                _ = d and 118 or 4
            else
                _, c, d = 90, e:Se{a[1], a[7], a[3], a[6], a[4], a[10], a[5], a[11], a[8], a[2], a[9]}, e._["pcall"]
            end
        until false
    end
end,
lf = function (e, h)
    return function (d)
        local i, a, _, c, f, j, b, k
        j = 0x52
        while true do
            if j >= 0x63 then
                if j > 170 then
                    i, b = b, b.sub
                    b = e.c(b(i, a, k))
                    return e.d(b)
                elseif j > 0x7a then
                    j = k and 0x16a - j or 0x101 - j
                elseif j <= 99 then
                    j, _ = j + 71, 5
                    f = _ - c
                    f, k = 1, -f
                    k = k - f
                else
                    i, k, a, b = d, e:mf{h[1], h[4], h[3]}, ".....", h[2][1][h[2][2]]
                    b = b(i, a, k)
                    k, a = 0, 1
                    k = c > k
                    j = k and 0xdd - j or j + 0x30
                end
            elseif j >= 82 then
                if j > 0x52 then
                    j, k = 0xc0, -1
                else
                    b, i = #d, 5
                    b, c = 0, b % i
                    j = c > b and 4 or 122
                end
            else
                a, b = 5, "~"
                i, a, b = b, a - c, b.rep
                j, b = 0x7a, b(i, a)
                d = d .. b
            end
        end
    end
end,
Cf = function (a, b, c, d)
    a.Bf[d] = a.if_(b, c)
    return a.Bf[d]
end,
ef = function (e, g)
    return function ()
        local c, d, b, _, f
        _ = 28
        repeat
            if _ <= 48 then
                if _ > 0x1c then
                    b = e.c(b(f))
                    _, c, d = 0x117 - _, d, d.SetValue
                else
                    _, d, b, f = 48, g[2][1][g[2][2]], e._["tostring"], g[1][1][g[1][2]]
                end
            else
                d(c, e.d(b))
                return
            end
        until false
    end
end,
de = function (e, a)
    return function ()
        local d, _, c
        _ = 194
        while true do
            if _ >= 0xc2 then
                _, c = 0x38, a[1][1][a[1][2]]
                d, c = c["runAutoFusePets"], true
            else
                d(c)
                return
            end
        end
    end
end,
Ga = function (e, a)
    return function ()
        local d, c, _, b
        _ = 0x51
        while true do
            if _ >= 94 then
                if _ < 0xca then
                    return
                elseif _ > 202 then
                    b, _, c = e:Ad{a[2], a[1]}, _ + -34, e._["pcall"]
                else
                    _ = 0x5e
                    c(b)
                end
            elseif _ <= 0x51 then
                _, d, c = 89, e._["pcall"], e:zd{a[2], a[1]}
            else
                d = d(c)
                c = not d
                _ = c and 236 or 0x5e
            end
        end
    end
end,
fe = function (e, a)
    return function ()
        local c, _, d
        _ = 60
        repeat
            if _ < 0x9a then
                if _ > 0x3c then
                    return
                else
                    _, d, c = 0xde, e._["typeof"], a[1][1][a[1][2]]
                end
            elseif _ <= 0xc5 then
                if _ <= 0x9a then
                    _, d = 351 - _, a[1][1][a[1][2]]
                    d, c = d.Disconnect, d
                else
                    _ = _ + -0x46
                    d(c)
                end
            else
                d = d(c)
                c = "RBXScriptConnection"
                _ = d == c and 0x9a or 349 - _
            end
        until false
    end
end,
Xc = function (e, a)
    return function ()
        local _, d, c
        _ = 0x52
        while true do
            if _ > 82 then
                d(c)
                return
            else
                d = a[1][1][a[1][2]]
                d, _, c = d.Destroy, 253, d
            end
        end
    end
end,
Wd = function (e, h)
    return function ()
        local _, c, d, b, f
        _ = 0
        repeat
            if _ <= 116 then
                if _ > 0 then
                    d = d(c, b)
                    d = {[2] = 3, [3] = d}
                    d[1] = d
                    b = e._["task"]
                    _, b, c = 216, e:me{h[1], d}, b["spawn"]
                else
                    c = h[2][1][h[2][2]]
                    b, f, d = {}, "Unload?", c["Dialog"]
                    b["Title"] = f
                    f = "Stops automation and closes the menu."
                    _, b["Content"] = 116, f
                    f = true
                    b["Danger"] = f
                    d, c = d.Confirm, d
                end
            else
                c(b)
                return
            end
        until false
    end
end,
xd = function (e, a)
    return function ()
        local d, _, c
        _ = 0x7c
        while true do
            if _ >= 0x77 then
                if _ > 0x7c then
                    _ = d and 295 - _ or 71
                elseif _ > 119 then
                    d = a[1][1][a[1][2]]
                    _ = d and 119 or 207
                else
                    _, d = 0x57, a[1][1][a[1][2]]
                    c, d = d, d.GetPivot
                end
            elseif _ >= 0x57 then
                if _ > 87 then
                    return d
                else
                    _, d = _ + 0x78, d(c)
                end
            else
                _, d = 0x9f - _, nil
            end
        end
    end
end,
Cd = function (e, a)
    return function ()
        local _, d, c
        _ = 0xc2
        while true do
            if _ > 183 then
                if _ < 231 then
                    if _ <= 194 then
                        _, c = 231, a[2][1][a[2][2]]
                        d = c["stealingEnabled"]
                    else
                        _ = 97
                        d(c)
                    end
                elseif _ <= 0xe7 then
                    d = d()
                    _ = d and 180 or 179
                else
                    _ = 179
                    d()
                end
            elseif _ <= 0xb3 then
                if _ > 151 then
                    c = a[2][1][a[2][2]]
                    d, _, c = c["isOn"], 151, "NoClip"
                elseif _ > 0x61 then
                    d = d(c)
                    _ = d and 0x6bf1 / _ or _ + -0x36
                else
                    return
                end
            elseif _ <= 180 then
                c = a[2][1][a[2][2]]
                _, d = 425 - _, c["swapStealHumanoid"]
            else
                d, _, c = a[1][1][a[1][2]], 208, true
            end
        end
    end
end,
ad = function (e, g)
    return function ()
        local b, c, d
        b, c = true, g[1][1][g[1][2]]
        d = c ~= b
        return d
    end
end,
m = function (e, h)
    return function ()
        local d, b, c, f, _
        _ = 8
        while true do
            if _ < 202 then
                if _ < 0xb1 then
                    if _ <= 8 then
                        _, c = 202, h[1][1][h[1][2]]
                        d = c["getSave"]
                    else
                        _, c = 0x4fc9 / _, d["EggInventory"]
                    end
                elseif _ <= 0xb1 then
                    b = 0
                    return b
                else
                    b = e.c(b(f))
                    return e.d(b)
                end
            elseif _ >= 0xd7 then
                if _ > 0xd7 then
                    f = h[1][1][h[1][2]]
                    b, _, f = f["countTable"], 0xbe, c
                else
                    _, b, f = 0xcb, e._["typeof"], c
                end
            elseif _ > 202 then
                b = b(f)
                f = "table"
                _ = b ~= f and _ + -0x1a or 0xeb
            else
                d = d()
                c = d
                _ = c and 95 or _ + 13
            end
        end
    end
end,
Qa = function (e, a)
    return function ()
        local d, c, _
        _ = 165
        while true do
            if _ > 0xa5 then
                d = d(c)
                _ = d and 0x46 or _ + -145
            elseif _ >= 70 then
                if _ > 0x46 then
                    _, c = 0xb2, a[2][1][a[2][2]]
                    d, c = c["isOn"], "AutoTreadmill"
                else
                    _, c = _ + -37, a[1][1][a[1][2]]
                    d = not c
                end
            else
                return d
            end
        end
    end
end,
Q = function (e, h)
    return function ()
        local _, d, b, c, f
        _ = 0xba
        while true do
            if _ < 184 then
                if _ <= 68 then
                    d, c = d(c)
                    b = d
                    _ = b and 123 or 0xb8
                else
                    _, f = 0xb8, true
                    b = c == f
                end
            elseif _ > 0xb8 then
                c, _, d = e:jd{h[1]}, 68, e._["pcall"]
            else
                return b
            end
        end
    end
end,
re = function (e, a)
    return function (...)
        local c, d, _, b
        _ = 8
        while true do
            if _ > 8 then
                d(c, e.d(b))
                return
            else
                d, b = a[1][1][a[1][2]], e.c(...)
                d, _, c = d.FireServer, 0x7d, d
            end
        end
    end
end,
sd = function (e, a)
    return function ()
        local c, d
        d, c = a[1][1][a[1][2]], false
        d["Anchored"] = c
        return
    end
end,
af = function (e, g)
    return function ()
        local c, _, b, d
        _ = 0xdb
        while true do
            if _ > 0xca then
                if _ <= 0xdb then
                    b, c = true, g[2][1][g[2][2]]
                    d = c == b
                    _ = d and 0xc0 or 0x8d
                else
                    c = g[3][1][g[3][2]]
                    _, d = 444 - _, not c
                end
            elseif _ >= 192 then
                if _ <= 192 then
                    _ = d and 242 or 202
                else
                    return d
                end
            elseif _ <= 106 then
                _, d = 192, d()
            else
                _, c = 0x3a62 / _, g[1][1][g[1][2]]
                d = c["placingEnabled"]
            end
        end
    end
end,
d = (function ()
    local function m(i, j, k)
        if j > k then
            return
        end
        return i[j], m(i, j + 1, k)
    end
    return function (o)
        return m(o[1], 1, o[2])
    end
end)(),
xc = function (s, h)
    return function (d)
        local u, f, e, l, g, n, j, a, b, r, v, _, c, w, t, k, q, p, i
        j = 121
        repeat
            if j >= 0x8d then
                if j > 0xcb then
                    if j <= 0xe4 then
                        if j >= 0xd7 then
                            if j <= 226 then
                                if j > 217 then
                                    i = i()
                                    t = not i
                                    j = t and 0x4b0a / j or 0x2f
                                elseif j > 215 then
                                    i = i + k
                                    j = k > 0 and 0x42 or 0x676a / j
                                else
                                    j = t and 0xc3 or 0x184 - j
                                end
                            else
                                j, n = 425 - j, h[1][1][h[1][2]]
                                w = n["RequestPlaceEgg"]
                                c = not w
                            end
                        elseif j <= 208 then
                            if j <= 0xce then
                                j = 120
                                a(p)
                                p, f, a = s._["ipairs"], w, false
                            else
                                j, i = 0xed - j, s._["task"]
                                i, t = 0.15, i["wait"]
                            end
                        else
                            j = i > g and 117 or 157
                        end
                    elseif j >= 0xf7 then
                        if j > 0xfb then
                            r, l = p(f, _)
                            _ = r
                            j = _ == nil and 0x2e or 0x68
                        elseif j > 0xf7 then
                            return a
                        else
                            i()
                            return a
                        end
                    elseif j < 244 then
                        j = 0xd0
                        t(i, g)
                    elseif j <= 0xf4 then
                        j = n and j + -0xf2 or j + -152
                    else
                        j = i < g and 117 or 0xcb
                    end
                elseif j >= 0xb6 then
                    if j < 194 then
                        if j <= 0xb7 then
                            if j > 0xb6 then
                                w = w()
                                p, a = 0, #w
                                n = a == p
                                j = n and 0x1ab - j or 0x427b / j
                            else
                                b = 1
                                j, e = 192, u[1][u[2]] + b
                                h[6][1][h[6][2]], t = e, true
                                a, b = t, s._["task"]
                                e, b = b["wait"], 0.25
                            end
                        else
                            j = 117
                            e(b)
                        end
                    elseif j > 197 then
                        j = k ~= k and j + -0x56 or 0x22e4 / j
                    elseif j <= 0xc3 then
                        if j > 0xc2 then
                            return a
                        else
                            n = n()
                            n = {[2] = 3, [3] = n}
                            n[1] = n
                            a, p = #n[1][n[2]], 0
                            j = a == p and 71 or 14
                        end
                    else
                        j = c and 151 or 0x7c
                    end
                elseif j < 155 then
                    if j <= 0x96 then
                        if j > 141 then
                            j, t, g = 0x17f - j, s._["pcall"], h[1][1][h[1][2]]
                            i, g = g["RequestEquipTool"], l[1][l[2]]
                        else
                            j, i = j + 112, 0
                            h[4][1][h[4][2]] = i
                        end
                    else
                        return
                    end
                elseif j <= 0xad then
                    if j >= 0x9d then
                        if j <= 0x9d then
                            j = k ~= k and 0x5405 / j or 59
                        else
                            g = h[5][1][h[5][2]]
                            j, i = j + 0x35, g["isNearPlot"]
                        end
                    else
                        j, i = 215, i()
                        t = not i
                    end
                else
                    i = i(g)
                    j, t = 47, not i
                end
            elseif j > 90 then
                if j > 120 then
                    if j > 0x7c then
                        if j <= 135 then
                            j, i = 0x51bd / j, c
                        else
                            j = i < g and 117 or 44
                        end
                    elseif j < 122 then
                        d = {[2] = 3, [3] = d}
                        d[1] = d
                        c = h[2][1][h[2][2]]
                        j = c and 0xc5 or 0xe4
                    elseif j <= 122 then
                        j = k <= 0 and j + 123 or 0xcb
                    else
                        j, c, n = 0x58a4 / j, s:af{h[5], d, h[2]}, h[5][1][h[5][2]]
                        w = n["getUnplacedEggUids"]
                    end
                elseif j > 98 then
                    if j >= 117 then
                        if j > 0x75 then
                            p, f, _ = p(f)
                            p, f, _ = s.b(p, f, _)
                            r, l = p(f, _)
                            _ = r
                            j = _ == nil and j + -0x4a or 104
                        else
                            i = not t
                            j = i and 1 or 258 - j
                        end
                    else
                        l = {[2] = 3, [3] = l}
                        l[1] = l
                        i = h[3][1][h[3][2]]
                        t = not i
                        j = t and 0xd7 or 0x87
                    end
                elseif j <= 0x5e then
                    if j >= 0x5d then
                        if j <= 0x5d then
                            j, p = 0x239a / j, h[5][1][h[5][2]]
                            a, p = p["ensureAtPlot"], c
                        else
                            j = 217
                        end
                    else
                        a = h[5][1][h[5][2]]
                        j, n = 0xc2, a["getPlacementLocalCFrames"]
                    end
                else
                    j, a = 342 - j, a(p)
                    n = not a
                end
            elseif j < 47 then
                if j > 29 then
                    if j <= 44 then
                        if j > 42 then
                            j, q = j + -2, h[6][1][h[6][2]]
                            q, b = 1, q + i
                            e, b = b - q, #n[1][n[2]]
                            v, e = e % b, q
                            u = v + e
                            u = {[2] = 3, [3] = u}
                            u[1] = u
                            v = false
                            v = {[2] = 3, [3] = v}
                            v[1] = v
                            e, b = s._["pcall"], s:bf{h[1], v, n, u, l}
                        else
                            e(b)
                            j = v[1][v[2]] and 0xb6 or 94
                        end
                    else
                        return a
                    end
                elseif j >= 14 then
                    if j > 14 then
                        t(i)
                        t, v, u, i = false, 1, #n[1][n[2]], 0
                        k, g = v, u - v
                        j = g ~= g and 117 or 90
                    else
                        j, p = 206, h[5][1][h[5][2]]
                        p, a = "Auto Place Egg", p["setJob"]
                    end
                elseif j <= 1 then
                    j, g = 0xf7, h[5][1][h[5][2]]
                    i = g["markPlotFull"]
                else
                    return
                end
            elseif j > 0x42 then
                if j >= 0x55 then
                    if j > 0x55 then
                        j = k > 0 and 0xd5 or 0x9d
                    else
                        j, g = 179, h[5][1][h[5][2]]
                        g, i = c, g["ensureAtPlot"]
                    end
                else
                    return
                end
            elseif j <= 59 then
                if j <= 57 then
                    if j <= 47 then
                        j = t and 0x2e15 / j or 0xa77 / j
                    else
                        i = h[1][1][h[1][2]]
                        t = i["RequestEquipTool"]
                        j = t and 150 or 0xd0
                    end
                else
                    j = k <= 0 and 0x1f93 / j or 44
                end
            else
                j = i > g and j + 51 or 0xbc - j
            end
        until false
    end
end,
Td = function (e, a)
    return function ()
        local _, c, d
        _ = 88
        repeat
            if _ <= 0x58 then
                c = e._["task"]
                c, _, d = e:le{a[1]}, 0xff, c["spawn"]
            else
                d(c)
                return
            end
        until false
    end
end,
w = function (e, h)
    return function (d, c)
        local i, g, j, a, b, f
        j = 222
        while true do
            if j > 0x82 then
                if j >= 0xc9 then
                    if j > 222 then
                        if j <= 238 then
                            i = i(a)
                            a = "table"
                            b = i ~= a
                            j = b and 31 or 178
                        else
                            b = false
                            return b
                        end
                    elseif j <= 217 then
                        if j < 210 then
                            b = true
                            return b
                        elseif j <= 210 then
                            b = e.c(b(i, a, g, f))
                            return e.d(b)
                        else
                            j = b and 0xc9 or 0x99
                        end
                    else
                        a, j, i = d, 238, e._["typeof"]
                    end
                elseif j >= 0x9a then
                    if j > 178 then
                        i, a = d["State"], "Dropped"
                        j, b = 0x21, i ~= a
                    elseif j <= 154 then
                        a, i = "Slot", d["State"]
                        b = i ~= a
                        j = b and 0x7850 / j or 33
                    else
                        j, a, i = j + -35, d["Uid"], e._["typeof"]
                    end
                elseif j > 143 then
                    j, a = 0x48ea / j, h[1][1][h[1][2]]
                    a, i = "AutoStealSelected", a["isOn"]
                else
                    j, i = 0x1151 / j, i(a)
                    a = "string"
                    b = i ~= a
                end
            elseif j < 0x43 then
                if j > 0x1c then
                    if j > 0x1f then
                        j = b and j + 0x39 or 0xa3 - j
                    else
                        j = b and 0x81d / j or 0x12a6 / j
                    end
                elseif j > 26 then
                    j, i = j + -12, h[1][1][h[1][2]]
                    a, i, b = d["AreaId"], "StealZones", i["selectionAllows"]
                elseif j > 0x16 then
                    b = b(i)
                    j = b and j + 2 or 0xd9
                elseif j > 16 then
                    b = true
                    return b
                else
                    j, b = 0xe9 - j, b(i, a)
                end
            elseif j > 90 then
                if j <= 122 then
                    i = i(a)
                    b = not i
                    j = b and 363 - j or j + -49
                else
                    j = c and 0x16 or 81
                end
            elseif j >= 81 then
                if j <= 81 then
                    j, i = 0x1a, h[1][1][h[1][2]]
                    i, b = d, i["isBigEgg"]
                else
                    b = false
                    return b
                end
            elseif j > 67 then
                j, i = j + 0x89, h[1][1][h[1][2]]
                i, f, b, a, g = d, "StealMutations", i["matchesEggFilters"], "StealZones", "StealRarities"
            else
                b = false
                return b
            end
        end
    end
end,
fa = function (e, g)
    return function ()
        local _, c, d, f, b
        _ = 0xc3
        while true do
            if _ <= 91 then
                if _ > 67 then
                    _ = d and 0x43 or 140
                elseif _ < 0x17 then
                    d(c, b, f)
                    _, c = 23, g[1][1][g[1][2]]
                    d, b = c["Theme"], "Light"
                    f, c, d = b, d, d.RememberPolarity
                elseif _ > 0x17 then
                    _, c = 13, g[1][1][g[1][2]]
                    f, d, b = "Ember", c["Theme"], "Dark"
                    d, c = d.RememberPolarity, d
                else
                    _ = _ + 0x75
                    d(c, b, f)
                end
            elseif _ >= 173 then
                if _ > 0xad then
                    c = g[1][1][g[1][2]]
                    d = c["Theme"]
                    _ = d and 173 or 91
                else
                    b = g[1][1][g[1][2]]
                    _, c = 0x3d7f / _, b["Theme"]
                    d = c["RememberPolarity"]
                end
            else
                return
            end
        end
    end
end,
_c = function (s, h)
    return function (d, c)
        local k, j, _, o, g, i, v, t, b, r, z, m, n, a, A, f, l, e, y, q, x, u, p, w
        j = 90
        repeat
            if j < 0x7b then
                if j > 70 then
                    if j >= 0x63 then
                        if j < 108 then
                            if j <= 105 then
                                if j > 0x67 then
                                    j, u = j + -105, u(p, w)
                                    a["CFrame"] = u
                                elseif j > 99 then
                                    j, l = 91, h[5][1][h[5][2]]
                                    r = l["getRoot"]
                                else
                                    m = m(u, p, w)
                                    u, p = m["Magnitude"], 0.001
                                    j = u > p and j + 0x62 or 107
                                end
                            else
                                p = s._["CFrame"]
                                p, j, u = x, 362 - j, p["new"]
                            end
                        elseif j < 115 then
                            if j <= 0x6c then
                                j, n = j + -24, n(a, z)
                            else
                                i, g = r(l, t)
                                t = i
                                j = t == nil and j + -8 or 0x142 - j
                            end
                        elseif j > 0x73 then
                            z = false
                            return z
                        else
                            y = h[5][1][h[5][2]]
                            e, y, j, v, k = a["Position"], g.X, 59, g.Z, y["groundedY"]
                            e = e.Y
                        end
                    elseif j < 0x54 then
                        if j >= 80 then
                            if j <= 0x50 then
                                j = v and 253 - j or 0x1180 / j
                            else
                                q = q(o, x, m)
                                j, x = 158, s._["math"]
                                o, u = x["min"], h[5][1][h[5][2]]
                                m = u["stealSpeed"]
                            end
                        else
                            v = h[2][1][h[2][2]]
                            j = v and 238 or j + 37
                        end
                    elseif j >= 91 then
                        if j <= 0x5b then
                            r = r()
                            a = r
                            r = not a
                            j = r and 0x138d / j or 0x159 - j
                        else
                            l, r = f, {}
                            r[1] = l
                            j, _ = 170, r
                        end
                    elseif j <= 0x54 then
                        j, z = 0x3c60 / j, h[5][1][h[5][2]]
                        a = z["getRoot"]
                    else
                        j, a, n = 0xe5, d, s._["typeof"]
                    end
                elseif j > 34 then
                    if j < 56 then
                        if j <= 0x2a then
                            if j <= 41 then
                                j, n = j + 153, h[2][1][h[2][2]]
                                A = not n
                            else
                                j, n, z, a = 0x6c, A.FindFirstChildOfClass, "Humanoid", A
                            end
                        else
                            r = false
                            return r
                        end
                    elseif j <= 69 then
                        if j <= 0x3b then
                            if j > 56 then
                                j, k = 0x9f, k(y, v, e)
                                v = s._["Vector3"]
                                v, b, e, y = g.X, g.Z, k, v["new"]
                            else
                                e = h[5][1][h[5][2]]
                                j, v = 0xd2, e["getRoot"]
                            end
                        else
                            _ = true
                            return _
                        end
                    else
                        j = z and 0x75 or 0xdf - j
                    end
                elseif j < 26 then
                    if j < 19 then
                        if j <= 0 then
                            p = s._["Vector3"]
                            u = p["zero"]
                            a["AssemblyLinearVelocity"] = u
                            u = p["zero"]
                            j, a["AssemblyAngularVelocity"] = 0x4a, u
                        else
                            y = h[5][1][h[5][2]]
                            j, k = 0xe2, y["getRoot"]
                        end
                    elseif j > 19 then
                        e = a["Position"]
                        v = y - e
                        q, e = h[3][1][h[3][2]], v["Magnitude"]
                        b = q["ArriveDistance"]
                        j = e <= b and 0x6f or 196
                    else
                        j, e = 0xb5, c
                    end
                elseif j <= 30 then
                    if j > 0x1b then
                        r = r(l)
                        a["CFrame"] = r
                        l = s._["Vector3"]
                        r = l["zero"]
                        a["AssemblyLinearVelocity"] = r
                        j, r = 141, l["zero"]
                        a["AssemblyAngularVelocity"] = r
                        i = a["Position"]
                        t = i - f
                        l, i = t["Magnitude"], s._["math"]
                        k, t, i = h[3][1][h[3][2]], i["max"], 3
                        g, k = k["ArriveDistance"], 1
                        g = g + k
                    elseif j <= 0x1a then
                        j, y = 176 - j, c
                    else
                        n = h[1][1][h[1][2]]
                        A = n["Character"]
                        n = A
                        j = n and 0x46e / j or 0x54
                    end
                elseif j > 31 then
                    j, z = 0x85, z(f, _, r)
                    _ = s._["Vector3"]
                    f, r, _, l = _["new"], z, d.X, d.Z
                else
                    k = false
                    return k
                end
            elseif j <= 0xc4 then
                if j < 0x9e then
                    if j >= 0x87 then
                        if j >= 150 then
                            if j > 150 then
                                z = false
                                n["Sit"] = z
                                j, n["PlatformStand"] = j + -24, z
                                z = true
                                n["AutoRotate"] = z
                                f = h[5][1][h[5][2]]
                                z = f["stealSpeed"]
                            else
                                y = y()
                                j, k = 0xf2, not y
                            end
                        elseif j > 0x87 then
                            t = t(i, g)
                            r = l <= t
                            return r
                        else
                            j, r = 233, h[5][1][h[5][2]]
                            r, _, l = a["Position"], r["buildStealPath"], f
                        end
                    elseif j >= 0x83 then
                        if j <= 131 then
                            j, z = 70, not a
                        else
                            f = f(_, r, l)
                            l = a["Position"]
                            r = l - f
                            _, l = r["Magnitude"], h[3][1][h[3][2]]
                            r = l["ArriveDistance"]
                            j = _ <= r and 69 or 135
                        end
                    elseif j <= 123 then
                        r, l, t = r(l)
                        r, l, t = s.b(r, l, t)
                        i, g = r(l, t)
                        t = i
                        j = t == nil and j + -20 or 0xd3
                    else
                        z = z()
                        n["WalkSpeed"] = z
                        z, r, _, f = f["groundedY"], a["Position"], d.Z, d.X
                        j, r = 34, r.Y
                    end
                elseif j > 0xad then
                    if j >= 194 then
                        if j <= 0xc2 then
                            j = A and 253 or 0x1476 / j
                        else
                            j, b, o = j + -0x1c, v["Unit"], s._["math"]
                            q, x = o["clamp"], h[4][1][h[4][2]]
                            o = x["Heartbeat"]
                            x, o = o, o.Wait
                        end
                    elseif j <= 0xb5 then
                        j, e = 0x50, e()
                        v = not e
                    else
                        a = a()
                        z = not n
                        j = z and 0x3250 / j or j + -53
                    end
                elseif j <= 168 then
                    if j >= 159 then
                        if j > 159 then
                            j, o = 0x3678 / j, o(x)
                            x, m = 0, 0.03333333333333333
                        else
                            j, y = 0xe9 - j, y(v, e, b)
                        end
                    else
                        m = m()
                        j, x, m = 365 - j, m * q, e
                    end
                elseif j <= 0xaa then
                    l, j, r = _, 123, s._["ipairs"]
                else
                    v = false
                    return v
                end
            elseif j > 0xe9 then
                if j > 0xfb then
                    if j > 254 then
                        u = u(p)
                        j, a["CFrame"] = 0, u
                    elseif j > 253 then
                        l = s._["CFrame"]
                        j, l, r = 0x1dc4 / j, f, l["new"]
                    else
                        A = false
                        return A
                    end
                elseif j < 247 then
                    if j <= 0xee then
                        v = c
                        j = v and 19 or 80
                    else
                        j = k and 0x1f or 6
                    end
                elseif j <= 247 then
                    k = false
                    return k
                else
                    v = false
                    return v
                end
            elseif j <= 224 then
                if j < 210 then
                    if j > 0xc5 then
                        o = o(x, m)
                        m, u = a["Position"], b * o
                        j, u, x = 0x63, s._["Vector3"], m + u
                        u, p, w, m = b.X, 0, b.Z, u["new"]
                    else
                        p = s._["CFrame"]
                        p, u, w = x, p["lookAt"], m["Unit"]
                        j, w = 105, x + w
                    end
                elseif j > 211 then
                    k = c
                    j = k and 0xfa - j or j + 18
                elseif j <= 0xd2 then
                    v = v()
                    a = v
                    v = not a
                    j = v and 461 - j or 0x12de / j
                else
                    y = h[2][1][h[2][2]]
                    k = not y
                    j = k and 453 - j or 224
                end
            elseif j <= 0xe5 then
                if j > 226 then
                    n = n(a)
                    a = "Vector3"
                    A = n ~= a
                    j = A and 194 or 0x10e - j
                else
                    k = k()
                    a = k
                    k = not a
                    j = k and j + 0x15 or 0x73
                end
            else
                _ = _(r, l)
                l, r = 0, #_
                j = r == l and 0x5849 / j or 0x9aba / j
            end
        until false
    end
end,
xe = function (e, h)
    return function ()
        local _, b, i, g, c, a, d
        _ = 6
        while true do
            if _ > 6 then
                c = c(b, i, a, g)
                b = true
                d = c == b
                h[2][1][h[2][2]] = d
                return
            else
                _, b = 0x3f, h[1][1][h[1][2]]
                c, a, g, b, i = b["CanSelectPet"], h[4][1][h[4][2]], false, h[5][1][h[5][2]], h[3][1][h[3][2]]
            end
        end
    end
end,
Dd = function (e, a)
    return function ()
        local c, _, b, d
        _ = 0xc7
        repeat
            if _ >= 199 then
                d, b = a[2][1][a[2][2]], a[1][1][a[1][2]]
                _, c, d = 195, d, d.JSONDecode
            else
                d = e.c(d(c, b))
                return e.d(d)
            end
        until false
    end
end,
yb = function (e, h)
    return function (d)
        local _, c, i, b, a
        _ = 0x86
        repeat
            if _ < 156 then
                if _ < 0x86 then
                    i = i(a)
                    _ = i and 0x90 or 0xdc - _
                elseif _ <= 0x86 then
                    b, a = h[2][1][h[2][2]], h[1][1][h[1][2]]
                    a, _, i = d["AssetCategory"], 0x40, a["resolveRarity"]
                else
                    c = b[i]
                    _ = c and 0xb5 or 0x83a0 / _
                end
            elseif _ <= 0xb5 then
                if _ > 156 then
                    return c
                else
                    _, i = 300 - _, "Common"
                end
            else
                _, c = 0xb5, 0
            end
        until false
    end
end,
Ld = function (e, a)
    return function ()
        local d, _, c
        _ = 0x28
        repeat
            if _ > 0x28 then
                d(c)
                return
            else
                c = e._["task"]
                _, d, c = 0x4e, c["spawn"], e:ce{a[1]}
            end
        until false
    end
end,
pc = function (e)
    return function (d)
        local i, a, b, j, f, c
        j = 0x35
        while true do
            if j <= 0x4e then
                if j > 53 then
                    if j > 0x3f then
                        c = c(b)
                        b = "table"
                        j = c ~= b and 63 or 84
                    else
                        return
                    end
                elseif j < 49 then
                    return
                elseif j <= 0x31 then
                    c, b, i = c(b)
                    c, b, i = e.b(c, b, i)
                    a = c(b, i)
                    i = a
                    j = i == nil and 32 or j + 0x94
                else
                    j, c, b = 0x4e, e._["type"], d
                end
            elseif j <= 120 then
                if j <= 84 then
                    b, j, c = d, 49, e._["pairs"]
                else
                    a = c(b, i)
                    i = a
                    j = i == nil and 0x20 or 0x5c58 / j
                end
            else
                j, f = j + -0x4d, nil
                d[a] = f
            end
        end
    end
end,
oa = function (e, h)
    return function (d)
        local c, i, j, f, k, g, _, a, b
        j = 0xf7
        while true do
            if j < 141 then
                if j >= 61 then
                    if j <= 74 then
                        if j <= 0x3d then
                            j = f and 197 or 141
                        else
                            j, g, f, _ = 110 - j, "RemoteEvent", k.IsA, k
                        end
                    else
                        a, k = c(b, i)
                        i = a
                        j = i == nil and 279 - j or j + -0x3f
                    end
                elseif j < 0x1e then
                    j, f = 0x3d, f(_, g)
                elseif j <= 30 then
                    c, b, i = c(e.d(b))
                    c, b, i = e.b(c, b, i)
                    a, k = c(b, i)
                    i = a
                    j = i == nil and j + 112 or 0x8ac / j
                else
                    f = f(_, g)
                    j = f and j + 0x19 or 179
                end
            elseif j <= 179 then
                if j > 154 then
                    f, j, g, _ = k.IsA, 0x1b, "RemoteFunction", k
                elseif j < 142 then
                    j = f and 0x68a6 / j or 137
                elseif j > 142 then
                    j, b = 30, e.c(b(i))
                else
                    c = nil
                    return c
                end
            elseif j <= 0xc5 then
                if j <= 190 then
                    return k
                else
                    _ = k["Name"]
                    j, f = 141, _ == d
                end
            else
                c, b = e._["ipairs"], h[1][1][h[1][2]]
                b, j, i = b.GetDescendants, 0x9a, b
            end
        end
    end
end,
Pc = function (e, g)
    return function ()
        local d, _, b, c
        _ = 0x38
        repeat
            if _ >= 112 then
                if _ < 155 then
                    if _ < 117 then
                        c = d["Position"]
                        return c
                    elseif _ <= 117 then
                        c = g[1][1][g[1][2]]
                        _, d = 0x5577 / _, c["GetRespawnPointCFrame"]
                    else
                        b = g[1][1][g[1][2]]
                        c = b["GetPlotData"]
                        d = not c
                        _ = d and 212 or 155
                    end
                elseif _ >= 212 then
                    if _ > 0xd4 then
                        b = d["CenterPoint"]
                        c = b["Position"]
                        return c
                    else
                        d = nil
                        return d
                    end
                elseif _ > 155 then
                    d = d()
                    _ = d and 112 or 0x7c
                else
                    _, c = 0x1f, g[1][1][g[1][2]]
                    d = c["GetPlotData"]
                end
            elseif _ < 0x20 then
                if _ >= 16 then
                    if _ > 0x10 then
                        d = d()
                        c = not d
                        _ = c and _ + 53 or _ + -15
                    else
                        c = d["CenterPoint"]
                        _ = c and 215 or 32
                    end
                else
                    c = nil
                    return c
                end
            elseif _ > 56 then
                c = nil
                return c
            elseif _ < 0x26 then
                c = d["PetArea"]
                _ = c and 38 or 224 / _
            elseif _ <= 38 then
                b = d["PetArea"]
                c = b["Position"]
                return c
            else
                c = g[1][1][g[1][2]]
                d = c["GetRespawnPointCFrame"]
                _ = d and 0x75 or 0x7c
            end
        until false
    end
end,
x = function (e, h)
    return function (d)
        local f, n, a, l, g, i, c, o, m, p, _, b, j, k
        j = 0x2e
        repeat
            if j > 155 then
                if j > 202 then
                    if j <= 0xe7 then
                        if j <= 224 then
                            if j <= 221 then
                                if j <= 0xd0 then
                                    g, l, b, f = h[1][1][h[1][2]], a["Unit"], e._["tonumber"], c["CFrame"]
                                    i, g, j, k = g["optionValue"], "FlySpeed", 0xb6d0 / j, 60
                                else
                                    j, a = 417 - j, not n
                                end
                            else
                                j, c = 93, c()
                                n = m
                                m = n["getHumanoid"]
                            end
                        elseif j > 0xe1 then
                            p = p(f, _, o)
                            j, a = j + -0x6b, a + p
                        else
                            j, i = 14, e.c(i(g, k))
                        end
                    elseif j >= 242 then
                        if j <= 242 then
                            j = a and 196 or 221
                        else
                            j, a = 0xeb62 / j, not m
                        end
                    elseif j <= 0xea then
                        a = true
                        j, m["PlatformStand"] = 103, a
                        p = e._["Vector3"]
                        o, p, a = e._["Enum"], h[3][1][h[3][2]], p["zero"]
                        _ = o["KeyCode"]
                        p, f, _ = p.IsKeyDown, p, _.W
                    else
                        o, p = e._["Enum"], h[3][1][h[3][2]]
                        _ = o["KeyCode"]
                        f, j, _, p = p, 68, _.D, p.IsKeyDown
                    end
                elseif j < 182 then
                    if j <= 173 then
                        if j < 164 then
                            f = e._["Vector3"]
                            p, _, f = f["new"], 1, 0
                            j, o = 0xe7, f
                        elseif j > 164 then
                            f = n["CFrame"]
                            p = f["LookVector"]
                            j, a = 0xcd7 / j, a - p
                        else
                            p = p(f, _)
                            j = p and 0xad or j + -145
                        end
                    elseif j <= 178 then
                        j, p, o = 0x169 - j, h[3][1][h[3][2]], e._["Enum"]
                        _ = o["KeyCode"]
                        _, f, p = _["Space"], p, p.IsKeyDown
                    else
                        p = p(f, _, o)
                        j, a = 0x1a, a - p
                    end
                elseif j >= 191 then
                    if j >= 196 then
                        if j <= 196 then
                            j = a and 77 or 0xea
                        else
                            return
                        end
                    else
                        p = p(f, _)
                        j = p and 13 or 0x1366 / j
                    end
                elseif j > 0xb6 then
                    p = p(f, _)
                    j = p and j + -25 or 0x7c
                else
                    j, b = 0x3774 / j, 60
                end
            elseif j >= 55 then
                if j < 93 then
                    if j <= 0x4d then
                        if j < 68 then
                            j, m = 0x9b, m(n)
                            c = not m
                        elseif j > 0x44 then
                            return
                        else
                            p = p(f, _)
                            j = p and 0x12 or 0x2f48 / j
                        end
                    elseif j > 0x4e then
                        f = n["CFrame"]
                        p = f["RightVector"]
                        j, a = 235, a - p
                    else
                        j, o = 202, l * b
                        _ = o * d
                        p = f + _
                        c["CFrame"] = p
                    end
                elseif j <= 120 then
                    if j > 0x6a then
                        p = p(f, _)
                        j = p and 0x2760 / j or 0xeb
                    elseif j <= 103 then
                        if j <= 0x5d then
                            m = m()
                            a = h[4][1][h[4][2]]
                            n, a = a["CurrentCamera"], not c
                            j = a and 242 or 249
                        else
                            p = p(f, _)
                            j = p and 0x77 - j or 147 - j
                        end
                    else
                        return
                    end
                elseif j > 124 then
                    j = c and 0x6a or 24
                else
                    o, p = e._["Enum"], h[3][1][h[3][2]]
                    j, _ = 0x13b - j, o["KeyCode"]
                    f, p, _ = p, p.IsKeyDown, _["LeftControl"]
                end
            elseif j > 20 then
                if j > 44 then
                    m = h[2][1][h[2][2]]
                    c = not m
                    j = c and 0x9b or 20
                elseif j >= 26 then
                    if j <= 0x1a then
                        f = e._["Vector3"]
                        p = f["zero"]
                        c["AssemblyLinearVelocity"] = p
                        f, p = 0, a["Magnitude"]
                        j = p > f and j + 182 or 202
                    else
                        j, p, o = 0x1c30 / j, h[3][1][h[3][2]], e._["Enum"]
                        _ = o["KeyCode"]
                        p, _, f = p.IsKeyDown, _.S, p
                    end
                else
                    m = h[1][1][h[1][2]]
                    j, c = 224, m["getRoot"]
                end
            elseif j <= 18 then
                if j < 0x10 then
                    if j > 13 then
                        b = b(e.d(i))
                        j = b and 0x5c - j or 0xc4 - j
                    else
                        j, f = 0x917 / j, e._["Vector3"]
                        _, f, p = 1, 0, f["new"]
                        o = f
                    end
                elseif j > 0x10 then
                    f = n["CFrame"]
                    p = f["RightVector"]
                    j, a = 178, a + p
                else
                    f = n["CFrame"]
                    p = f["LookVector"]
                    j, a = 0x2c, a + p
                end
            elseif j > 0x13 then
                n = h[1][1][h[1][2]]
                j, n, m = 55, "Fly", n["isOn"]
            else
                p, o = h[3][1][h[3][2]], e._["Enum"]
                j, _ = 120, o["KeyCode"]
                p, f, _ = p.IsKeyDown, p, _.A
            end
        until false
    end
end,
Tb = function (e, h)
    return function ()
        local o, j, d, a, b, k, n, c, l, _, f, m
        j = 0xd6
        repeat
            if j < 166 then
                if j <= 60 then
                    if j < 0x19 then
                        if j <= 18 then
                            if j > 1 then
                                m(n, e.d(a))
                                n = e._["table"]
                                n, k, m = c, h[2][1][h[2][2]], n["insert"]
                                k, f, a, l = "Speed Power", "`", k["embedField"], h[2][1][h[2][2]]
                                l, j, o = d["SpeedPower"], 0x3c, l["formatNumber"]
                            else
                                j, a = 230, e.c(a(k, f, _))
                            end
                        else
                            d = d()
                            m = {}
                            c = m
                            j = d and 0xd3 or 0xa6
                        end
                    elseif j >= 52 then
                        if j <= 0x34 then
                            m(n, e.d(a))
                            n = e._["table"]
                            k, n, m = h[2][1][h[2][2]], c, n["insert"]
                            f, a, o, b, k = "`", k["embedField"], e._["tostring"], h[2][1][h[2][2]], "Pets Owned"
                            j, l, b = 135, b["countTable"], d["Inventory"]
                        else
                            j, o = 0xae, o(l)
                            l = "`"
                            _ = o .. l
                            f = f .. _
                        end
                    elseif j > 0x19 then
                        j = 166
                        m(n, e.d(a))
                    else
                        j, a = 0x31, e.c(a(k, f))
                    end
                elseif j <= 0x71 then
                    if j > 0x6f then
                        j, a = 131 - j, e.c(a(k, f))
                    elseif j > 89 then
                        a = a(k)
                        n["timestamp"] = a
                        m = n
                        return m
                    elseif j <= 0x4a then
                        j, o = 99 - j, o(e.d(l))
                        l = "`"
                        _ = o .. l
                        f = f .. _
                    else
                        a = a(k, f, _, e.d(o))
                        n["description"] = a
                        j, a = 0x6f, 0x5865f2
                        n["color"] = a
                        n["fields"] = c
                        f, k = "MMB HUB", {}
                        k["text"] = f
                        a = k
                        n["footer"] = a
                        k = e._["os"]
                        k, a = "!%Y-%m-%dT%H:%M:%SZ", k["date"]
                    end
                elseif j <= 122 then
                    j, o = 0x59, e.c(o(l))
                else
                    j, l = 0xd1 - j, e.c(l(b))
                end
            elseif j <= 183 then
                if j >= 179 then
                    if j <= 0xb6 then
                        if j > 0xb4 then
                            f = f(_, o, l, b)
                            j, _ = 183 - j, false
                        elseif j <= 179 then
                            j = 169
                        else
                            l = l()
                            j, b = 0x12e - j, h[5][1][h[5][2]]
                            l = l - b
                        end
                    else
                        j, a = 0x252c / j, e.c(a(k, f))
                    end
                elseif j < 0xa9 then
                    n = e._["table"]
                    j, k, m, n = 182, h[2][1][h[2][2]], n["insert"], c
                    k, a, _ = "Since Last Summary", k["embedField"], e._["string"]
                    l, f, b, o, _ = h[7][1][h[7][2]], _["format"], h[3][1][h[3][2]], h[1][1][h[1][2]], "Eggs stolen: **%d**\nPets obtained: **%d**\nRebirths: **%d**"
                elseif j <= 169 then
                    o = o(l)
                    l = "`"
                    _ = o .. l
                    j, f = j + 14, f .. _
                else
                    j, a = 0x9792 / j, e.c(a(k, f))
                end
            elseif j <= 0xdf then
                if j > 221 then
                    m(n, e.d(a))
                    n = e._["table"]
                    n, k, m = c, h[2][1][h[2][2]], n["insert"]
                    l, f, k, a, o = d["Rebirth"], "`", "Rebirth", k["embedField"], e._["tostring"]
                    j = l and 0xb3 or 0xc083 / j
                elseif j <= 214 then
                    if j > 211 then
                        c = h[2][1][h[2][2]]
                        j, d = 0x18, c["getSave"]
                    else
                        j, n = j + 0x2b, e._["table"]
                        n, m, k = c, n["insert"], h[2][1][h[2][2]]
                        a, k, l, f = k["embedField"], "Money", h[2][1][h[2][2]], "`"
                        l, o = d["Money"], l["formatNumber"]
                    end
                else
                    j, l = 0xb3, 0
                end
            elseif j > 230 then
                j, o = 113, o(l)
                l = "`"
                _ = o .. l
                f = f .. _
            else
                m(n, e.d(a))
                n, k, f = {}, {}, "Steal an Egg | MMB HUB"
                k["name"] = f
                a = k
                n["author"] = a
                a = "Session Summary"
                n["title"] = a
                k = e._["string"]
                k, a, _ = "**Player** `%s`\n**Server** `%s`\n**Runtime** `%s`", k["format"], h[6][1][h[6][2]]
                _, f, l = h[4][1][h[4][2]], _["Name"], h[2][1][h[2][2]]
                o, j, b = l["formatElapsed"], 0xb4, e._["os"]
                l = b["clock"]
            end
        until false
    end
end,
sa = function (e, h)
    return function (d)
        local f, _, c, b, j, i, a, k
        j = 0x83
        while true do
            if j >= 117 then
                if j > 173 then
                    if j >= 208 then
                        if j <= 0xd0 then
                            j, i = 92, not b
                        else
                            i = false
                            return i
                        end
                    else
                        j, a = j + -0x7c, e._["Vector3"]
                        _, f, a, i = 5, c.Y, c.X, a["new"]
                        k, f = f + _, c.Z
                    end
                elseif j > 0x85 then
                    b = b()
                    i = not c
                    j = i and j + -0x51 or 208
                elseif j > 131 then
                    a = e.c(a(k, f))
                    return e.d(a)
                elseif j <= 0x75 then
                    j = i and 231 or 0xb7
                else
                    j, b = 0x21, h[1][1][h[1][2]]
                    c = b["getBasePosition"]
                end
            elseif j < 0x3b then
                if j < 33 then
                    i = d
                    j = i and 0x57c / j or 0x75
                elseif j > 0x21 then
                    i = false
                    return i
                else
                    c = c()
                    i = b
                    j, b = 0xce - j, i["getRoot"]
                end
            elseif j >= 78 then
                if j > 0x4e then
                    j = i and 0x30 or j + -0x4a
                else
                    j, a = 0x49, d
                end
            elseif j > 0x3b then
                j, a = 190 - j, a()
                i = not a
            else
                i = i(a, k, f)
                k = h[1][1][h[1][2]]
                j, k, f, a = j + 0x4a, i, d, k["humanoidStealMoveTo"]
            end
        end
    end
end,
Y = function (e)
    return function (...)
        local b, _, a, d, g, i, c
        _ = 0x6c
        repeat
            if _ > 108 then
                i = i(a, e.d(g))
                c.n = i
                b = e.c(...)
                e.e(c, 1, e.d(b))
                d = c
                return d
            else
                i, _, c, g, a = e._["select"], 0x9e, {}, e.c(...), "#"
            end
        until false
    end
end,
Xe = function (e, a)
    return function ()
        local b, _, c, d
        _ = 59
        while true do
            if _ > 59 then
                d = d(c, b)
                a[2][1][a[2][2]] = d
                return
            else
                _, b, d = 65, a[3][1][a[3][2]], a[1][1][a[1][2]]
                d, c = d.JSONEncode, d
            end
        end
    end
end,
Kd = function (e, g)
    return function (d)
        local b, c, _
        _ = 211
        while true do
            if _ >= 211 then
                _, b = 198, g[1][1][g[1][2]]
                b, c = d, b["applyFpsCap"]
            else
                c(b)
                return
            end
        end
    end
end,
ba = function (e, h)
    return function ()
        local c, d, f, _, b
        _ = 0x3f
        repeat
            if _ > 206 then
                if _ > 225 then
                    if _ <= 0xef then
                        b = 0
                        _ = c <= b and 0x86 or 0x1579 / _
                    else
                        _, c, b = 0x1c9 - _, e._["tonumber"], d["ClaimableAmount"]
                    end
                elseif _ >= 218 then
                    if _ <= 0xda then
                        c = c(b)
                        b = "table"
                        _ = c ~= b and 0xd5 or 0x1d5 - _
                    else
                        d = d(c)
                        b, _, c = d, 0xda, e._["typeof"]
                    end
                else
                    c = false
                    return c
                end
            elseif _ <= 70 then
                if _ <= 63 then
                    if _ > 0x1c then
                        c = h[2][1][h[2][2]]
                        _, b, d = 0xe1, h[1][1][h[1][2]], c["netInvoke"]
                        c = b["OfflineAssets"]
                        c = c["GET_SUMMARY"]
                    elseif _ > 0x17 then
                        _, c = 0xef, 0
                    else
                        b = h[2][1][h[2][2]]
                        _, c, f = 70, b["netCall"], h[1][1][h[1][2]]
                        b = f["OfflineAssets"]
                        b = b["REQUEST_REDEEM"]
                    end
                else
                    c(b)
                    c = true
                    return c
                end
            elseif _ <= 0x86 then
                c = false
                return c
            else
                c = c(b)
                _ = c and 0xef or 234 - _
            end
        until false
    end
end,
hb = function (e, h)
    return function (d)
        local j, i, b, k, f, a, _, c
        j = 2
        repeat
            if j > 0x72 then
                if j >= 0xc9 then
                    if j >= 220 then
                        if j <= 220 then
                            j = 0x183 - j
                            a(k)
                            k = h[1][1][h[1][2]]
                            a, f, _, k = k["waitFor"], 0.05, e:oe{h[2], i}, 1
                        else
                            a = true
                            return a
                        end
                    else
                        a = false
                        return a
                    end
                elseif j <= 0xa7 then
                    if j > 0x88 then
                        a = e.c(a(k, f, _))
                        return e.d(a)
                    else
                        i = false
                        return i
                    end
                else
                    a = i[1][i[2]]["Parent"]
                    j = a == c and j + 0x2f or j + -0x61
                end
            elseif j >= 77 then
                if j < 0x59 then
                    if j <= 0x4d then
                        a, j, k = e._["pcall"], 0x422c / j, e:ne{i, b}
                    else
                        a = h[1][1][h[1][2]]
                        i, j, a = a["findToolByUid"], 0x59, d
                    end
                elseif j <= 0x59 then
                    i = i(a)
                    i = {[2] = 3, [3] = i}
                    i[1] = i
                    a = not i[1][i[2]]
                    j = a and 0x122 - j or 0xae
                else
                    b = b()
                    b = {[2] = 3, [3] = b}
                    b[1] = b
                    i = not c
                    j = i and 0x2c or 0x8a - j
                end
            elseif j < 24 then
                b = h[2][1][h[2][2]]
                c, j, i = b["Character"], 0x72, h[1][1][h[1][2]]
                b = i["getHumanoid"]
            elseif j > 0x18 then
                j = i and 136 or 0x53
            else
                j, i = 0x2c, not b[1][b[2]]
            end
        until false
    end
end,
qb = function (e, h)
    return function ()
        local n, _, c, p, m, f, l, b, i, j, d, r, a, g, k
        j = 8
        repeat
            if j < 0x7b then
                if j > 51 then
                    if j <= 109 then
                        if j <= 0x67 then
                            if j < 89 then
                                p, f, _ = p(f)
                                p, f, _ = e.b(p, f, _)
                                r, l = p(f, _)
                                _ = r
                                j = _ == nil and 0x2074 / j or 0x2b5a / j
                            elseif j > 89 then
                                j, c = 188, d["EggInventory"]
                            else
                                j = b and 0x7a6 / j or 0xe5
                            end
                        else
                            r, l = p(f, _)
                            _ = r
                            j = _ == nil and 134 or 179
                        end
                    elseif j <= 114 then
                        j = i and 0xa9 or 223 - j
                    else
                        j, n = 0x87, n(a)
                        p = h[1][1][h[1][2]]
                        a, p = p["multiSelected"], "SellEggRarities"
                    end
                elseif j < 14 then
                    if j > 8 then
                        j, k, g = 114, true, a[b]
                        i = g == k
                    elseif j <= 1 then
                        g = g(k)
                        k = "string"
                        i = g == k
                        j = i and 11 or 115 - j
                    else
                        j, c = 51, h[1][1][h[1][2]]
                        d = c["getSave"]
                    end
                elseif j > 0x2e then
                    d = d()
                    c = d
                    j = c and 0x1485 / j or 0xef - j
                elseif j >= 0x16 then
                    if j > 22 then
                        j, a = 0x79, h[1][1][h[1][2]]
                        a, n = "SellEggRarities", a["multiHasAny"]
                    else
                        i, g = l["Placement"], nil
                        j, b = 251 - j, i == g
                    end
                else
                    return m
                end
            elseif j >= 188 then
                if j > 218 then
                    if j > 0xe5 then
                        k, j, g = b, 1, e._["typeof"]
                    elseif j > 0xdd then
                        j = b and 190 or 0x6d
                    else
                        b = b(i)
                        i = not n
                        j = i and j + -0x6b or 0xe7
                    end
                elseif j >= 216 then
                    if j <= 0xd8 then
                        n = n(a)
                        a = "table"
                        j = n ~= a and 14 or 0x2e
                    else
                        i = i(g)
                        g = "string"
                        b = i == g
                        j = b and 0x68be / j or 307 - j
                    end
                elseif j <= 188 then
                    n = {}
                    a, n, j, m = c, e._["typeof"], 0x9ea0 / j, n
                else
                    i = h[1][1][h[1][2]]
                    i, j, b = l["AssetCategory"], 0x19b - j, i["resolveRarity"]
                end
            elseif j <= 135 then
                if j <= 134 then
                    if j < 126 then
                        i, j, g = e._["typeof"], j + 28, l
                    elseif j <= 0x7e then
                        j = 0x6d
                        i(g, k)
                    else
                        return m
                    end
                else
                    a = a(p)
                    f, j, p = c, 0x3e, e._["pairs"]
                end
            elseif j <= 0xa9 then
                if j > 0x97 then
                    j, g = 0x7e, e._["table"]
                    i, k, g = g["insert"], r, m
                else
                    i = i(g)
                    j, g = 240 - j, "table"
                    b = i == g
                end
            else
                j, i, g = 0x986e / j, e._["typeof"], r
            end
        until false
    end
end,
b = (function ()
    local q, i, s = type, getmetatable, pairs
    return function (u, v, w)
        if q(u) ~= "function" then
            local p = i(u)
            if p ~= nil and p.__iter ~= nil then
                return p.__iter(u)
            elseif (p and p.__call) == nil and q(u) == "table" then
                return s(u)
            end
        end
        return u, v, w
    end
end)(),
M = function (e, g)
    return function ()
        local c, d, b, f, _
        _ = 195
        while true do
            if _ <= 104 then
                if _ >= 93 then
                    if _ > 0x5d then
                        _, c = 173 - _, nil
                    else
                        _, c = 169, c(b, f)
                    end
                elseif _ > 43 then
                    return c
                else
                    b, _, f, c = d, 93, "HumanoidRootPart", d.FindFirstChild
                end
            elseif _ > 169 then
                c = g[1][1][g[1][2]]
                d = c["Character"]
                c = d
                _ = c and 0x2b or 169
            else
                _ = c and 0x45 or 104
            end
        end
    end
end,
cb = function (e, h)
    return function ()
        local k, f, j, i, d, c, b
        j = 0x1a
        repeat
            if j > 0x97 then
                if j <= 0xa2 then
                    i = d(c, b)
                    b = i
                    j = b == nil and 360 - j or 0x97
                else
                    return
                end
            elseif j <= 0x51 then
                if j <= 63 then
                    if j > 26 then
                        d, c, b = d(c)
                        d, c, b = e.b(d, c, b)
                        i = d(c, b)
                        b = i
                        j = b == nil and 198 or 0x97
                    else
                        j, c, d = 0x3f, h[2][1][h[2][2]], e._["pairs"]
                    end
                else
                    j = j + 81
                    k(f)
                end
            else
                j, f = 0x51, h[1][1][h[1][2]]
                k, f = f["releaseEsp"], i
            end
        until false
    end
end,
le = function (e, a)
    return function ()
        local d, _, c
        _ = 0x21
        repeat
            if _ > 33 then
                d(c)
                return
            else
                c = a[1][1][a[1][2]]
                _, c, d = 0x3d, true, c["runAutoPlaceEggs"]
            end
        until false
    end
end,
n = function (e, h)
    return function ()
        local j, d, b, _, c, f, i, k
        j = 0xd4
        while true do
            if j >= 0x71 then
                if j <= 148 then
                    if j <= 133 then
                        if j > 122 then
                            j = 0x3a
                            k(f)
                        elseif j > 0x71 then
                            d, c, b = d(c)
                            d, c, b = e.b(d, c, b)
                            i = d(c, b)
                            b = i
                            j = b == nil and 202 - j or 0x1d12 / j
                        else
                            j, f = 0x3ab5 / j, h[2][1][h[2][2]]
                            k, f = f["releaseEsp"], i
                        end
                    else
                        d(c)
                        c = h[2][1][h[2][2]]
                        j, d = 0x143c / j, c["collectEggEsp"]
                    end
                elseif j <= 0xd4 then
                    if j <= 0xa1 then
                        j = j + -159
                        d()
                        d = c["collectPlayerEsp"]
                    else
                        c = h[2][1][h[2][2]]
                        c, j, d = h[1][1][h[1][2]], 0x94, c["clearTable"]
                    end
                else
                    j = 351 - j
                    d()
                    d, c = e._["pairs"], h[3][1][h[3][2]]
                end
            elseif j >= 58 then
                if j >= 0x3e then
                    if j <= 62 then
                        d()
                        j, d = 229, c["collectPlotEsp"]
                    else
                        return
                    end
                elseif j <= 58 then
                    i = d(c, b)
                    b = i
                    j = b == nil and 80 or 61
                else
                    _ = h[1][1][h[1][2]]
                    f = _[i]
                    k = not f
                    j = k and 113 or 0xdd2 / j
                end
            elseif j < 8 then
                d()
                j, d = 0x7c / j, c["collectMachineEsp"]
            elseif j > 8 then
                d()
                j, d = 8, c["collectGuardEsp"]
            else
                j = 169 - j
                d()
                d = c["collectPetEsp"]
            end
        end
    end
end,
Pa = function (e, h)
    return function (d)
        local m, n, k, _, b, l, f, i, o, j, a, c
        j = 0x87
        while true do
            if j <= 0x83 then
                if j < 0x35 then
                    if j > 0x15 then
                        if j <= 0x24 then
                            if j < 0x1d then
                                o = e._["table"]
                                b, _, j, o = e._["table"], o["insert"], 0x15, n
                                b, l, i = f, b["concat"], ", "
                            elseif j > 29 then
                                return
                            else
                                j, m = 104, d["AssetCategory"]
                            end
                        elseif j <= 50 then
                            j, a = 0xa5, d["AreaId"]
                        else
                            j, a = 13, c["AreaId"]
                        end
                    elseif j >= 0x12 then
                        if j > 20 then
                            j, l = 0x98, e.c(l(b, i))
                        elseif j > 18 then
                            return
                        else
                            n, j, m = d["Uid"], 0x94, e._["typeof"]
                        end
                    elseif j <= 13 then
                        if j > 11 then
                            j = a and 0x861 / j or 50
                        else
                            j, _ = 244, e.c(_(o, l))
                        end
                    else
                        k = k(f)
                        f = "string"
                        j = k == f and 0xac0 / j or 0x35
                    end
                elseif j < 0x54 then
                    if j >= 64 then
                        if j > 75 then
                            m = h[2][1][h[2][2]]
                            j, c, m = j + 0x47, m["findAreaEggRecord"], d["Uid"]
                        elseif j <= 64 then
                            j = m and 104 or 29
                        else
                            l = l(b)
                            j = l and 0xed or 0xb5
                        end
                    elseif j <= 0x35 then
                        j = c and 0xb7 or 0xf2
                    else
                        j = c and j + 0xa1 or j + 38
                    end
                elseif j < 0x7e then
                    if j < 97 then
                        _ = h[2][1][h[2][2]]
                        j, _, f = 0xe3, c, _["recordMutations"]
                    elseif j > 0x61 then
                        a, f = {}, e._["string"]
                        j, o, f, k = 0xb0, h[2][1][h[2][2]], "**%s** `%s`", f["format"]
                        _, o = o["assetName"], m
                    else
                        j, c = 0xdc, nil
                    end
                elseif j <= 129 then
                    if j > 126 then
                        j, m = 193 - j, c["AssetCategory"]
                    else
                        k = k(f)
                        j = k and 257 - j or 0xd2 - j
                    end
                else
                    _ = e._["table"]
                    _, j, f, l = n, 234, _["insert"], e._["string"]
                    l, o, b = "x%.2f", l["format"], k
                end
            elseif j < 0xb7 then
                if j < 0x9d then
                    if j <= 148 then
                        if j < 0x8f then
                            j, m, c = 0x9d, d, e._["typeof"]
                        elseif j <= 0x8f then
                            j = 0x54
                            f(_, e.d(o))
                        else
                            m = m(n)
                            n = "string"
                            c = m == n
                            j = c and j + -0x42 or 59
                        end
                    elseif j <= 152 then
                        j = j + 90
                        _(o, e.d(l))
                    else
                        j, c = j + -0x5e, c(m)
                    end
                elseif j <= 0xac then
                    if j <= 0xa5 then
                        if j > 0x9d then
                            k, j, f = e._["typeof"], j + -0x95, a
                        else
                            c = c(m)
                            m = "table"
                            j = c ~= m and 20 or 0x12
                        end
                    else
                        j, f = 230, e._["table"]
                        f, k, _ = n, f["insert"], a
                    end
                elseif j <= 176 then
                    j, _ = 251 - j, _(o)
                    b, o = h[2][1][h[2][2]], e._["tostring"]
                    b, l = m, b["resolveRarity"]
                else
                    j, l = 0xa791 / j, "?"
                end
            elseif j < 230 then
                if j > 190 then
                    if j <= 0xdc then
                        m = c
                        j = m and 0x81 or 0x3700 / j
                    else
                        f = f(_)
                        o, _ = 0, #f
                        j = _ > o and 26 or j + 15
                    end
                elseif j <= 0xb8 then
                    if j <= 0xb7 then
                        f, j, k = c["AssetScale"], 309 - j, e._["tonumber"]
                    else
                        k = e.c(k(f, _, e.d(o)))
                        e.e(a, 1, e.d(k))
                        n, a = a, c
                        j = a and 236 - j or 13
                    end
                else
                    j, f = 11, e._["table"]
                    f, k, o = h[1][1][h[1][2]], f["insert"], e._["table"]
                    _, l, o = o["concat"], " | ", n
                end
            elseif j < 0xf2 then
                if j > 0xea then
                    j = 248
                elseif j > 230 then
                    j, o = 143, e.c(o(l, b))
                else
                    j = 53
                    k(f, _)
                end
            elseif j > 244 then
                j, o = 0xb240 / j, e.c(o(l))
            elseif j <= 242 then
                f = h[1][1][h[1][2]]
                k, f = #f, 100
                j = k < f and j + -0x34 or 36
            else
                j = 36
                k(f, e.d(_))
            end
        end
    end
end,
e = function (e, f, ...)
    local h = {...}
    local d = select("#", ...)
    for i = 1, d do
        e[f + i - 1] = h[i]
    end
end,
Tc = function (e, g)
    return function ()
        local c, b, d
        c, b = g[1][1][g[1][2]], true
        d = c == b
        return d
    end
end,
zb = function (s, h)
    return function (d)
        local p, k, a, b, r, l, c, m, i, j, _, f, g, q, n
        j = 202
        while true do
            if j >= 0x7b then
                if j >= 221 then
                    if j > 239 then
                        if j > 0xf9 then
                            f, _, r = f(_)
                            f, _, r = s.b(f, _, r)
                            l, b = f(_, r)
                            r = l
                            j = r == nil and 0x6db3 / j or 76
                        elseif j <= 245 then
                            j, g = 423 - j, -i
                        else
                            j, m = j + -28, m(n)
                            a = h[2][1][h[2][2]]
                            p, a, n = "Highest Rarity", "FuseTarget", a["optionValue"]
                        end
                    elseif j <= 228 then
                        if j <= 0xe3 then
                            if j <= 221 then
                                n = n(a, p)
                                _, a = s._["math"], nil
                                j, f = 253, _["huge"]
                                f, p, _ = s._["pairs"], -f, c
                            else
                                j = 476 - j
                            end
                        else
                            j, n = 0xca2c / j, 0
                        end
                    else
                        k = k(q)
                        j = k and 18 or 0x79
                    end
                elseif j <= 0xb2 then
                    if j > 166 then
                        j = g > p and j + -129 or j + 4
                    elseif j > 128 then
                        j, g = 178, #b
                    elseif j > 123 then
                        r, f = {}, c[a]
                        b = f[1]
                        i, l = f[2], b["uid"]
                        b, g = i["uid"], f[3]
                        i = g["uid"]
                        r[1], r[2], r[3] = l, b, i
                        _ = r
                        return _
                    else
                        c = c(m)
                        n = s._["math"]
                        m, n, p = n["floor"], s._["tonumber"], h[2][1][h[2][2]]
                        j, p, f, a = j + -72, "FuseKeepPerCategory", 0, p["optionValue"]
                    end
                elseif j <= 182 then
                    l, b = f(_, r)
                    r = l
                    j = r == nil and 111 or 0x3608 / j
                else
                    j, m = 123, h[2][1][h[2][2]]
                    m, c = d, m["fuseGroups"]
                end
            elseif j < 0x3f then
                if j > 26 then
                    if j <= 49 then
                        a, j, p = l, 0xb6, g
                    else
                        j, a = 78, s.c(a(p, f))
                    end
                elseif j < 19 then
                    if j <= 1 then
                        i(g, k)
                        g = #b
                        i, g = g - m, 3
                        j = i >= g and 70 - j or 0xb6
                    else
                        i = g[k]
                        j = i and 106 or 0x3f
                    end
                elseif j <= 19 then
                    k = "Lowest Rarity"
                    j = n == k and 0x122f / j or j + 159
                else
                    f = nil
                    return f
                end
            elseif j < 78 then
                if j > 0x45 then
                    j, g = 76 / j, s._["table"]
                    g, k, i = b, s:Be(), g["sort"]
                elseif j > 63 then
                    q, j, g = h[2][1][h[2][2]], j + 0xaa, h[1][1][h[1][2]]
                    q, k = l, q["resolveRarity"]
                else
                    j, i = 0x6a, 0
                end
            elseif j < 0x6f then
                if j > 0x4e then
                    k, g = "Most Duplicates", i
                    j = n == k and 272 - j or 0x13
                else
                    n = n(s.d(a))
                    j = n and 0xe3 or 0x132 - j
                end
            elseif j > 111 then
                j, k = 0x882 / j, "Common"
            else
                f = not a
                j = f and 0xb46 / j or 239 - j
            end
        end
    end
end,
Of = function (a, b, c, d)
    a.Nf[d] = a.if_(b, c)
    return a.Nf[d]
end,
Ff = {}, L = function (e, a)
    return function (d)
        local _, c, b
        _ = 67
        while true do
            if _ > 0xdd then
                return
            elseif _ > 0xc2 then
                _, b, c = 0xa77a / _, e:gd{d, a[1]}, e._["pcall"]
            elseif _ > 0x43 then
                _ = 243
                c(b)
            else
                d = {[2] = 3, [3] = d}
                d[1] = d
                c = a[1][1][a[1][2]]
                _ = c and 0xdd or 0xf3
            end
        end
    end
end,
Ua = function (e, h)
    return function (d, c, b)
        local a, f, _
        _ = 218
        repeat
            if _ <= 0xab then
                if _ >= 0x90 then
                    if _ > 0x90 then
                        return
                    else
                        a, f = b, e._["tostring"]
                        _ = a and 0x1b00 / _ or 65
                    end
                elseif _ > 0x30 then
                    _, a = _ + -17, c
                else
                    _ = 259 - _
                end
            elseif _ <= 0xd3 then
                f = f(a)
                _, h[1][1][h[1][2]] = _ + -40, f
            else
                f = h[2][1][h[2][2]]
                _ = d == f and 0x90 or 0xab
            end
        until false
    end
end,
Id = function (e, a)
    return function ()
        local _, d, c
        _ = 0xd0
        repeat
            if _ < 208 then
                d(c)
                return
            else
                c = e._["task"]
                _, c, d = 52, e:ae{a[2], a[1]}, c["spawn"]
            end
        until false
    end
end,
ob = function (e, h)
    return function (d, ...)
        local c, _, b, f
        _ = 9
        while true do
            if _ <= 237 then
                if _ <= 0x38 then
                    if _ > 9 then
                        b = nil
                        return b
                    else
                        b = h[1][1][h[1][2]]
                        f, b, _, c = e.c(...), d, 0xf6, b["pickFromTable"]
                    end
                else
                    b = b(f)
                    f = "Instance"
                    _ = b == f and _ + 12 or _ + -0xb5
                end
            elseif _ <= 0xf6 then
                c = c(b, e.d(f))
                _, f, b = 0xe3be / _, c, e._["typeof"]
            else
                return c
            end
        end
    end
end,
tb = function (e, h)
    return function (d, c)
        local a, b, j, f, k, i
        j = 0xf6
        repeat
            if j <= 168 then
                if j < 0x99 then
                    if j > 46 then
                        j, i = 153, h[1][1][h[1][2]]
                        b = i["unload"]
                    else
                        f, i = e._["Enum"], d["KeyCode"]
                        j, k = 214 - j, f["KeyCode"]
                        a = k["End"]
                        b = i == a
                    end
                elseif j <= 153 then
                    j = j + 0x5f
                    b()
                else
                    j = b and 299 - j or 416 - j
                end
            elseif j <= 246 then
                b = not c
                j = b and 46 or 0xa8
            else
                return
            end
        until false
    end
end,
eb = function (e, g)
    return function ()
        local b, d, _, c
        _ = 0x8a
        repeat
            if _ >= 138 then
                _, b = 48, e._["os"]
                c = b["clock"]
            else
                c = c()
                b = g[1][1][g[1][2]]
                d = c < b
                return d
            end
        until false
    end
end,
bd = function (e, g)
    return function ()
        local _, c, b, d
        _ = 65
        while true do
            if _ <= 121 then
                if _ < 0x41 then
                    _, b = 0x1482 / _, nil
                    c = d == b
                elseif _ <= 65 then
                    c = g[2][1][g[2][2]]
                    c, _, d = "PlayerRequest", 0x79, c["RequestDropHeldAreaEgg"]
                else
                    d = d(c)
                    b = true
                    c = d == b
                    _ = c and _ + 0x36 or 0x1e
                end
            else
                g[1][1][g[1][2]] = c
                return
            end
        end
    end
end,
we = function (e, a)
    return function ()
        local c, _, d
        _ = 249
        repeat
            if _ >= 249 then
                d, c = a[1][1][a[1][2]], true
                d["Disabled"] = c
                d, _, c = d.Destroy, 237, d
            else
                d(c)
                return
            end
        until false
    end
end,
nb = function (e, h)
    return function (d, c)
        local n, j, o, _, i, f, m, l, b, a, k
        j = 0x4e
        repeat
            if j >= 0x83 then
                if j <= 190 then
                    if j >= 0xb8 then
                        if j > 184 then
                            j, l = 0xb8, h[1][1][h[1][2]]
                            b, o, l, i = f.Z, l["stealMoveTo"], f.X, c
                        else
                            o = o(l, b, i)
                            _ = not o
                            j = _ and 247 or 0x8c
                        end
                    elseif j <= 131 then
                        j, o = 0x3a, c
                    else
                        k, f = m(n, a)
                        a = k
                        j = a == nil and 0x2760 / j or 0x94c / j
                    end
                elseif j > 0xe7 then
                    _ = false
                    return _
                else
                    _ = false
                    return _
                end
            elseif j >= 0x48 then
                if j <= 78 then
                    if j > 72 then
                        j, m, n = 0x42, e._["ipairs"], d
                    else
                        m = true
                        return m
                    end
                else
                    j = _ and 0xe7 or 0xbe
                end
            elseif j <= 0x3a then
                if j > 0x11 then
                    j, o = 115, o()
                    _ = not o
                else
                    _ = c
                    j = _ and j + 0x72 or 0x84 - j
                end
            else
                m, n, a = m(n)
                m, n, a = e.b(m, n, a)
                k, f = m(n, a)
                a = k
                j = a == nil and 0x48 or j + -49
            end
        until false
    end
end,
Yd = function (e, g)
    return function (d)
        local c, _, b
        _ = 159
        while true do
            if _ >= 159 then
                b = g[1][1][g[1][2]]
                _, b, c = 15, d, b["applyAntiGameplayPause"]
            else
                c(b)
                return
            end
        end
    end
end,
Ub = function (e, h)
    return function ()
        local o, f, d, _, l, p, g, j, a, c, n, i, k, b, m
        j = 0x6a
        repeat
            if j > 0xa5 then
                if j > 192 then
                    if j <= 0xeb then
                        if j > 231 then
                            j, b = 2, e._["string"]
                            b, g, k, i, l = o, 1, true, "ragdoll", b["find"]
                        elseif j <= 0xe4 then
                            if j > 0xce then
                                j, n = 0x9a, not m
                            else
                                n, a, p = n(e.d(a))
                                n, a, p = e.b(n, a, p)
                                f, _ = n(a, p)
                                p = f
                                j = p == nil and 455 - j or 0x11
                            end
                        else
                            j, m = 0x171 - j, h[1][1][h[1][2]]
                            c = m["stealingEnabled"]
                        end
                    elseif j <= 0xf9 then
                        if j > 240 then
                            a = e._["Vector3"]
                            n = a["zero"]
                            m["AssemblyLinearVelocity"] = n
                            n = a["zero"]
                            m["AssemblyAngularVelocity"] = n
                            return
                        else
                            o = o(l, b)
                            j = o and 178 or 0x1a0 - j
                        end
                    else
                        o = o(l)
                        j, b = 443 - j, e._["string"]
                        l, g, b, k, i = b["find"], 1, o, true, "push"
                    end
                elseif j <= 178 then
                    if j > 0xb0 then
                        if j > 177 then
                            l = e._["string"]
                            l, j, o = _[1][_[2]]["Name"], 252, l["lower"]
                        else
                            j, n = j + -12, not c[1][c[2]]
                        end
                    elseif j >= 0xad then
                        if j > 173 then
                            f, _ = n(a, p)
                            p = f
                            j = p == nil and 249 or 17
                        else
                            return
                        end
                    else
                        n(a)
                        p, j, n, a = d, 196 - j, e._["ipairs"], d.GetDescendants
                    end
                elseif j <= 0xbf then
                    if j <= 188 then
                        if j <= 0xb4 then
                            j = 0x7bc0 / j
                            l(b)
                        else
                            j = l and 37 or 235
                        end
                    else
                        l = l(b, i, g, k)
                        j = l and 0x8c44 / j or 192
                    end
                else
                    j, b = 0x7680 / j, e._["string"]
                    l, k, g, i, b = b["find"], true, 1, "knock", o
                end
            elseif j <= 101 then
                if j >= 0x1f then
                    if j <= 74 then
                        if j <= 37 then
                            if j <= 0x1f then
                                m = m()
                                n = not d
                                j = n and 196 - j or 177
                            else
                                j = l and 12 or 0x1970 / j
                            end
                        else
                            return
                        end
                    elseif j > 98 then
                        c = c()
                        c = {[2] = 3, [3] = c}
                        j, c[1] = 0x84 - j, c
                        n = m
                        m = n["getRoot"]
                    else
                        n(a)
                        j, a = 167, e:Me{c}
                    end
                elseif j < 0x11 then
                    if j > 2 then
                        j, l, b = j + 168, e._["pcall"], e:Le{_}
                    else
                        j, l = 0x4a / j, l(b, i, g, k)
                    end
                elseif j <= 17 then
                    _ = {[2] = 3, [3] = _}
                    _[1] = _
                    j, b, o, l = 0xff0 / j, "LocalScript", _[1][_[2]].IsA, _[1][_[2]]
                else
                    j, a = 0xce, e.c(a(p))
                end
            elseif j <= 138 then
                if j > 0x6a then
                    if j <= 0x75 then
                        j = d and 0x21d2 / j or 0xde - j
                    else
                        j, c = 117, c()
                        d = not c
                    end
                elseif j >= 105 then
                    if j > 0x69 then
                        c = h[2][1][h[2][2]]
                        d = not c
                        j = d and 0x75 or 0xe7
                    else
                        j, c = j + -4, h[3][1][h[3][2]]
                        d, m = c["Character"], h[1][1][h[1][2]]
                        c = m["getHumanoid"]
                    end
                else
                    n, j, a = e._["pcall"], 0x62, e:Ke{c}
                end
            elseif j > 0x9e then
                j = n and 0x9a or 0xe4
            elseif j > 154 then
                j, l = 0xbc, l(b, i, g, k)
            else
                j = n and 0xad or 0x66
            end
        until false
    end
end,
_a = function (e)
    return function (d)
        local i, _, b, k, f, j, a, c
        j = 128
        while true do
            if j <= 128 then
                if j >= 115 then
                    if j < 127 then
                        i = i(a)
                        a = 0
                        j = b > a and 0x7f or 0xe3
                    elseif j > 0x7f then
                        b = e._["math"]
                        a, c, j, b = e._["math"], b["max"], 0xaa, 0
                        i, a = a["floor"], d
                    else
                        k = e._["string"]
                        k, _, a, j, f = "%dh %dm", i, k["format"], 0x8c - j, b
                    end
                elseif j <= 13 then
                    a = e.c(a(k, f, _))
                    return e.d(a)
                else
                    a = e.c(a(k, f))
                    return e.d(a)
                end
            elseif j > 240 then
                c = c(b, e.d(i))
                i = e._["math"]
                b, i = i["floor"], 0xe10
                j, i = 0xed30 / j, c / i
            elseif j < 227 then
                j, i = 423 - j, e.c(i(a))
            elseif j <= 227 then
                j, k = 0x4a, e._["string"]
                k, f, a = "%dm", i, k["format"]
            else
                b = b(i)
                a = e._["math"]
                k, i = 0xe10, a["floor"]
                k, j, a = 60, 0x6bd0 / j, c % k
                a = a / k
            end
        end
    end
end,
Af = function (a, b, c, d)
    a.zf[d] = a.if_(b, c)
    return a.zf[d]
end,
Pf = function (a, ...)
    a.kf, a.gf, a.if_ = a:kf(), a:gf(), a:if_()
    return a:f()(...)
end,
If = function (a, b, c, d)
    a.Hf[d] = a.gf(b, c)
    return a.Hf[d]
end,
P = function (e, g)
    return function ()
        local d, b, c
        d, b = g[2][1][g[2][2]], g[1][1][g[1][2]]
        c = b["protect_gui"]
        d["protect_gui"] = c
        return
    end
end,
hf = function (e, h)
    return function (d, c)
        local l, o, a, n, b, g, f, _, m, i, p, j
        j = 0x51
        repeat
            if j < 0x5d then
                if j >= 0x47 then
                    if j >= 85 then
                        if j <= 85 then
                            j = n > a and 93 or 0x11
                        else
                            j, l = 11, e.c(l(b, i))
                        end
                    elseif j > 0x47 then
                        n, f, _, m = 0, #d, 1, ""
                        p, a = _, f - _
                        j = a ~= a and 93 or 107
                    else
                        j = p ~= p and 170 or 228
                    end
                elseif j >= 0x15 then
                    if j > 0x15 then
                        j, o = 0x10a7 / j, o(l, b)
                        b, g, l = c, #c, h[3][1][h[3][2]]
                        i, g = n % g, 1
                        i = i + g
                    else
                        j = p ~= p and 0x72 - j or j + 75
                    end
                elseif j <= 11 then
                    j, _ = 254, e.c(_(o, e.d(l)))
                else
                    j = p <= 0 and 210 or 0x165 / j
                end
            elseif j <= 170 then
                if j <= 0x6b then
                    if j >= 0x60 then
                        if j <= 0x60 then
                            b, f, l, o, _ = 1, h[2][1][h[2][2]], d, h[3][1][h[3][2]], h[1][1][h[1][2]]
                            j, b = 0x91 - j, n + b
                        else
                            j = p > 0 and 312 - j or 0x1dad / j
                        end
                    else
                        return m
                    end
                elseif j > 164 then
                    j = n < a and 263 - j or 0x10a - j
                else
                    n = n + p
                    j = p > 0 and 0x3674 / j or 0x11
                end
            elseif j > 0xe4 then
                f = f(e.d(_))
                j, m = j + -0x5a, m .. f
            elseif j <= 210 then
                if j <= 205 then
                    j = n > a and 93 or 71
                else
                    j = n < a and 0x5d or 0x113a / j
                end
            else
                j = p <= 0 and 170 or 0x60
            end
        until false
    end
end,
H = function (e, h)
    return function (d)
        local f, j, b, i, c, g, a
        j = 237
        while true do
            if j >= 0x99 then
                if j < 0xbb then
                    if j <= 0x9e then
                        if j > 153 then
                            c = false
                            return c
                        else
                            j, i = 20, 1.5
                        end
                    else
                        c = c(b)
                        b = not c
                        j = b and j + 21 or 0x417e / j
                    end
                elseif j <= 0xc6 then
                    if j <= 187 then
                        b = false
                        return b
                    else
                        b = b(i)
                        c = not b
                        j = c and 0x9e or 116
                    end
                else
                    j, i = 198, h[1][1][h[1][2]]
                    i, b = "StealBigEggs", i["isOn"]
                end
            elseif j > 0x65 then
                if j > 116 then
                    j, a = 0x5f, e.c(a(g, f))
                else
                    j, c, b = 166, e._["tonumber"], d["AssetScale"]
                end
            elseif j >= 0x5f then
                if j <= 0x5f then
                    i = i(e.d(a))
                    j = i and 0x14 or 153
                else
                    g, i = h[1][1][h[1][2]], e._["tonumber"]
                    j, g, a, f = 131, "StealBigEggScale", g["optionValue"], 1.5
                end
            else
                b = c >= i
                return b
            end
        end
    end
end,
dc = function (e, h)
    return function (d, c)
        local f, b, a, _
        _ = 0xe9
        repeat
            if _ <= 0xbe then
                if _ <= 0x9c then
                    if _ <= 0x76 then
                        return c
                    else
                        return b
                    end
                else
                    b = b(f, a)
                    f = nil
                    _ = b == f and 308 - _ or 0x73c8 / _
                end
            else
                _, f = 190, h[1][1][h[1][2]]
                f, b, a = d, f["getState"], c
            end
        until false
    end
end,
md = function (e, a)
    return function ()
        local _, d, c
        _ = 0x59
        while true do
            if _ > 0x59 then
                d(c)
                return
            else
                _, c = 0xc0, a[1][1][a[1][2]]
                d, c = c["RequestDropHeldAreaEgg"], "PlayerRequest"
            end
        end
    end
end,
Ae = function (e, a)
    return function ()
        local c, _, d
        _ = 0x83
        while true do
            if _ > 0x83 then
                d(c)
                return
            else
                d = a[1][1][a[1][2]]
                _, c, d = 248, d, d.Destroy
            end
        end
    end
end,
ha = function (e, g)
    return function ()
        local d, b, f, c, _
        _ = 0x57
        repeat
            if _ > 0x99 then
                if _ <= 160 then
                    _, c = 0xc8, nil
                else
                    return c
                end
            elseif _ > 0x57 then
                _ = c and 353 - _ or _ + 7
            elseif _ >= 30 then
                if _ > 0x1e then
                    c = g[1][1][g[1][2]]
                    d = c["Character"]
                    c = d
                    _ = c and 29 or 0x99
                else
                    _, c = 0x99, c(b, f)
                end
            else
                b, _, c, f = d, 0x1e, d.FindFirstChildOfClass, "Humanoid"
            end
        until false
    end
end,
Ye = function (b)
    return function ()
        return
    end
end,
S = function (e)
    return function (d)
        local _, c, b, f
        _ = 0x65
        while true do
            if _ <= 0xc7 then
                if _ <= 101 then
                    if _ > 0x37 then
                        c = d
                        _ = c and 0xcd or 0x37
                    elseif _ > 2 then
                        _ = c and 2 or 0xc7
                    else
                        c = false
                        _, d["CanCollide"] = 201 - _, c
                    end
                else
                    return
                end
            elseif _ <= 205 then
                f, _, c, b = "BasePart", 227, d.IsA, d
            else
                _, c = 0x37, c(b, f)
            end
        end
    end
end,
Qc = function (s, h)
    return function ()
        local t, j, y, w, n, A, _, i, D, x, B, c, k, l, z, f, a, v, d, b, q, g, m, E, r, o, p, C
        j = 83
        while true do
            if j <= 0x8e then
                if j >= 67 then
                    if j > 0x6b then
                        if j >= 137 then
                            if j <= 0x8d then
                                if j >= 138 then
                                    if j <= 138 then
                                        w = w(B)
                                        B = "string"
                                        p = w == B
                                        j = p and 233 or 159
                                    else
                                        _ = _(r)
                                        l = h[1][1][h[1][2]]
                                        j, r, l = 0x4680 / j, l["multiHasAny"], "SellMutations"
                                    end
                                else
                                    j, w = j + -0x68, p
                                end
                            else
                                n = n(a)
                                a = "table"
                                j = n ~= a and 228 or 0x76
                            end
                        elseif j < 124 then
                            n = d["EquippedAssets"]
                            j = n and 232 or 180
                        elseif j > 0x7c then
                            j, r = 0x6580 / j, r(l)
                            t = h[1][1][h[1][2]]
                            t, l = "SellRarities", t["multiSelected"]
                        else
                            E = E(p)
                            p = not t
                            j = p and 283 - j or 70
                        end
                    elseif j <= 0x50 then
                        if j <= 71 then
                            if j > 0x46 then
                                w, B = m(E, p)
                                p = w
                                j = p == nil and j + 128 or 182
                            elseif j <= 0x43 then
                                m, E, p = m(E)
                                m, E, p = s.b(m, E, p)
                                w, B = m(E, p)
                                p = w
                                j = p == nil and j + 132 or 182
                            else
                                w, j, B = s._["typeof"], 138, E
                            end
                        elseif j > 74 then
                            j, a = 258 - j, 10
                        else
                            q = f
                            j = q and j + 83 or 0x93
                        end
                    elseif j >= 0x62 then
                        if j > 0x62 then
                            t = t(i)
                            j, i, g = 174, s._["pairs"], c
                        else
                            j = m and 0xeee / j or j + 0x65
                        end
                    elseif j > 83 then
                        x, o = true, D["InFuse"]
                        j, q = j + 153, o == x
                    else
                        j, c = 240, h[1][1][h[1][2]]
                        d = c["getSave"]
                    end
                elseif j <= 33 then
                    if j > 0x12 then
                        if j >= 31 then
                            if j > 0x1f then
                                j = w and 0x17d9 / j or 6
                            else
                                j, z = j + 0x20, z(f)
                                _ = h[1][1][h[1][2]]
                                f, _ = _["isOn"], "SellKeepEquipped"
                            end
                        elseif j <= 20 then
                            b = b(q)
                            q = "table"
                            j, D = j + 0xcc, b == q
                        else
                            o = o(x)
                            m = z
                            j = m and 0xe6 or 0x3c - j
                        end
                    elseif j <= 13 then
                        if j >= 6 then
                            if j <= 6 then
                                y, v = i(g, k)
                                k = y
                                j = k == nil and 0x10 or 0x100 - j
                            else
                                j, p = j + 0x6f, h[1][1][h[1][2]]
                                p, E = v["Category"], p["resolveRarity"]
                            end
                        else
                            b = b(q)
                            q = "string"
                            D = b == q
                            j = D and 201 or 0xe0
                        end
                    elseif j > 16 then
                        j = w and 137 or 0x33 - j
                    else
                        return A
                    end
                elseif j >= 0x33 then
                    if j < 0x39 then
                        if j <= 51 then
                            j, b = 243, h[1][1][h[1][2]]
                            b, D = v, b["getPetItemData"]
                        else
                            m = m(E)
                            j = m and j + -0x29 or 0x1e96 / j
                        end
                    elseif j > 57 then
                        f = f(_)
                        r = h[1][1][h[1][2]]
                        j, _, r = 141, r["multiSelected"], "SellMutations"
                    else
                        o, j, x = D["IsFavorite"], 189, true
                        q = o == x
                    end
                elseif j > 39 then
                    a = a(s.d(z))
                    j = a and 0x1de6 / j or 0x7b - j
                elseif j > 0x25 then
                    j, E, m, x = j + 0x1c, o, s._["ipairs"], false
                else
                    x = not m
                    m = x
                    j = m and 0xba - j or 98
                end
            elseif j >= 191 then
                if j > 0xe6 then
                    if j > 0xf0 then
                        if j <= 0xf3 then
                            if j <= 242 then
                                j = q and 147 or 74
                            else
                                D = D(b)
                                j, o = 0xc3, s._["table"]
                                o, q, x = n, o["find"], y
                            end
                        else
                            b, j, q = s._["typeof"], 253 - j, y
                        end
                    elseif j < 0xec then
                        if j <= 0xe8 then
                            f, j, a = h[1][1][h[1][2]], 0x93b8 / j, s._["tonumber"]
                            _, z, f = 10, f["optionValue"], "SellMaxScale"
                        else
                            B, j, w = true, 0x90b7 / j, l[E]
                            p = w == B
                        end
                    elseif j > 236 then
                        d = d()
                        c = d
                        j = c and 0xb310 / j or 152
                    else
                        j, x = j + -0x25, true
                    end
                elseif j > 0xcb then
                    if j > 0xe4 then
                        p, E = 0, #o
                        j, m = 0x25, E > p
                    elseif j < 0xe3 then
                        j = D and 51 or 0xe6 - j
                    elseif j <= 227 then
                        j = 233 - j
                        w(B, C)
                    else
                        return A
                    end
                elseif j < 199 then
                    if j > 191 then
                        q = q(o, x)
                        o = nil
                        b, q = q ~= o, not D
                        j = q and 0x180 - j or 0x39
                    else
                        j, c = 152, d["Inventory"]
                    end
                elseif j <= 201 then
                    if j <= 199 then
                        m, j, E = s._["tonumber"], 0x36, v["Scale"]
                    else
                        j, q, b = 0x14, v, s._["typeof"]
                    end
                else
                    j, l = 310 - j, l(t)
                    i = h[1][1][h[1][2]]
                    i, t = "SellRarities", i["multiHasAny"]
                end
            elseif j < 0xa3 then
                if j >= 0x95 then
                    if j <= 157 then
                        if j < 0x98 then
                            j, m = 0x62, r
                        elseif j > 152 then
                            j, q = 147, b
                        else
                            j, n = 0x126 - j, {}
                            a, A, n = c, n, s._["typeof"]
                        end
                    else
                        w = x
                        j = w and 175 or 0x12
                    end
                elseif j > 0x91 then
                    o = not q
                    j = o and 0x52b0 / j or 0x372 / j
                elseif j <= 144 then
                    j, x = 0x17, h[1][1][h[1][2]]
                    x, o = v, x["recordMutations"]
                else
                    j, m = 13, 0
                end
            elseif j >= 180 then
                if j < 185 then
                    if j > 0xb4 then
                        C = _[B]
                        j = C and 0xec or 71
                    else
                        j, a = 0xa320 / j, {}
                        n = a
                    end
                elseif j <= 0xb9 then
                    B = s._["table"]
                    j, C, w, B = 0xa40b / j, y, B["insert"], A
                else
                    j = q and 0xb2aa / j or 278 - j
                end
            elseif j < 0xaf then
                if j > 163 then
                    i, g, k = i(g)
                    i, g, k = s.b(i, g, k)
                    y, v = i(g, k)
                    k = y
                    j = k == nil and 16 or j + 0x4c
                else
                    j, z = 0x1b61 / j, s.c(z(f, _))
                end
            elseif j > 175 then
                f = h[1][1][h[1][2]]
                j, z, f = 209 - j, f["isOn"], "SellKeepMutated"
            else
                j, w = 0x12, m <= a
            end
        end
    end
end,
xa = function (e)
    return function (d)
        local f, c, _, b, a
        _ = 20
        while true do
            if _ <= 0x5a then
                if _ <= 0x14 then
                    b, _, c = d, 167, e._["tostring"]
                else
                    c = e.c(c(b, f, a))
                    return e.d(c)
                end
            else
                c = c(b)
                _, c, a, f, b = 90, c.gsub, "", "%s*%[X%d+%]%s*$", c
            end
        end
    end
end,
Fd = function (e, a)
    return function ()
        local d, c, _
        _ = 78
        repeat
            if _ > 0x4e then
                d = e.c(d(c))
                return e.d(d)
            else
                _, d = 159, a[1][1][a[1][2]]
                c, d = d, d.GetBoundingBox
            end
        until false
    end
end,
Ke = function (e, h)
    return function ()
        local a, i, c, _, d, b
        _ = 157
        while true do
            if _ >= 192 then
                if _ > 192 then
                    d(c, b, i)
                    return
                else
                    _ = _ + -90
                    d(c, b, i)
                    i, d = a["HumanoidStateType"], h[1][1][h[1][2]]
                    d, i, b, c = d.SetStateEnabled, false, i["FallingDown"], d
                end
            elseif _ <= 0x66 then
                d(c, b, i)
                i, d = a["HumanoidStateType"], h[1][1][h[1][2]]
                d, _, i, c, b = d.SetStateEnabled, 352 - _, false, d, i["PlatformStanding"]
            else
                d, a = h[1][1][h[1][2]], e._["Enum"]
                _, i = 192, a["HumanoidStateType"]
                d, b, c, i = d.SetStateEnabled, i["Ragdoll"], d, false
            end
        end
    end
end,
Gb = function (e, h)
    return function ()
        local b, i, a, _, g, c, j, k, f, d
        j = 207
        repeat
            if j >= 117 then
                if j <= 156 then
                    if j <= 0x86 then
                        if j <= 0x77 then
                            if j <= 0x75 then
                                b, j, c = d[1][d[2]]["WaterWaveSize"], 119, d[1][d[2]]["Terrain"]
                                c["WaterWaveSize"] = b
                                b, c = d[1][d[2]]["WaterReflectance"], d[1][d[2]]["Terrain"]
                                c["WaterReflectance"] = b
                            else
                                j, b, c = 0xbe, d[1][d[2]]["Effects"], e._["ipairs"]
                            end
                        else
                            d = h[2][1][h[2][2]]
                            d, j, c = d.Disconnect, j + -57, d
                        end
                    elseif j <= 0x89 then
                        a, k = c(b, i)
                        i = a
                        j = i == nil and j + 52 or 81
                    else
                        j, b = 0x2aa8 / j, d[1][d[2]]["Terrain"]
                        c = b["Parent"]
                    end
                elseif j < 0xcf then
                    if j > 0xbd then
                        c, b, i = c(b)
                        c, b, i = e.b(c, b, i)
                        a, k = c(b, i)
                        i = a
                        j = i == nil and 189 or j + -109
                    else
                        return
                    end
                elseif j > 0xcf then
                    return
                else
                    d = h[2][1][h[2][2]]
                    j = d and 134 or 72
                end
            elseif j >= 0x46 then
                if j <= 0x48 then
                    if j <= 71 then
                        if j > 70 then
                            j = 0x3f
                            c(b)
                        else
                            j = c and 0x1ffe / j or 0x77
                        end
                    else
                        d = h[1][1][h[1][2]]
                        d = {[2] = 3, [3] = d}
                        d[1] = d
                        c = not d[1][d[2]]
                        j = c and 0xde or j + -26
                    end
                elseif j <= 0x4d then
                    d(c)
                    j, d = j + -5, nil
                    h[2][1][h[2][2]] = d
                else
                    _ = h[3][1][h[3][2]]
                    _, j, f, g = k, 405 / j, _["setEffectEnabled"], true
                end
            elseif j <= 46 then
                if j <= 21 then
                    if j <= 5 then
                        j = 0x89
                        f(_, g)
                    else
                        c, j, b = e._["pcall"], j + 0x32, e:Ee{d}
                    end
                else
                    c = nil
                    h[1][1][h[1][2]], c = c, d[1][d[2]]["QualityLevel"]
                    j = c and 0x15 or 0x3f
                end
            else
                b, c = d[1][d[2]]["GlobalShadows"], h[4][1][h[4][2]]
                c["GlobalShadows"] = b
                b = d[1][d[2]]["FogEnd"]
                c["FogEnd"] = b
                c = d[1][d[2]]["Terrain"]
                j = c and j + 0x5d or 0x113a / j
            end
        until false
    end
end,
oe = function (e, h)
    return function ()
        local d, c, f, b
        b = h[2][1][h[2][2]]
        f, c = h[1][1][h[1][2]], b["Parent"]
        b = f["Character"]
        d = c == b
        return d
    end
end,
ra = function (e, h)
    return function (d, c, m)
        local _, f, g, a, i, l, k, j
        j = 39
        repeat
            if j <= 0x7d then
                if j <= 106 then
                    if j <= 39 then
                        if j > 0x13 then
                            a = h[1][1][h[1][2]]
                            j, i = 106, a["getRoot"]
                        else
                            k = h[1][1][h[1][2]]
                            j, k, _, a, f = 0x9a, d, i["Position"], k["groundedY"], c
                            _ = _.Y
                        end
                    else
                        i = i()
                        a = not i
                        j = a and 0x7d or 0x13
                    end
                else
                    a = false
                    return a
                end
            elseif j <= 236 then
                if j <= 154 then
                    a = a(k, f, _)
                    f = h[1][1][h[1][2]]
                    k, _ = f["humanoidStealMoveTo"], e._["Vector3"]
                    _, l, j, f, g = d, c, 0xf0, _["new"], a
                else
                    k = e.c(k(f, _))
                    return e.d(k)
                end
            else
                j, f = 0xec, f(_, g, l)
                _ = m
            end
        until false
    end
end,
jf = function (e, h)
    return function (d, c)
        local j, r, a, _, l, p, m, i, n, f, b, k, g
        j = 99
        while true do
            if j >= 93 then
                if j < 0xb5 then
                    if j >= 99 then
                        if j <= 99 then
                            n, f, m, _ = 0, #d, "", 1
                            a, p = f - _, _
                            j = a ~= a and 13 or 0x39
                        else
                            j = p <= 0 and 66 or 0x916c / j
                        end
                    elseif j > 0x5d then
                        r = r(l, b)
                        k, l, b, i = #c, h[3][1][h[3][2]], c, #c
                        j, g = 93, n % k
                        i = i - g
                    else
                        j, l = 7, e.c(l(b, i))
                    end
                elseif j <= 202 then
                    if j <= 0xb7 then
                        if j <= 181 then
                            j = n < a and 13 or 0xb7
                        else
                            j = p ~= p and 13 or 0xa245 / j
                        end
                    else
                        j, f = 0xe3 - j, f(e.d(_))
                        m = m .. f
                    end
                elseif j > 0xe3 then
                    j = p ~= p and 66 or 0x991c / j
                else
                    f, _, b, j, l, r = h[2][1][h[2][2]], h[1][1][h[1][2]], 1, 0x62, d, h[3][1][h[3][2]]
                    b = n + b
                end
            elseif j > 53 then
                if j >= 64 then
                    if j <= 64 then
                        j = n > a and j + -0x33 or 0x500 / j
                    else
                        j = n < a and 13 or 0x3a86 / j
                    end
                else
                    j = p > 0 and 0x35 or j + 0xb6
                end
            elseif j > 20 then
                if j <= 0x19 then
                    n = n + p
                    j = p > 0 and 64 or 0x14
                else
                    j = n > a and j + -0x28 or 0x124 - j
                end
            elseif j >= 13 then
                if j > 13 then
                    j = p <= 0 and 181 or 0xb7
                else
                    return m
                end
            else
                j, _ = 0x586 / j, e.c(_(r, e.d(l)))
            end
        end
    end
end,
sc = function (e, h)
    return function (d)
        local a, i, _, c, b
        _ = 0xba
        while true do
            if _ < 160 then
                if _ < 45 then
                    c = e.c(c(b, i, a))
                    return e.d(c)
                elseif _ > 0x2d then
                    b = h[2][1][h[2][2]]
                    a, c = h[1][1][h[1][2]], b["netCall"]
                    i = a["AssetInventory"]
                    i, _, b = d[1][d[2]], 160, i["SELL_ASSET"]
                else
                    b = b(i)
                    c = not b
                    _ = c and 185 or 155 - _
                end
            elseif _ > 185 then
                d = {[2] = 3, [3] = d}
                d[1] = d
                _, i = 0x2d, h[2][1][h[2][2]]
                i, b = d[1][d[2]], i["holdUid"]
            elseif _ > 0xa0 then
                c = false
                return c
            else
                _ = 8
                c(b, i)
                b = h[2][1][h[2][2]]
                c, i, b, a = b["waitFor"], 0.1, 2, e:_f{d, h[2]}
            end
        end
    end
end,
ic = function (e, a)
    return function ()
        local d, b, c, _
        _ = 160
        repeat
            if _ >= 95 then
                if _ > 0xa0 then
                    if _ > 0xbe then
                        return
                    else
                        _ = 0x2f8 / _
                        d(c, b)
                    end
                elseif _ <= 97 then
                    if _ <= 95 then
                        d(c, b)
                        _, d, b = 69, a[1][1][a[1][2]], false
                        d, c = d.SetHighContrast, d
                    else
                        b, d = "", a[1][1][a[1][2]]
                        d, _, c = d.SetFooterText, _ + 93, d
                    end
                else
                    d, _, b = a[1][1][a[1][2]], 95, "Comfortable"
                    d, c = d.SetDensity, d
                end
            elseif _ > 0x2c then
                d(c, b)
                c = a[1][1][a[1][2]]
                d = c["SetFooterText"]
                _ = d and 97 or 4
            elseif _ > 0x20 then
                _ = 0xef - _
                d(c, b)
            elseif _ > 4 then
                d, b = a[1][1][a[1][2]], "Made with <3 - MMB HUB"
                _, c, d = 0x2c, d, d.SetSubtitle
            else
                c = a[1][1][a[1][2]]
                d = c["SetSubtitle"]
                _ = d and 0x20 or 195
            end
        until false
    end
end,
sb = function (e)
    return function (d, c)
        local a, b, i
        a, i = c["price"], d["price"]
        b = i < a
        return b
    end
end,
za = function (e, a)
    return function ()
        local d, _, c
        _ = 109
        repeat
            if _ > 48 then
                if _ <= 0x6d then
                    c = a[1][1][a[1][2]]
                    _, c, d = 0x2c, "AutoPlaceSelected", c["isOn"]
                else
                    _, d = 0xf2 - _, d(c)
                end
            elseif _ >= 44 then
                if _ > 44 then
                    _, c = _ + 172, a[1][1][a[1][2]]
                    c, d = "AutoPlaceAll", c["isOn"]
                else
                    d = d(c)
                    _ = d and 22 or 0x840 / _
                end
            else
                return d
            end
        until false
    end
end,
La = function (e, h)
    return function (d)
        local i, c, g, b, j, a
        j = 0x5b
        repeat
            if j > 91 then
                if j > 111 then
                    j, a = 62, a()
                    b = i <= a
                else
                    g = c["Position"]
                    j, a = 179, g - d
                    i, g = a["Magnitude"], h[1][1][h[1][2]]
                    a = g["espDistanceLimit"]
                end
            elseif j < 0x45 then
                return b
            elseif j > 69 then
                b = h[1][1][h[1][2]]
                j, c = 69, b["getRoot"]
            else
                c = c()
                i = nil
                b = c ~= i
                j = b and 0x6f or 0x83 - j
            end
        until false
    end
end,
A = function (e, h)
    return function (d, c)
        local a, o, f, i, _, n, b, g, p, l, j, m
        j = 81
        while true do
            if j <= 160 then
                if j < 98 then
                    if j >= 81 then
                        if j > 81 then
                            return d
                        else
                            j = c and 0x5a or 118
                        end
                    elseif j > 0x37 then
                        f = e.c(f(_, o, e.d(l)))
                        return e.d(f)
                    else
                        m, n, a, p = m()
                        o = e._["math"]
                        _ = o["huge"]
                        f = m == _
                        j = f and 0xa0 or 0x109 - j
                    end
                elseif j <= 125 then
                    if j > 118 then
                        j, _ = 0x2fda / j, _(o, l, b)
                        b, o = e._["math"], d.Y
                        i, l, b, g = a, b["clamp"], d.Z, p
                    elseif j > 98 then
                        n = h[1][1][h[1][2]]
                        j, m = 55, n["getCorridorBounds"]
                    else
                        j, l = 0xa1 - j, e.c(l(b, i, g))
                    end
                else
                    j = f and 322 - j or 0xc8
                end
            elseif j > 0xd2 then
                if j > 226 then
                    j = f and j + -8 or 191
                elseif j > 224 then
                    j, f = j + 6, a > p
                else
                    return d
                end
            elseif j >= 200 then
                if j > 200 then
                    j, l = 0xa0, e._["math"]
                    o = l["huge"]
                    _ = -o
                    f = n == _
                else
                    j, f = 0xa2, m > n
                end
            elseif j <= 162 then
                j = f and j + 0x46 or 0x8f04 / j
            else
                _ = e._["Vector3"]
                o, f = e._["math"], _["new"]
                o, l, b, j, _ = d.X, m, n, 125, o["clamp"]
            end
        end
    end
end,
Ad = function (e, h)
    return function ()
        local c, f, d, _, b
        _ = 193
        while true do
            if _ < 193 then
                d(c, b, f)
                return
            else
                f, _, d = e._["game"], 0xac, h[2][1][h[2][2]]
                b, f, d, c = f["PlaceId"], h[1][1][h[1][2]], d.Teleport, d
            end
        end
    end
end,
ff = function (e, a)
    return function ()
        local c, _, d
        _ = 8
        repeat
            if _ <= 8 then
                d = a[1][1][a[1][2]]
                _, d, c = 112, d.Disconnect, d
            else
                d(c)
                return
            end
        until false
    end
end,
O = function (e, h)
    return function (d, c)
        local _, m, i, k, g, f, j, a
        j = 176
        repeat
            if j >= 0x67 then
                if j >= 177 then
                    if j > 208 then
                        j, m = 31, m(i)
                        k, i = h[1][1][h[1][2]], e._["ipairs"]
                        k, a = c, k["recordMutations"]
                    elseif j > 177 then
                        i, a, k = i(e.d(a))
                        i, a, k = e.b(i, a, k)
                        f, _ = i(a, k)
                        k = f
                        j = k == nil and 2 or j + -205
                    else
                        m = true
                        return m
                    end
                elseif j >= 119 then
                    if j <= 0x77 then
                        g = true
                        return g
                    else
                        a = h[1][1][h[1][2]]
                        j, i, a = 51, a["multiHasAny"], d
                    end
                else
                    j, i = 0xd4, h[1][1][h[1][2]]
                    i, m = d, i["multiSelected"]
                end
            elseif j < 4 then
                if j <= 2 then
                    i = false
                    return i
                else
                    g = m[_]
                    j = g and 0x77 or 4
                end
            elseif j < 31 then
                f, _ = i(a, k)
                k = f
                j = k == nil and 6 - j or 3
            elseif j <= 31 then
                j, a = 0xef - j, e.c(a(k))
            else
                i = i(a)
                m = not i
                j = m and 228 - j or 103
            end
        until false
    end
end,
ud = function (e, a)
    return function ()
        local d, c, _
        _ = 7
        repeat
            if _ <= 7 then
                d = a[1][1][a[1][2]]
                c, _, d = d, 11, d.Cancel
            else
                d(c)
                return
            end
        until false
    end
end,
Hc = function (e, h)
    return function (d, c)
        local b, i, g, j, a
        j = 0xb2
        repeat
            if j <= 161 then
                if j >= 0x86 then
                    if j > 0x86 then
                        b, i = b(i)
                        a = b
                        j = a and 208 or 48
                    else
                        return i
                    end
                elseif j <= 48 then
                    j = a and 0x1920 / j or j + 33
                else
                    return c
                end
            elseif j > 0xb2 then
                g = nil
                j, a = 256 - j, i ~= g
            else
                d = {[2] = 3, [3] = d}
                j, d[1] = 0xa1, d
                b, i = e._["pcall"], e:df{d, h[1]}
            end
        until false
    end
end,
_ = getfenv(), We = function (e, h)
    return function ()
        local c, j, b, a, d, f, k, i
        j = 49
        repeat
            if j <= 0x5f then
                if j < 0x34 then
                    if j > 0x28 then
                        c = h[1][1][h[1][2]]
                        j, d = 40, c["getRoot"]
                    elseif j > 0x1c then
                        d = d()
                        h[2][1][h[2][2]] = d
                        d = h[2][1][h[2][2]]
                        j = d and 0x6c or j + 12
                    else
                        j = j + 24
                        c(b, e.d(i))
                    end
                elseif j > 72 then
                    d = true
                    return d
                elseif j >= 0x3b then
                    if j > 0x3b then
                        d = d(c, b, i)
                        b = h[1][1][h[1][2]]
                        a, c, b = e._["CFrame"], b["placeRoot"], h[2][1][h[2][2]]
                        j, k, i = 147, h[5][1][h[5][2]], a["new"]
                        f, k, a = h[5][1][h[5][2]], d, k.X
                        f = f.Z
                    else
                        b, c = true, h[3][1][h[3][2]]
                        d = c == b
                        return d
                    end
                else
                    j, b = 0x3330 / j, h[1][1][h[1][2]]
                    c = b["stealingEnabled"]
                end
            elseif j >= 0xab then
                if j >= 0xcb then
                    if j > 203 then
                        c = c()
                        d = not c
                        j = d and 347 - j or 129
                    else
                        j, c = 171, h[1][1][h[1][2]]
                        c, d = h[4][1][h[4][2]], c["tryCarryEgg"]
                    end
                else
                    j = j + -112
                    d(c)
                end
            elseif j >= 0x81 then
                if j <= 129 then
                    c = h[3][1][h[3][2]]
                    d = not c
                    j = d and 0xcb or 188 - j
                else
                    j, i = 0x1c, e.c(i(a, k, f))
                end
            else
                c = h[1][1][h[1][2]]
                b, d = h[5][1][h[5][2]], c["groundedY"]
                i, c = b, b.X
                i, j, b = i.Y, 0x1e60 / j, i.Z
            end
        until false
    end
end,
ke = function (e, h)
    return function ()
        local c, i, g, d, a, _, b
        _ = 0xee
        repeat
            if _ >= 0x8c then
                if _ > 224 then
                    if _ > 234 then
                        c = h[1][1][h[1][2]]
                        _, b, d = 140, c, c["resolveWaypoint"]
                        b, i, c = "WaypointTarget", "Base", b["optionValue"]
                    else
                        return
                    end
                elseif _ < 0xc5 then
                    _, c = _ + -15, e.c(c(b, i))
                elseif _ > 197 then
                    _ = 0x1ca - _
                    c(b, i, a, g)
                else
                    _, b = 0xac60 / _, h[1][1][h[1][2]]
                    a, i, g, b, c = "Error", "Teleport failed", 3, "Waypoint", b["notify"]
                end
            elseif _ > 76 then
                if _ <= 125 then
                    d = d(e.d(c))
                    c = not d
                    _ = c and 0x1676 / _ or 0x31
                else
                    b = b(i, a)
                    c = not b
                    _ = c and 0xc5 or 0x7a7c / _
                end
            elseif _ <= 49 then
                if _ > 46 then
                    i = h[1][1][h[1][2]]
                    b, _, a, i = i["travelTo"], 134, true, d
                else
                    _, b = 76, h[1][1][h[1][2]]
                    b, c, i, a, g = "Waypoint", b["notify"], "Not available right now", "Warning", 3
                end
            else
                c(b, i, a, g)
                return
            end
        until false
    end
end,
Rc = function (s, h)
    return function ()
        local c, g, r, a, f, k, n, q, p, _, j, l, b, m, d, i
        j = 0xa5
        while true do
            if j >= 0x79 then
                if j > 0xdc then
                    if j < 242 then
                        if j <= 225 then
                            if j > 222 then
                                b = h[5][1][h[5][2]]
                                l = b[r]
                                b = l
                                j = b and j + -0x98 or 0x6a59 / j
                            else
                                c = c(m)
                                m = d["TrailInventory"]
                                j = m and 242 or 339 - j
                            end
                        else
                            return n
                        end
                    elseif j >= 0xf4 then
                        if j <= 0xf4 then
                            d = d()
                            c = not d
                            j = c and 0x59 or 220
                        else
                            _, r = a(p, f)
                            f = _
                            j = f == nil and 239 or 0xc8
                        end
                    else
                        a, j, n, p = s._["ipairs"], 0x29, false, h[1][1][h[1][2]]
                    end
                elseif j < 0xc8 then
                    if j >= 179 then
                        if j <= 0xb3 then
                            j, i = 0x3b6f / j, m
                        else
                            j, i = 31, d
                        end
                    elseif j <= 0x79 then
                        j = b and 0x809 / j or 255
                    else
                        j, c = 0xf4, h[2][1][h[2][2]]
                        d = c["getSave"]
                    end
                elseif j <= 0xd4 then
                    if j >= 0xce then
                        if j <= 206 then
                            c = false
                            return c
                        else
                            m = h[2][1][h[2][2]]
                            c, j, m = m["multiSelected"], 222, "TrailWanted"
                        end
                    else
                        l = c[r]
                        j = l and 0xafc8 / j or 0xc738 / j
                    end
                else
                    j, n = 10, h[2][1][h[2][2]]
                    m, n = n["multiHasAny"], "TrailWanted"
                end
            elseif j >= 0x1f then
                if j > 85 then
                    if j <= 0x66 then
                        if j <= 89 then
                            j = c and 0x127 - j or 0xd4
                        else
                            i = d["Money"]
                            j = i >= b and 0x13 or 357 - j
                        end
                    else
                        n = {}
                        j, m = 0x167 - j, n
                    end
                elseif j < 73 then
                    if j > 31 then
                        a, p, f = a(p)
                        a, p, f = s.b(a, p, f)
                        _, r = a(p, f)
                        f = _
                        j = f == nil and 0x2647 / j or 200
                    else
                        d = i
                        i = d["TrailInventory"]
                        j = i and j + 0x36 or j + 0x94
                    end
                elseif j <= 0x49 then
                    j, i = j + 48, m[l]
                    b = not i
                else
                    j, m = 0xff, i
                end
            elseif j > 0x11 then
                if j < 0x13 then
                    i(g)
                    g = h[2][1][h[2][2]]
                    j, i = 3, g["getSave"]
                elseif j > 19 then
                    i(g, k)
                    j, g, n = 18, s._["task"], true
                    g, i = 0.35, g["wait"]
                else
                    j, g = 0x14, h[2][1][h[2][2]]
                    q, i = h[4][1][h[4][2]], g["netCall"]
                    k = q["Trails"]
                    g, k = k["REQUEST_PURCHASE"], l
                end
            elseif j <= 12 then
                if j > 10 then
                    j, b = 102, 0
                elseif j > 3 then
                    m = m(n)
                    j, c = 0x37a / j, not m
                else
                    i = i()
                    j = i and 0x1f or 0xc0
                end
            else
                i = h[3][1][h[3][2]]
                b = i[r]
                j = b and 119 - j or 12
            end
        end
    end
end,
Lb = function (e, a)
    return function ()
        local d, _, c
        _ = 0x16
        while true do
            if _ > 0xa2 then
                if _ <= 239 then
                    _ = 240
                    d(c)
                else
                    _, d = _ + -0x4e, nil
                    c, a[2][1][a[2][2]] = a[1][1][a[1][2]], d
                    c, d = a[3][1][a[3][2]], c["clearTable"]
                end
            elseif _ >= 33 then
                if _ <= 33 then
                    c, _, d = e:Ge{a[2]}, 0xef, e._["pcall"]
                else
                    d(c)
                    return
                end
            else
                d = a[2][1][a[2][2]]
                _ = d and 33 or 240
            end
        end
    end
end,
bf = function (e, h)
    return function ()
        local c, b, i, d, _, a
        _ = 0x89
        repeat
            if _ < 137 then
                c = c(b, i)
                b = true
                d = c == b
                h[2][1][h[2][2]] = d
                return
            else
                _, b = 14, h[1][1][h[1][2]]
                c, i, a, b = b["RequestPlaceEgg"], h[3][1][h[3][2]], h[4][1][h[4][2]], h[5][1][h[5][2]]
                i = i[a]
            end
        until false
    end
end,
ib = function (s, h)
    return function (d)
        local a, b, i, f, l, q, k, n, p, c, m, j, _, g, r
        j = 189
        while true do
            if j < 131 then
                if j >= 54 then
                    if j < 0x55 then
                        if j > 0x4a then
                            if j <= 76 then
                                return
                            else
                                f = f(_)
                                j = f and j + 0xa6 or 242
                            end
                        elseif j < 0x48 then
                            g = h[3][1][h[3][2]]
                            i = not g
                            j = i and 5 or 0xb9
                        elseif j <= 72 then
                            j, r = j + 141, h[2][1][h[2][2]]
                            l, _, r = true, r["travelTo"], p
                        else
                            f = h[2][1][h[2][2]]
                            j, p = 1, f["getFuseMachinePosition"]
                        end
                    elseif j >= 115 then
                        if j <= 0x80 then
                            if j <= 0x73 then
                                j = f and 0x6d29 / j or 0x728d / j
                            else
                                g = g()
                                j, i = 0x85 - j, not g
                            end
                        else
                            j = p and 0x159 - j or 0x2594 / j
                        end
                    elseif j >= 94 then
                        if j <= 0x5e then
                            j, a = 179 - j, h[2][1][h[2][2]]
                            a, n = "FuseAutoReveal", a["isOn"]
                        else
                            i(g, k)
                            j, g = 0x33af / j, s._["task"]
                            g, i = 0.2, g["wait"]
                        end
                    else
                        n = n(a)
                        j = n and j + -0x41 or 47
                    end
                elseif j > 0x20 then
                    if j <= 0x2a then
                        if j < 0x27 then
                            f(_)
                            f = true
                            return f
                        elseif j > 0x27 then
                            c = c()
                            m = not c
                            j = m and 0x51 - j or j + 163
                        else
                            return
                        end
                    elseif j > 46 then
                        j, a = j + -0x1b, true
                        n = d[1][d[2]] == a
                    else
                        j, p = 228 - j, h[2][1][h[2][2]]
                        p, f, a = c, n, p["fusePrice"]
                    end
                elseif j > 8 then
                    if j > 0x14 then
                        g = h[2][1][h[2][2]]
                        q, i = h[1][1][h[1][2]], g["netInvoke"]
                        k = q["FuseMachine"]
                        g, j, k = k["INSERT_MOB"], j + 0x45, b
                    else
                        j = n and 253 - j or 7
                    end
                elseif j < 7 then
                    if j > 1 then
                        j = i and j + 143 or 0x20
                    else
                        p = p()
                        f = p
                        j = f and 0x48 or 115
                    end
                elseif j <= 7 then
                    return
                else
                    _ = h[2][1][h[2][2]]
                    f, r = _["netInvoke"], h[1][1][h[1][2]]
                    j, _ = j + 28, r["FuseMachine"]
                    _ = _["START_FUSE"]
                end
            elseif j < 0xd7 then
                if j > 0xb9 then
                    if j <= 204 then
                        if j > 0xc3 then
                            n = n(a)
                            a = not n
                            j = a and 0x3c90 / j or 46
                        elseif j > 0xbd then
                            f, _, r = f(_)
                            f, _, r = s.b(f, _, r)
                            l, b = f(_, r)
                            r = l
                            j = r == nil and 8 or 0xf9 - j
                        else
                            j, d = 42, {[2] = 3, [3] = d}
                            d[1] = d
                            m = h[2][1][h[2][2]]
                            c = m["getSave"]
                        end
                    elseif j <= 0xcd then
                        n, a, m = c["FusionLocked"], true, s:pe{h[2], d}
                        j = n == a and 0x12b - j or 133
                    else
                        j, _ = j + -98, _(r, l)
                        f = not _
                    end
                elseif j >= 148 then
                    if j < 0xb6 then
                        return
                    elseif j > 0xb6 then
                        j, g = j + -0x39, m
                    else
                        a = a(p, f)
                        p = a
                        j = p and j + 38 or 0x138 - j
                    end
                elseif j >= 133 then
                    if j <= 0x85 then
                        j, a = 0x69fc / j, h[2][1][h[2][2]]
                        a, n = c, a["pickFuseGroup"]
                    else
                        j = 0xd9
                        f(_)
                    end
                else
                    j = j + 109
                    i(g)
                end
            elseif j > 235 then
                if j >= 243 then
                    if j <= 0xf7 then
                        if j <= 0xf3 then
                            return
                        else
                            j, p = 0x82, f < a
                        end
                    else
                        _, f = true, c["FusionInfoAcknowledged"]
                        j = f ~= _ and 0x1da - j or 472 - j
                    end
                elseif j > 0xf0 then
                    j, f = 0xf7, 0
                else
                    l, b = f(_, r)
                    r = l
                    j = r == nil and j + -232 or 0x126 - j
                end
            elseif j > 220 then
                if j <= 233 then
                    j, a = 0xeb, h[2][1][h[2][2]]
                    p, n = h[1][1][h[1][2]], a["netInvoke"]
                    a = p["FuseMachine"]
                    a = a["COMPLETE_REVEAL"]
                else
                    j = 242 - j
                    n(a)
                end
            elseif j < 0xdb then
                if j <= 215 then
                    return
                else
                    j, _, f = 195, n, s._["ipairs"]
                end
            elseif j <= 219 then
                _ = h[2][1][h[2][2]]
                r, j, f = h[1][1][h[1][2]], 0x86, _["netInvoke"]
                _ = r["FuseMachine"]
                _ = _["ACKNOWLEDGE_INFO"]
            else
                j, f, _ = j + -0x8b, s._["tonumber"], c["Money"]
            end
        end
    end
end,
Pe = function (e)
    return function ()
        local i, d, a, j, f, c, b, k
        j = 0x89
        repeat
            if j > 121 then
                if j <= 137 then
                    b, d = "VirtualInputManager", e._["game"]
                    c, j, d = d, 0x79, d.GetService
                else
                    c(b, i, a, k, f)
                    return
                end
            elseif j < 0x3d then
                c(b, i, a, k, f)
                j, b = 244 / j, e._["task"]
                b, c = 0.05, b["wait"]
            elseif j > 61 then
                j, d = 484 / j, d(c, b)
                f, i = e._["Enum"], true
                k = f["KeyCode"]
                k, b, a, f, c = false, d, k["Space"], e._["game"], d.SendKeyEvent
            else
                c(b)
                i, f = false, e._["Enum"]
                k = f["KeyCode"]
                b, j, f, k, c, a = d, j + 0xb6, e._["game"], i, d.SendKeyEvent, k["Space"]
            end
        until false
    end
end,
Cb = function (s, h)
    return function ()
        local n, c, l, _, t, g, f, j, d, p, a, u, r, m, i, o, e, k
        j = 194
        repeat
            if j <= 0x92 then
                if j <= 0x48 then
                    if j <= 33 then
                        if j < 0x14 then
                            if j > 8 then
                                j = i and 140 - j or 0xc72 / j
                            elseif j > 5 then
                                j, f, _ = 0x59, s._["ipairs"], p["data"]
                            else
                                g, j, k = s._["typeof"], 0x168 / j, t["id"]
                            end
                        elseif j < 0x1e then
                            if j > 20 then
                                j, r, _ = 0x1bde / j, p["nextPageCursor"], s._["typeof"]
                            else
                                g, j, k = s._["tonumber"], 0xdc, t["maxPlayers"]
                            end
                        elseif j <= 0x1e then
                            j, i = 0x258 / j, 0
                        else
                            j, g = 35, 0
                        end
                    elseif j >= 0x3f then
                        if j <= 66 then
                            if j <= 0x3f then
                                j = j + 43
                                k(u, o)
                            else
                                j = a > 0 and 84 or 0x166e / j
                            end
                        else
                            g = g(k)
                            k = "string"
                            j, i = 0x12, g == k
                        end
                    elseif j >= 39 then
                        if j > 39 then
                            j, f = 0x86 - j, p["nextPageCursor"]
                        else
                            g, j, i = t["playing"], 0x20e8 / j, s._["tonumber"]
                        end
                    else
                        u = 0
                        k = g > u
                        j = k and 0xd4 or 0xd66 / j
                    end
                elseif j <= 110 then
                    if j < 89 then
                        if j > 84 then
                            j = a ~= a and 0xff or 0x4f2f / j
                        elseif j <= 0x4a then
                            j = f and 214 or 241
                        else
                            j = m > n and 0x89 or 87
                        end
                    elseif j > 0x6a then
                        m(n, a)
                        return c
                    elseif j > 0x62 then
                        l, t = f(_, r)
                        r = l
                        j = r == nil and 29 or 252
                    elseif j <= 89 then
                        f, _, r = f(_)
                        f, _, r = s.b(f, _, r)
                        l, t = f(_, r)
                        r = l
                        j = r == nil and 118 - j or 0x579c / j
                    else
                        j = k and 0x159 - j or 106
                    end
                elseif j <= 0x89 then
                    if j >= 123 then
                        if j <= 123 then
                            j = a <= 0 and j + 0x62 or 182
                        else
                            n = s._["table"]
                            m, a, j, n = n["sort"], s:Ce(), j + -27, c
                        end
                    else
                        g, j, u = t["id"], 0x12b - j, s._["game"]
                        k = u["JobId"]
                        i = g ~= k
                    end
                elseif j <= 142 then
                    u, k = t["id"], h[1][1][h[1][2]]
                    j, g = j + 4, k[u]
                    i = not g
                else
                    j = i and 0x27 or 0x6a
                end
            elseif j >= 215 then
                if j < 0xf1 then
                    if j > 221 then
                        if j > 222 then
                            j = a <= 0 and 488 - j or 215
                        else
                            m = m + a
                            j = a > 0 and 0x8b9e / j or 0x7b
                        end
                    elseif j > 220 then
                        j = m < n and 0x7645 / j or 0xb6
                    elseif j >= 216 then
                        if j <= 0xd8 then
                            i = i(g)
                            j = i and 236 - j or 30
                        else
                            g = g(k)
                            j = g and 35 or 253 - j
                        end
                    else
                        j, f = 147, h[2][1][h[2][2]]
                        p, f = f["fetchServerPage"], d
                    end
                elseif j <= 0xf7 then
                    if j <= 0xf6 then
                        if j > 243 then
                            _ = _(r)
                            r = "string"
                            f = _ == r
                            j = f and 0x3c or j + -172
                        elseif j > 0xf1 then
                            j, _ = 165, s._["task"]
                            f, _ = _["wait"], 0.25
                        else
                            j, f = 0x1c7 - j, nil
                        end
                    else
                        u = s._["table"]
                        u, k, o, e = c, u["insert"], {}, t["id"]
                        j, o["id"] = 0x3f, e
                        o["playing"] = i
                    end
                elseif j <= 252 then
                    j, k, g = 0xc6, t, s._["typeof"]
                else
                    j = m < n and j + -118 or 470 - j
                end
            elseif j >= 0xb1 then
                if j < 198 then
                    if j >= 0xb6 then
                        if j > 182 then
                            m, d = {}, nil
                            n, m, c = 4, 1, m
                            a = m
                            j = n ~= n and 137 or 0x42
                        else
                            j = a ~= a and 0x89 or j + 0x21
                        end
                    else
                        j = i and 0x622e / j or 0x143 - j
                    end
                elseif j >= 212 then
                    if j > 0xd4 then
                        d = f
                        f = not d
                        j = f and j + -0x3b or 0xa9
                    else
                        j, k = 0x62, i < g
                    end
                else
                    g = g(k)
                    k = "table"
                    i = g == k
                    j = i and 0xcb - j or 0xdec / j
                end
            elseif j > 0xa1 then
                if j <= 0xa5 then
                    j = 0xde
                    f(_)
                else
                    j, _, r = 155, #c, 40
                    f = _ >= r
                end
            elseif j > 155 then
                j = m > n and 0x5629 / j or 123
            elseif j <= 0x93 then
                p = p(f)
                f = not p
                j = f and 137 or 0x498 / j
            else
                j = f and 137 or 243
            end
        until false
    end
end,
zf = {}, v = function (e)
    return function (d, ...)
        local n, m, l, c, j, a, g, _, f, k
        j = 196
        while true do
            if j >= 177 then
                if j < 227 then
                    if j >= 192 then
                        if j > 0xc0 then
                            j, c, m = 0x3d, e._["typeof"], d
                        else
                            f, _ = n(a, k)
                            k = f
                            j = k == nil and 0xabc0 / j or 4
                        end
                    else
                        n, a, k = n(a)
                        n, a, k = e.b(n, a, k)
                        f, _ = n(a, k)
                        k = f
                        j = k == nil and 229 or j + -173
                    end
                elseif j < 229 then
                    g = g(l)
                    l = "table"
                    j = g ~= l and j + -53 or j + -168
                elseif j <= 0xe5 then
                    return m
                else
                    c = nil
                    return c
                end
            elseif j <= 59 then
                if j >= 0x27 then
                    if j <= 0x27 then
                        n, j, m = e.c(...), 177, {}
                        e.e(m, 1, e.d(n))
                        c, m, n = m, d, e._["ipairs"]
                        a = c
                    else
                        j, m = 0x2c40 / j, m[_]
                    end
                else
                    g, j, l = e._["typeof"], 0xe3, m
                end
            elseif j > 0x3d then
                g = nil
                return g
            else
                c = c(m)
                m = "table"
                j = c ~= m and 0x396d / j or 0x94b / j
            end
        end
    end
end,
db = function (s, G)
    return function ()
        local y, J, z, f, b, H, a, C, D, E, w, N, p, I, g, k, c, F, x, _, M, v, t, B, j, O, m, n, A, u, i, K, e, l, L, o, r, q
        I = 0xca
        repeat
            if I > 160 then
                if I < 239 then
                    if I < 0xca then
                        if I >= 181 then
                            if I < 0xbe then
                                if I > 0xb8 then
                                    if I > 186 then
                                        I = 0x39
                                        B(C, e)
                                        e, u = {}, "ESP"
                                        e["Title"] = u
                                        u = "eye"
                                        e["Icon"] = u
                                        B, C = a.AddSection, a
                                    else
                                        H = H(L, _)
                                        r, l = {}, "Session"
                                        r["Title"] = l
                                        I, l = 0xbf - I, "activity"
                                        r["Icon"] = l
                                        _, L = M, M.AddSection
                                    end
                                elseif I < 182 then
                                    q(o, x)
                                    J, I, x = "Hop Now", 242, {}
                                    x["Title"] = J
                                    J = "Hop"
                                    x["Text"] = J
                                    J = "shuffle"
                                    x["Icon"] = J
                                    E, w, p, B, C = {}, "hop", "server", "switch", "new server"
                                    E[1], E[2], E[3], E[4] = p, w, B, C
                                    J = E
                                    x["Keywords"] = J
                                    J = s:Jd{G[2], G[0x1e]}
                                    x["Callback"] = J
                                    o, q = k, k.AddButton
                                elseif I > 0xb6 then
                                    J(E, p)
                                    p, w = {}, "Upgrades"
                                    p["Title"] = w
                                    I, w = 247, "arrow-big-up"
                                    p["Icon"] = w
                                    E, J = n, n.AddSection
                                else
                                    B(C, e)
                                    u, e = "AutoClaimIndex", {}
                                    I, e["Id"] = 0xf9, u
                                    u = "Auto Claim Index"
                                    e["Title"] = u
                                    u = "book-check"
                                    e["Icon"] = u
                                    u = false
                                    e["Default"] = u
                                    C, B = E, E.AddToggle
                                end
                            elseif I > 0xc4 then
                                if I <= 0xc5 then
                                    p = p(w, B)
                                    e, I, C = "Training", I + -40, {}
                                    C["Title"] = e
                                    e = "dumbbell"
                                    C["Icon"] = e
                                    w, B = n.AddSection, n
                                else
                                    i = i(F, k)
                                    y, v = {}, "Egg Handling"
                                    y["Title"] = v
                                    v = "refresh-cw"
                                    y["Icon"] = v
                                    v = "Place, hatch and sell eggs"
                                    I, y["Description"] = I + -0x55, v
                                    F, k = c.AddSection, c
                                end
                            elseif I <= 194 then
                                if I > 0xbe then
                                    J(E, p)
                                    p, I, w = {}, 180, "FuseAutoReveal"
                                    p["Id"] = w
                                    w = "Auto Complete Reveal"
                                    p["Title"] = w
                                    w = true
                                    p["Default"] = w
                                    J, E = o.AddToggle, o
                                else
                                    B(C, e)
                                    u, e = "AutoBuyTrail", {}
                                    e["Id"] = u
                                    u = "Auto Buy Trail"
                                    e["Title"] = u
                                    u = "shopping-bag"
                                    e["Icon"] = u
                                    I, u = 246 - I, false
                                    e["Default"] = u
                                    C, B = p, p.AddToggle
                                end
                            else
                                B(C, e)
                                e, u = {}, "AutoTreadmill"
                                e["Id"] = u
                                u = "Auto Treadmill Training"
                                e["Title"] = u
                                u = "dumbbell"
                                e["Icon"] = u
                                I, u = 0xbc, false
                                e["Default"] = u
                                C, B = w, w.AddToggle
                            end
                        elseif I > 0xac then
                            if I > 178 then
                                J(E, p)
                                w, p = "FuseMaxScale", {}
                                p["Id"] = w
                                w = "Maximum Scale to Fuse"
                                p["Title"] = w
                                w = 0
                                p["Min"] = w
                                w = 10
                                p["Max"] = w
                                I, p["Default"] = 0x567c / I, w
                                w = 0.1
                                p["Step"] = w
                                E, J = o, o.AddSlider
                            elseif I <= 0xb0 then
                                if I <= 0xae then
                                    I = 0x196 - I
                                    v(D, b)
                                    q, b = "Target filters", {}
                                    b["Title"] = q
                                    v, D = i.AddDivider, i
                                else
                                    j(m, N)
                                    f, N = "Library Dev", {}
                                    N["Title"] = f
                                    f = "MMB HUB"
                                    N["Content"] = f
                                    I, f = 0x3c9 - I, "globe"
                                    N["Icon"] = f
--===== [Credits] About page entries =====
                                    j, m = z.AddParagraph, z
                                end
                            else
                                u(g, O)
                                z, O = "EspPets", {}
                                O["Id"] = z
                                z = "Pet ESP"
                                O["Title"] = z
                                I, z = 0x258c / I, false
                                O["Default"] = z
                                g, u = B, B.AddToggle
                            end
                        elseif I > 169 then
                            if I <= 0xab then
                                e = e(u, g)
                                z, O = "EspWorldEggs", {}
                                I, O["Id"] = I + -20, z
                                z = "World Egg ESP"
                                O["Title"] = z
                                z = "egg"
                                O["Icon"] = z
                                z = false
                                O["Default"] = z
                                g, u = B, B.AddToggle
                            else
                                i(F, k)
                                k, y = {}, "Place Eggs"
                                k["Title"] = y
                                y = "Place"
                                k["Text"] = y
                                y = "package"
                                k["Icon"] = y
                                y = s:Td{G[0x1e]}
                                k["Callback"] = y
                                I, F, i = 39, r, r.AddButton
                            end
                        elseif I > 0xa8 then
                            D = D(b, q)
                            I, D = I + 77, {[2] = 3, [3] = D}
                            D[1] = D
                            b = s:Xd{D}
                            x, q = G[0x1e][1][G[0x1e][2]], b
                            x, o, J = "HopMode", x["optionValue"], "No Matching Eggs"
                        elseif I <= 166 then
                            if I > 162 then
                                M = M(c, A)
                                a, c, n = "farm", G[12][1][G[12][2]], {}
                                n["Id"] = a
                                a = "Farm"
                                I, n["Title"] = I + 0x3d, a
                                a = "egg"
                                n["Icon"] = a
                                c, A = c.AddTab, c
                            else
                                v(D, b)
                                q, b = "AutoServerHop", {}
                                b["Id"] = q
                                q = "Auto Server Hop"
                                b["Title"] = q
                                q = "server"
                                b["Icon"] = q
                                q = false
                                I, b["Default"] = 58, q
                                D, v = k, k.AddToggle
                            end
                        else
                            i(F, k)
                            I, k, y = 150, {}, "Filters"
                            k["Title"] = y
                            y = "Empty multi-select filters mean everything matches."
                            k["Content"] = y
                            y = "filter"
                            k["Icon"] = y
                            F, i = l, l.AddParagraph
                        end
                    elseif I < 222 then
                        if I < 210 then
                            if I >= 205 then
                                if I >= 0xce then
                                    if I > 0xce then
                                        j(m, N)
                                        f, N = "Unload Script", {}
                                        N["Title"] = f
                                        f = "Unload"
                                        N["Text"] = f
                                        f = "power"
                                        N["Icon"] = f
                                        f = "Danger"
                                        I, N["Variant"] = 210, f
                                        f = s:Wd{G[30], G[12]}
                                        N["Callback"] = f
                                        m, j = z, z.AddButton
                                    else
                                        I = 131
                                        p(w, B)
                                    end
                                else
                                    t = t(i, F)
                                    k, G[31][1][G[31][2]], F = "Current Job", t, {}
                                    F["Title"] = k
                                    k = "Idle"
                                    F["Value"] = k
                                    k = "Neutral"
                                    F["Status"] = k
                                    I, i, t = I + -0x87, L, L.AddStatus
                                end
                            elseif I > 0xca then
                                J(E, p)
                                p, w = {}, "AutoDeleteOwnPets"
                                p["Id"] = w
                                I, w = 0xb336 / I, "Hide Own Pet Renders"
                                p["Title"] = w
                                w = "Removes your own pet models locally to reduce clutter"
                                p["Description"] = w
                                w = false
                                p["Default"] = w
                                E, J = q, q.AddToggle
                            else
                                A, M, n = {}, G[12][1][G[12][2]], "home"
                                A["Id"] = n
                                n = "Home"
                                I, A["Title"] = 166, n
                                n = "home"
                                A["Icon"] = n
                                M, c = M.AddTab, M
                            end
                        elseif I <= 0xd7 then
                            if I >= 212 then
                                if I > 0xd4 then
                                    v(D, b)
                                    q, b = "LifecycleMutations", {}
                                    b["Id"] = q
                                    q = "Lifecycle Mutations"
                                    b["Title"] = q
                                    q = G[14][1][G[14][2]]
                                    b["Options"] = q
                                    q = true
                                    b["Multi"] = q
                                    b["Searchable"] = q
                                    o = {}
                                    q = o
                                    b["Default"] = q
                                    I, v, D = 252, F.AddDropdown, F
                                else
                                    u(g, O)
                                    O, z = {}, "JumpPowerEnabled"
                                    O["Id"] = z
                                    I, z = 0xef, "Jump Power Override"
                                    O["Title"] = z
                                    z = false
                                    O["Default"] = z
                                    u, g = C.AddToggle, C
                                end
                            else
                                j(m, N)
                                return
                            end
                        elseif I <= 0xda then
                            I, y = 0x6e, y(s.d(v))
                            k["Value"] = y
                            y = "Neutral"
                            k["Status"] = y
                            y = "egg"
                            k["Icon"] = y
                            F, i = _, _.AddStatus
                        else
                            B = {}
                            I, B["Id"] = 98, E
                            e = s._["string"]
                            e, u, C = "Priority %d", J, e["format"]
                        end
                    elseif I >= 232 then
                        if I >= 235 then
                            if I < 0xed then
                                J(E, p)
                                w, p = "FuseKeepEquipped", {}
                                I, p["Id"] = 0xc2, w
                                w = "Never Fuse Equipped"
                                p["Title"] = w
                                w = true
                                p["Default"] = w
                                E, J = o, o.AddToggle
                            elseif I > 237 then
                                J(E, p)
                                w, I, p = "Fuse Now", I + -0x75, {}
                                p["Title"] = w
                                w = "Fuse"
                                p["Text"] = w
                                w = "combine"
                                p["Icon"] = w
                                w = s:Ld{G[0x1e]}
                                p["Callback"] = w
                                E, J = o, o.AddButton
                            else
                                v(D, b)
                                b, q = {}, "AutoDropEgg"
                                b["Id"] = q
                                q = "Auto Drop Held Egg"
                                b["Title"] = q
                                I, q = 33, "package-x"
                                b["Icon"] = q
                                q = false
                                b["Default"] = q
                                v, D = i.AddToggle, i
                            end
                        elseif I <= 0xe8 then
                            v(D, b)
                            q, b = "StealZones", {}
                            I, b["Id"] = 75, q
                            q = "Areas"
                            b["Title"] = q
                            q = "Empty = all areas"
                            b["Description"] = q
                            q = G[10][1][G[10][2]]
                            b["Options"] = q
                            q = true
                            b["Multi"] = q
                            b["Searchable"] = q
                            o = {}
                            q = o
                            b["Default"] = q
                            D, v = i, i.AddDropdown
                        else
                            u(g, O)
                            O, z = {}, "WalkSpeed"
                            I, O["Id"] = 0xd4, z
                            z = "Walk Speed"
                            O["Title"] = z
                            z = 0x10
                            O["Min"] = z
                            z = 500
                            O["Max"] = z
                            z = 0x20
                            O["Default"] = z
                            z = 1
                            O["Step"] = z
                            z = true
                            O["ValueInput"] = z
                            u, g = C.AddSlider, C
                        end
                    elseif I > 0xe2 then
                        if I > 0xe3 then
                            v(D, b)
                            b, I, q = {}, I + -0x7f, "Steal Speed"
                            b["Title"] = q
                            q = "Locked at 700. This value cannot be changed."
                            b["Content"] = q
                            q = "lock"
                            b["Icon"] = q
                            v, D = i.AddParagraph, i
                        else
                            c = c(A, n)
                            H, A, I, a = "pets", G[12][1][G[12][2]], 85, {}
                            a["Id"] = H
                            H = "Pets"
                            a["Title"] = H
                            H = "paw-print"
                            a["Icon"] = H
                            n, A = A, A.AddTab
                        end
                    elseif I < 0xdf then
                        I, y = 295 - I, y(v, D)
                        q, b = "Use Selected for filtered farming. Use All to ignore rarity / mutation filters. Big Eggs can run by itself or together with either mode.", {}
                        b["Content"] = q
                        q = "info"
                        b["Icon"] = q
                        D, v = i, i.AddParagraph
                    elseif I <= 0xdf then
                        i = i(F, k)
                        y, G[0x15][1][G[0x15][2]], k = "Return to Base", i, {}
                        k["Title"] = y
                        y = "Return"
                        k["Text"] = y
                        y = "home"
                        k["Icon"] = y
                        y = s:Qd{G[0x1e]}
                        k["Callback"] = y
                        i, I, F = r.AddButton, I + -51, r
                    else
                        J(E, p)
                        p, I, w = {}, 0x3b26 / I, "AutoFusePets"
                        p["Id"] = w
                        w = "Auto Fuse Pets"
                        p["Title"] = w
                        w = "combine"
                        p["Icon"] = w
                        w = false
                        p["Default"] = w
                        J, E = o.AddToggle, o
                    end
                elseif I < 425 then
                    if I <= 252 then
                        if I < 245 then
                            if I < 0xf1 then
                                if I > 239 then
                                    J(E, p)
                                    p, w = {}, "SellMaxScale"
                                    p["Id"] = w
                                    w = "Maximum Scale to Sell"
                                    p["Title"] = w
                                    w = 0
                                    p["Min"] = w
                                    w = 10
                                    p["Max"] = w
                                    p["Default"] = w
                                    w = 0.1
                                    p["Step"] = w
                                    E, I, J = x, 154, x.AddSlider
                                else
                                    u(g, O)
                                    z, I, O = "JumpPower", 0x19, {}
                                    O["Id"] = z
                                    z = "Jump Power"
                                    O["Title"] = z
                                    z = 10
                                    O["Min"] = z
                                    z = 0x1f4
                                    O["Max"] = z
                                    z = 50
                                    O["Default"] = z
                                    z = 1
                                    O["Step"] = z
                                    z = true
                                    O["ValueInput"] = z
                                    g, u = C, C.AddSlider
                                end
                            elseif I <= 242 then
                                if I <= 0xf1 then
                                    J(E, p)
                                    p, w = {}, "FuseKeepMutated"
                                    p["Id"] = w
                                    w = "Never Fuse Mutated"
                                    p["Title"] = w
                                    I, w = 0xdd3b / I, true
                                    p["Default"] = w
                                    J, E = o.AddToggle, o
                                else
                                    q(o, x)
                                    x, J = {}, "When several automation jobs are ready at the same time, the scheduler runs the first available task in this order."
                                    x["Content"] = J
                                    J = "list-ordered"
                                    I, x["Icon"] = 256 - I, J
                                    o, q = y, y.AddParagraph
                                end
                            else
                                v(D, b)
                                b, q = {}, "AutoOpenReadyEggs"
                                b["Id"] = q
                                q = "Auto Hatch Ready"
                                b["Title"] = q
                                q = "egg"
                                I, b["Icon"] = 0x92, q
                                q = false
                                b["Default"] = q
                                D, v = F, F.AddToggle
                            end
                        elseif I >= 0xf8 then
                            if I <= 0xf9 then
                                if I > 248 then
                                    B(C, e)
                                    u, e = "AutoClaimGroupReward", {}
                                    e["Id"] = u
                                    u = "Auto Claim Group Reward"
                                    e["Title"] = u
                                    u = "users"
                                    e["Icon"] = u
                                    u = false
                                    I, e["Default"] = 0x1f7 - I, u
                                    C, B = E, E.AddToggle
                                else
                                    n = n(a, H)
                                    L, a, _ = {}, G[12][1][G[12][2]], "player"
                                    L["Id"] = _
                                    _ = "Player"
                                    L["Title"] = _
                                    I, _ = 257 - I, "eye"
                                    L["Icon"] = _
                                    H, a = a, a.AddTab
                                end
                            else
                                v(D, b)
                                b, q = {}, "Egg selling"
                                b["Title"] = q
                                D, I, v = F, 130, F.AddDivider
                            end
                        elseif I <= 0xf6 then
                            if I <= 0xf5 then
                                J(E, p)
                                w, p = "FuseInterval", {}
                                p["Id"] = w
                                I, w = 483 - I, "Fuse Interval"
                                p["Title"] = w
                                w = 1
                                p["Min"] = w
                                w = 120
                                p["Max"] = w
                                w = 8
                                p["Default"] = w
                                w = 1
                                p["Step"] = w
                                w = " s"
                                p["Suffix"] = w
                                J, E = o.AddSlider, o
                            else
                                I, o = 0xf7 - I, s.c(o(x, J))
                            end
                        else
                            I, J = 36, J(E, p)
                            w, B = {}, "Rewards"
                            w["Title"] = B
                            B = "coins"
                            w["Icon"] = B
                            E, p = n.AddSection, n
                        end
                    elseif I < 268 then
                        if I > 259 then
                            j(m, N)
                            f, N = "AutoReconnect", {}
                            N["Id"] = f
                            f = "Auto Reconnect"
                            N["Title"] = f
                            f = false
                            I, N["Default"] = 0x3e6 - I, f
                            j, m = u.AddToggle, u
                        elseif I > 0x102 then
                            u(g, O)
                            O, z = {}, "Fly"
                            I, O["Title"] = 0x2dc - I, z
                            u, g = C.AddDivider, C
                        elseif I <= 254 then
                            B(C, e)
                            e, u = {}, "AutoClaimOffline"
                            e["Id"] = u
                            u = "Claim Offline Earnings"
                            e["Title"] = u
                            I, u = 190, "wallet"
                            e["Icon"] = u
                            u = false
                            e["Default"] = u
                            B, C = E.AddToggle, E
                        else
                            j(m, N)
                            f, N = "DisableRendering", {}
                            N["Id"] = f
                            f = "Disable 3D Rendering"
                            N["Title"] = f
                            I, f = 0x3e1, false
                            N["Default"] = f
                            f = s:Vd{G[30]}
                            N["Callback"] = f
                            j, m = g.AddToggle, g
                        end
                    elseif I >= 391 then
                        if I >= 397 then
                            if I <= 0x18d then
                                I = 0x3b2
                                j(m, N)
                                f, N = "WebhookPingId", {}
                                N["Id"] = f
                                f = "Ping User ID"
                                N["Title"] = f
                                f = "123456789012345678"
                                N["Placeholder"] = f
                                f = ""
                                N["Default"] = f
                                m, j = O, O.AddInput
                            else
                                O = O(z, j)
                                N, m = "About", {}
                                m["Title"] = N
                                N = "info"
                                I, m["Icon"] = I + 0x8b, N
                                j, z = H, H.AddSection
                            end
                        else
                            u(g, O)
                            O, z = {}, "FlySpeed"
                            O["Id"] = z
                            z = "Fly Speed"
                            O["Title"] = z
                            z = 10
                            O["Min"] = z
                            z = 0x190
                            I, O["Max"] = 0x384, z
                            z = 0x3c
                            O["Default"] = z
                            z = 1
                            O["Step"] = z
                            z = true
                            O["ValueInput"] = z
                            u, g = C.AddSlider, C
                        end
                    elseif I <= 268 then
                        j(m, N)
                        f, N = "AntiGameplayPause", {}
                        N["Id"] = f
                        f = "No Gameplay Paused"
                        N["Title"] = f
                        I, f = 267, true
                        N["Default"] = f
                        f = s:Yd{G[0x1e]}
                        N["Callback"] = f
                        m, j = u, u.AddToggle
                    else
                        j(m, N)
                        N, f = {}, "WebhookRarities"
                        N["Id"] = f
                        f = "Rarities"
                        N["Title"] = f
                        f = G[11][1][G[11][2]]
                        N["Options"] = f
                        I, f = 0x24b, true
                        N["Multi"] = f
                        N["Searchable"] = f
                        K = {}
                        f = K
                        N["Default"] = f
                        j, m = O.AddDropdown, O
                    end
                elseif I < 0x256 then
                    if I <= 0x1d0 then
                        if I < 449 then
                            if I >= 427 then
                                if I <= 0x1ab then
                                    j(m, N)
                                    N, f = {}, "WebhookUrl"
                                    N["Id"] = f
                                    f = "Webhook URL"
                                    N["Title"] = f
                                    I, f = 0x18d, "https://discord.com/api/webhooks/..."
                                    N["Placeholder"] = f
                                    f = ""
                                    N["Default"] = f
                                    j, m = O.AddInput, O
                                else
                                    j(m, N)
                                    f, N = "WebhookEggSpawns", {}
                                    N["Id"] = f
                                    f = "List Spawned Eggs"
                                    I, N["Title"] = I + -148, f
                                    f = true
                                    N["Default"] = f
                                    m, j = O, O.AddToggle
                                end
                            else
                                j(m, N)
                                N, f = {}, "Send Summary Now"
                                N["Title"] = f
                                f = "Send"
                                N["Text"] = f
                                f = "send"
                                N["Icon"] = f
                                I, f = 0x24e, s:Hd{G[30]}
                                N["Callback"] = f
                                m, j = O, O.AddButton
                            end
                        elseif I < 0x1c2 then
                            I, u = 450, u(g, O)
                            z, j = {}, "Performance"
                            z["Title"] = j
                            j = "gauge"
                            z["Icon"] = j
                            O, g = H, H.AddSection
                        elseif I > 450 then
                            j(m, N)
                            I, N, f = 0x102, {}, "FpsBoost"
                            N["Id"] = f
                            f = "FPS Boost"
                            N["Title"] = f
                            f = false
                            N["Default"] = f
                            f = s:Md{G[30]}
                            N["Callback"] = f
                            m, j = g, g.AddToggle
                        else
                            g = g(O, z)
                            I, j, m = 0x2dec4 / I, {}, "Webhooks"
                            j["Title"] = m
                            m = "webhook"
                            j["Icon"] = m
                            O, z = H.AddSection, H
                        end
                    elseif I <= 0x24b then
                        if I > 0x22d then
                            j(m, N)
                            f, N = "WebhookDisconnectAlerts", {}
                            N["Id"] = f
                            f = "Disconnect Alerts"
                            I, N["Title"] = 425, f
                            f = false
                            N["Default"] = f
                            j, m = O.AddToggle, O
                        elseif I > 473 then
                            z = z(j, m)
                            I, f, N = 268, "AntiAfk", {}
                            N["Id"] = f
                            f = "Anti-AFK"
                            N["Title"] = f
                            f = "shield-check"
                            N["Icon"] = f
                            f = true
                            N["Default"] = f
                            j, m = u.AddToggle, u
                        else
                            u(g, O)
                            z, O = "Fly", {}
                            O["Id"] = z
                            O["Title"] = z
                            z = false
                            O["Default"] = z
                            I, z = 0x2d26f / I, s:Rd{G[30]}
                            O["Callback"] = z
                            g, u = C, C.AddToggle
                        end
                    else
                        j(m, N)
                        N, f = {}, "Script Dev"
                        N["Title"] = f
                        f = "MMB"
                        N["Content"] = f
                        f = "user"
                        I, N["Icon"] = 0x2c8, f
                        m, j = z, z.AddParagraph
                    end
                elseif I >= 0x319 then
                    if I < 0x384 then
                        if I > 0x319 then
                            j(m, N)
                            f, N = "Copy Join Script", {}
                            N["Title"] = f
                            f = "Copy"
                            N["Text"] = f
                            f = "clipboard"
                            I, N["Icon"] = 464, f
                            f = s:Nd{G[0x11], G[30]}
                            N["Callback"] = f
                            m, j = u, u.AddButton
                        else
                            j(m, N)
                            N, f = {}, "Search"
                            N["Title"] = f
                            f = "Use the header search or Ctrl+K to find controls, tabs, commands, configs and favorites without digging through the sidebar."
                            N["Content"] = f
                            f = "search"
                            I, N["Icon"] = 0x297, f
                            m, j = z, z.AddParagraph
                        end
                    elseif I < 0x3b2 then
                        u(g, O)
                        z, O = "WaypointTarget", {}
                        O["Id"] = z
                        z = "Waypoint"
                        O["Title"] = z
                        z = G[16][1][G[0x10][2]]
                        O["Options"] = z
                        I, z = 0x2e1, true
                        O["Searchable"] = z
                        z = "Base"
                        O["Default"] = z
                        g, u = e, e.AddDropdown
                    elseif I <= 0x3b2 then
                        j(m, N)
                        f, N = "WebhookInterval", {}
                        N["Id"] = f
                        f = "Summary Interval"
                        N["Title"] = f
                        f = 1
                        N["Min"] = f
                        f = 0xb4
                        N["Max"] = f
                        I, f = 0x1b7, 15
                        N["Default"] = f
                        f = 1
                        N["Step"] = f
                        f = " min"
                        N["Suffix"] = f
                        m, j = O, O.AddSlider
                    else
                        j(m, N)
                        f, N = "FpsCap", {}
                        N["Id"] = f
                        f = "FPS Cap"
                        N["Title"] = f
                        f = 15
                        N["Min"] = f
                        f = 360
                        N["Max"] = f
                        f = 60
                        N["Default"] = f
                        f = 1
                        N["Step"] = f
                        f = " fps"
                        I, N["Suffix"] = 0x637 - I, f
                        f = true
                        N["ValueInput"] = f
                        f = s:Kd{G[30]}
                        N["Callback"] = f
                        m, j = g, g.AddSlider
                    end
                elseif I > 0x2c8 then
                    if I <= 0x2db then
                        j(m, N)
                        f, N = "Rejoin Server", {}
                        I, N["Title"] = 0x98692 / I, f
                        f = "Rejoin"
                        N["Text"] = f
                        f = "refresh-cw"
                        N["Icon"] = f
                        f = "Rejoin the current server?"
                        N["Confirm"] = f
                        f = s:Ud{G[0x1e]}
                        N["Callback"] = f
                        j, m = u.AddButton, u
                    else
                        u(g, O)
                        O, z = {}, "Teleport to Waypoint"
                        O["Title"] = z
                        I, z = 0x366 - I, "Teleport"
                        O["Text"] = z
                        z = "map-pin"
                        O["Icon"] = z
                        z = s:Sd{G[0x1e]}
                        O["Callback"] = z
                        g, u = e, e.AddButton
                    end
                elseif I >= 0x297 then
                    if I > 0x297 then
                        j(m, N)
                        N, I, f = {}, 0x1e980 / I, "UI Library"
                        N["Title"] = f
                        f = "MMB HUB"
                        N["Content"] = f
                        f = "layout-dashboard"
                        N["Icon"] = f
                        m, j = z, z.AddParagraph
                    else
                        j(m, N)
                        m, j = G[0x1e][1][G[0x1e][2]], s:Pd{G[30], G[0x18], G[0x1c], G[0x13], G[1], G[12]}
                        m["unload"] = j
                        j, N = G[0x13][1][G[19][2]], m
                        m = N["unload"]
                        j["__MMB_HUB_SHUTDOWN"] = m
                        I, f, N = 0x367 - I, "Danger Zone", {}
                        N["Title"] = f
                        j, m = z.AddDivider, z
                    end
                else
                    j(m, N)
                    f, N = "WebhookEnabled", {}
                    N["Id"] = f
                    f = "Enable Webhooks"
                    N["Title"] = f
                    f = "webhook"
                    N["Icon"] = f
                    I, f = 0x1ab, false
                    N["Default"] = f
                    j, m = O.AddToggle, O
                end
            elseif I < 73 then
                if I >= 0x2b then
                    if I <= 57 then
                        if I < 0x33 then
                            if I >= 47 then
                                if I <= 0x31 then
                                    if I <= 47 then
                                        v(D, b)
                                        b, q = {}, "SellEggRarities"
                                        b["Id"] = q
                                        q = "Sell Rarities"
                                        b["Title"] = q
                                        q = G[11][1][G[11][2]]
                                        b["Options"] = q
                                        q = true
                                        b["Multi"] = q
                                        b["Searchable"] = q
                                        o = {}
                                        I, q = 3, o
                                        b["Default"] = q
                                        v, D = F.AddDropdown, F
                                    else
                                        i = i(F, k)
                                        k, y, G[20][1][G[20][2]] = {}, "Pets Owned", i
                                        k["Title"] = y
                                        y = "0"
                                        k["Value"] = y
                                        y = "Neutral"
                                        I, k["Status"] = I + 0xae, y
                                        F, i = _, _.AddStatus
                                    end
                                else
                                    J(E, p)
                                    p, I, w = {}, 240, "SellKeepEquipped"
                                    p["Id"] = w
                                    w = "Never Sell Equipped"
                                    p["Title"] = w
                                    w = true
                                    p["Default"] = w
                                    E, J = x, x.AddToggle
                                end
                            elseif I > 43 then
                                C = C(e, u)
                                g, O = {}, "Teleports"
                                g["Title"] = O
                                I, O = 0xab, "map-pin"
                                g["Icon"] = O
                                u, e = a, a.AddSection
                            else
                                B(C, e)
                                u, e = "UpgradeTypes", {}
                                e["Id"] = u
                                u = "Upgrade Types"
                                I, e["Title"] = 0x1e92 / I, u
                                u = G[5][1][G[5][2]]
                                e["Options"] = u
                                u = true
                                e["Multi"] = u
                                e["Searchable"] = u
                                O, g, z = "Base", {}, "Treadmill"
                                g[1], g[2] = O, z
                                u = g
                                e["Default"] = u
                                B, C = J.AddDropdown, J
                            end
                        elseif I <= 0x36 then
                            if I < 53 then
                                if I <= 0x33 then
                                    v(D, b)
                                    I, b, q = 237, {}, "AutoReturn"
                                    b["Id"] = q
                                    q = "Auto Return to Base"
                                    b["Title"] = q
                                    q = "home"
                                    b["Icon"] = q
                                    q = true
                                    b["Default"] = q
                                    D, v = i, i.AddToggle
                                else
                                    v(D, b)
                                    b, q = {}, "StealPriority"
                                    b["Id"] = q
                                    q = "Target Priority"
                                    b["Title"] = q
                                    q = G[8][1][G[8][2]]
                                    b["Options"] = q
                                    q = "Rarest"
                                    b["Default"] = q
                                    D, I, v = i, I + 0xb0, i.AddDropdown
                                end
                            elseif I <= 53 then
                                u(g, O)
                                z, O = "EspDistance", {}
                                O["Id"] = z
                                z = "Render Distance"
                                O["Title"] = z
                                z = 0x64
                                O["Min"] = z
                                z = 0x1770
                                O["Max"] = z
                                z = 0x7d0
                                O["Default"] = z
                                z = 0x32
                                I, O["Step"] = 71, z
                                z = " studs"
                                O["Suffix"] = z
                                z = true
                                O["ValueInput"] = z
                                u, g = B.AddSlider, B
                            else
                                I = 0x7ce / I
                                u(g, O)
                                O, z = {}, "EspPlayers"
                                O["Id"] = z
                                z = "Player ESP"
                                O["Title"] = z
                                z = false
                                O["Default"] = z
                                u, g = B.AddToggle, B
                            end
                        elseif I <= 56 then
                            I = 0x28
                            B(C, e)
                            e, u = {}, "TrailWanted"
                            e["Id"] = u
                            u = "Trails"
                            e["Title"] = u
                            u = G[4][1][G[4][2]]
                            e["Options"] = u
                            u = true
                            e["Multi"] = u
                            e["Searchable"] = u
                            g = {}
                            u = g
                            e["Default"] = u
                            B, C = p.AddDropdown, p
                        else
                            B = B(C, e)
                            g, u = "Movement", {}
                            u["Title"] = g
                            g = "move"
                            I, u["Icon"] = I + -12, g
                            e, C = a, a.AddSection
                        end
                    elseif I < 0x42 then
                        if I >= 0x3e then
                            if I > 0x3e then
                                J(E, p)
                                p, w = {}, "SellRarities"
                                p["Id"] = w
                                w = "Sell Rarities"
                                p["Title"] = w
                                w = G[11][1][G[11][2]]
                                p["Options"] = w
                                I, w = 74, true
                                p["Multi"] = w
                                p["Searchable"] = w
                                B = {}
                                w = B
                                p["Default"] = w
                                E, J = x, x.AddDropdown
                            else
                                _ = _(r, l)
                                t, i = {}, "Quick Actions"
                                t["Title"] = i
                                i = "zap"
                                I, t["Icon"] = 22, i
                                l, r = M, M.AddSection
                            end
                        elseif I <= 0x3a then
                            v(D, b)
                            q, b = "HopMode", {}
                            b["Id"] = q
                            q = "Hop When"
                            b["Title"] = q
                            q = G[15][1][G[15][2]]
                            b["Options"] = q
                            q = "No Matching Eggs"
                            b["Default"] = q
                            v, I, D = k.AddDropdown, 135, k
                        else
                            t = t(i, F)
                            F, G[18][1][G[0x12][2]], k = {}, t, "Server"
                            F["Title"] = k
                            k = G[26][1][G[0x1a][2]]
                            F["Value"] = k
                            k = "Neutral"
                            I, F["Status"] = 89, k
                            t, i = L.AddStatus, L
                        end
                    elseif I < 68 then
                        if I <= 66 then
                            q = q(o, x)
                            E, J = "Auto Fuse", {}
                            J["Title"] = E
                            I, E = 0x1f, "combine"
                            J["Icon"] = E
                            x, o = A, A.AddSection
                        else
                            J(E, p)
                            w, p = "FuseRarities", {}
                            p["Id"] = w
                            w = "Fuse Rarities"
                            p["Title"] = w
                            w = G[11][1][G[11][2]]
                            p["Options"] = w
                            w = true
                            p["Multi"] = w
                            I, p["Searchable"] = 145, w
                            B = {}
                            w = B
                            p["Default"] = w
                            J, E = o.AddDropdown, o
                        end
                    elseif I < 0x46 then
                        v(D, b)
                        q, b = "StealMutations", {}
                        b["Id"] = q
                        I, q = 52, "Mutations"
                        b["Title"] = q
                        q = "Empty = all mutations"
                        b["Description"] = q
                        q = G[14][1][G[14][2]]
                        b["Options"] = q
                        q = true
                        b["Multi"] = q
                        b["Searchable"] = q
                        o = {}
                        q = o
                        b["Default"] = q
                        v, D = i.AddDropdown, i
                    elseif I <= 0x46 then
                        t = t(i, F)
                        F, G[7][1][G[7][2]], k = {}, t, "Stolen Eggs"
                        I, F["Title"] = 160, k
                        k = "0"
                        F["Value"] = k
                        k = "Neutral"
                        F["Status"] = k
                        t, i = L.AddStatus, L
                    else
                        u(g, O)
                        O, z = {}, "WalkSpeedEnabled"
                        I, O["Id"] = 0xe9, z
                        z = "Walk Speed Override"
                        O["Title"] = z
                        z = false
                        O["Default"] = z
                        u, g = C.AddToggle, C
                    end
                elseif I <= 25 then
                    if I >= 8 then
                        if I > 0x16 then
                            if I > 23 then
                                u(g, O)
                                O, z = {}, "InfJump"
                                I, O["Id"] = 132, z
                                z = "Infinite Jump"
                                O["Title"] = z
                                z = false
                                O["Default"] = z
                                u, g = C.AddToggle, C
                            else
                                u(g, O)
                                z, O = "EspGuards", {}
                                O["Id"] = z
                                z = "Guard ESP"
                                O["Title"] = z
                                I, z = 178, false
                                O["Default"] = z
                                g, u = B, B.AddToggle
                            end
                        elseif I <= 14 then
                            if I <= 9 then
                                if I <= 8 then
                                    v(D, b)
                                    b, q = {}, "StealBigEggs"
                                    b["Id"] = q
                                    q = "Steal Big Eggs"
                                    b["Title"] = q
                                    q = "maximize"
                                    b["Icon"] = q
                                    q = false
                                    I, b["Default"] = I + 166, q
                                    v, D = i.AddToggle, i
                                else
                                    a = a(H, L)
                                    _, r, H = {}, "system", G[12][1][G[12][2]]
                                    _["Id"] = r
                                    r = "System"
                                    _["Title"] = r
                                    r = "settings-2"
                                    _["Icon"] = r
                                    H, I, L = H.AddTab, 0xba, H
                                end
                            else
                                I = 41 - I
                                q(o, x)
                                o, q = G[0x19][1][G[25][2]], s._["ipairs"]
                            end
                        else
                            r = r(l, t)
                            i, F = {}, "Quick Start"
                            i["Title"] = F
                            I, F = I + 66, "book-open"
                            i["Icon"] = F
                            l, t = M.AddSection, M
                        end
                    elseif I < 4 then
                        if I > 1 then
                            v(D, b)
                            q, b = "SellEggInterval", {}
                            b["Id"] = q
                            q = "Sell Interval"
                            b["Title"] = q
                            q = 1
                            b["Min"] = q
                            q = 120
                            b["Max"] = q
                            q = 8
                            b["Default"] = q
                            q = 1
                            b["Step"] = q
                            q = " s"
                            I, b["Suffix"] = 0xa2, q
                            v, D = F.AddSlider, F
                        else
                            q(s.d(o))
                            o, I, x, q = v, 181, b, v.OnChanged
                        end
                    elseif I >= 5 then
                        if I > 5 then
                            k = k(y, v)
                            b, D = "Task Order", {}
                            D["Title"] = b
                            b = "list-ordered"
                            I, D["Icon"] = 0xde, b
                            y, v = c.AddSection, c
                        else
                            L = L(_, r)
                            t, l = "Account", {}
                            l["Title"] = t
                            t = "user"
                            l["Icon"] = t
                            r, I, _ = M, 0x136 / I, M.AddSection
                        end
                    else
                        u(g, O)
                        z, O = "EspPlots", {}
                        O["Id"] = z
                        z = "Plot ESP"
                        O["Title"] = z
                        z = false
                        I, O["Default"] = 53, z
                        g, u = B, B.AddToggle
                    end
                elseif I >= 36 then
                    if I < 38 then
                        if I > 36 then
                            u(g, O)
                            O, z = {}, "EspMachines"
                            O["Id"] = z
                            z = "Machine ESP"
                            I, O["Title"] = 4, z
                            z = false
                            O["Default"] = z
                            g, u = B, B.AddToggle
                        else
                            E = E(p, w)
                            C, B = "Equipment", {}
                            I, B["Title"] = 0xe9 - I, C
                            C = "shopping-bag"
                            B["Icon"] = C
                            w, p = n, n.AddSection
                        end
                    elseif I <= 39 then
                        if I <= 38 then
                            x = x(J, E)
                            p, w = {}, "AutoEquipBest"
                            p["Id"] = w
                            w = "Auto Equip Best Pets"
                            p["Title"] = w
                            w = "sparkles"
                            p["Icon"] = w
                            w = false
                            I, p["Default"] = 0xcb, w
                            E, J = q, q.AddToggle
                        else
                            i(F, k)
                            k, y = {}, "Server Hop"
                            k["Title"] = y
                            y = "Hop"
                            k["Text"] = y
                            y = "server"
                            k["Icon"] = y
                            y = s:Id{G[2], G[30]}
                            I, k["Callback"] = 0x115e / I, y
                            i, F = r.AddButton, r
                        end
                    else
                        B(C, e)
                        e, u = {}, "AutoEquipBestTrail"
                        e["Id"] = u
                        u = "Auto Equip Best Trail"
                        I, e["Title"] = 0x9f, u
                        u = "sparkles"
                        e["Icon"] = u
                        u = false
                        e["Default"] = u
                        B, C = p.AddToggle, p
                    end
                elseif I < 0x1f then
                    if I > 0x1b then
                        v(D, b)
                        q, b = "AutoStealAll", {}
                        b["Id"] = q
                        q = "Auto Steal All"
                        b["Title"] = q
                        q = "Ignore rarity and mutation filters"
                        b["Description"] = q
                        J, E, x, o, w, p = "steal", "all", "egg", {}, "autofarm", "farm"
                        o[1], o[2], o[3], o[4], o[5] = x, J, E, p, w
                        q = o
                        b["Keywords"] = q
                        q = "bot"
                        b["Icon"] = q
                        q = false
                        b["Default"] = q
                        v, I, D = i.AddToggle, I + -21, i
                    else
                        q, o, x = q(o)
                        q, o, x = s.b(q, o, x)
                        J, E = q(o, x)
                        x = J
                        I = x == nil and 122 - I or 221
                    end
                elseif I <= 31 then
                    o = o(x, J)
                    E, p = {}, "Auto Sell Pets"
                    E["Title"] = p
                    p = "tags"
                    E["Icon"] = p
                    x, I, J = A.AddSection, 38, A
                else
                    v(D, b)
                    b, q = {}, "AutoPlaceSelected"
                    b["Id"] = q
                    q = "Auto Place Selected"
                    b["Title"] = q
                    q = "package"
                    b["Icon"] = q
                    q = false
                    b["Default"] = q
                    I, v, D = 81, F.AddToggle, F
                end
            elseif I < 0x72 then
                if I > 0x5f then
                    if I > 0x68 then
                        if I > 110 then
                            I = t and 0x81 or 0x69
                        elseif I > 0x6c then
                            I, i = 93, i(F, k)
                            G[27][1][G[27][2]], k, y = i, {}, "Money"
                            k["Title"] = y
                            y = "0"
                            k["Value"] = y
                            y = "Neutral"
                            k["Status"] = y
                            i, F = _.AddStatus, _
                        elseif I <= 0x69 then
                            I, t = 0xea - I, 0x64
                        else
                            I, t = 111, t(i)
                        end
                    elseif I >= 99 then
                        if I <= 101 then
                            if I <= 0x63 then
                                I, v = I + 119, s.c(v())
                            else
                                v(D, b)
                                q, b = "StealBigEggScale", {}
                                b["Id"] = q
                                q = "Minimum Big Egg Size"
                                b["Title"] = q
                                q = 1
                                b["Min"] = q
                                q = 50
                                b["Max"] = q
                                q = 1.5
                                b["Default"] = q
                                q = 0.1
                                b["Step"] = q
                                q = "x"
                                I, b["Suffix"] = 0x68, q
                                v, D = i.AddSlider, i
                            end
                        else
                            v(D, b)
                            b, q = {}, "Carry behavior"
                            b["Title"] = q
                            v, I, D = i.AddDivider, 0x14b8 / I, i
                        end
                    elseif I > 97 then
                        C = C(e, u)
                        B["Title"] = C
                        C = G[0x17][1][G[23][2]]
                        B["Options"] = C
                        e = C
                        C = e[J]
                        I, B["Default"] = 0x4edc / I, C
                        w, p = y, y.AddDropdown
                    else
                        i(F, k)
                        y, k = "Farm flow", {}
                        k["Title"] = y
                        y = "1) Open Farm -> Steal.  2) Pick areas / rarities only when you want filters.  3) Enable Auto Steal Selected or Auto Steal All.  4) Keep Auto Return on so stolen eggs come back to your plot."
                        k["Content"] = y
                        I, y = I + 0x47, "play"
                        k["Icon"] = y
                        i, F = l.AddParagraph, l
                    end
                elseif I >= 0x55 then
                    if I < 93 then
                        if I <= 88 then
                            if I > 85 then
                                l = l(t, i)
                                k, F = "Automation", {}
                                F["Title"] = k
                                I, k = 0xcd, "Ready"
                                F["Value"] = k
                                k = "Success"
                                F["Status"] = k
                                t, i = L.AddStatus, L
                            else
                                A = A(n, a)
                                L, H, n = "progress", {}, G[12][1][G[12][2]]
                                H["Id"] = L
                                I, L = I + 163, "Progress"
                                H["Title"] = L
                                L = "arrow-big-up"
                                H["Icon"] = L
                                a, n = n, n.AddTab
                            end
                        else
                            t(i, F)
                            t = G[0x16][1][G[22][2]]
                            I = t and 0x5e or 0xc8 - I
                        end
                    elseif I > 0x5e then
                        x, I, J = {}, 66, "Pets"
                        x["Title"] = J
                        J = "paw-print"
                        x["Icon"] = J
                        o, q = A, A.AddSection
                    elseif I <= 0x5d then
                        i = i(F, k)
                        G[13][1][G[13][2]], y, k = i, "Speed Power", {}
                        k["Title"] = y
                        y = "0"
                        k["Value"] = y
                        y = "Neutral"
                        I, k["Status"] = 0x1b9c / I, y
                        F, i = _, _.AddStatus
                    else
                        i, t = G[0x16][1][G[22][2]], s._["tonumber"]
                        I, i = 0xca - I, i["MAX_INVENTORY"]
                    end
                elseif I < 75 then
                    if I <= 73 then
                        v(D, b)
                        b, q = {}, "AutoStealSelected"
                        b["Id"] = q
                        q = "Auto Steal Selected"
                        b["Title"] = q
                        q = "Use area / rarity / mutation filters below"
                        b["Description"] = q
                        E, w, o, J, p, x = "farm", "autofarm", {}, "steal", "filtered", "egg"
                        o[1], o[2], o[3], o[4], o[5] = x, J, E, p, w
                        I, q = I + -44, o
                        b["Keywords"] = q
                        q = "filter"
                        b["Icon"] = q
                        q = false
                        b["Default"] = q
                        v, D = i.AddToggle, i
                    else
                        J(E, p)
                        p, w = {}, "SellMutations"
                        p["Id"] = w
                        w = "Sell Mutations"
                        p["Title"] = w
                        w = G[14][1][G[14][2]]
                        p["Options"] = w
                        I, w = 128, true
                        p["Multi"] = w
                        p["Searchable"] = w
                        B = {}
                        w = B
                        p["Default"] = w
                        E, J = x, x.AddDropdown
                    end
                elseif I > 0x4c then
                    v(D, b)
                    q, b = "AutoPlaceAll", {}
                    b["Id"] = q
                    q = "Auto Place All"
                    b["Title"] = q
                    q = "boxes"
                    I, b["Icon"] = 0xf3, q
                    q = false
                    b["Default"] = q
                    D, v = F, F.AddToggle
                elseif I > 75 then
                    i = i(F, k)
                    G[9][1][G[9][2]], y, k = i, "Rebirths", {}
                    k["Title"] = y
                    y = "0"
                    k["Value"] = y
                    y = "Neutral"
                    k["Status"] = y
                    F, I, i = _, 0x31, _.AddStatus
                else
                    v(D, b)
                    q, b = "StealRarities", {}
                    b["Id"] = q
                    q = "Rarities"
                    b["Title"] = q
                    q = "Empty = all rarities"
                    b["Description"] = q
                    q = G[11][1][G[11][2]]
                    b["Options"] = q
                    q = true
                    b["Multi"] = q
                    b["Searchable"] = q
                    o = {}
                    q = o
                    b["Default"] = q
                    I, D, v = 0x44, i, i.AddDropdown
                end
            elseif I >= 0x85 then
                if I >= 0x97 then
                    if I > 0x9d then
                        if I <= 0x9f then
                            B(C, e)
                            e, u = {}, "AutoEquipBestGear"
                            e["Id"] = u
                            u = "Auto Equip Best Gear"
                            e["Title"] = u
                            u = "sword"
                            e["Icon"] = u
                            u = false
                            I, e["Default"] = 196, u
                            C, B = p, p.AddToggle
                        else
                            t = t(i, F)
                            G[3][1][G[3][2]], k, F = t, "Carrying Egg", {}
                            I, F["Title"] = 155, k
                            k = "No"
                            F["Value"] = k
                            k = "Neutral"
                            F["Status"] = k
                            t, i = L.AddStatus, L
                        end
                    elseif I < 155 then
                        if I > 151 then
                            J(E, p)
                            p, w = {}, "SellInterval"
                            p["Id"] = w
                            I, w = 338 - I, "Sell Interval"
                            p["Title"] = w
                            w = 1
                            p["Min"] = w
                            w = 0x78
                            p["Max"] = w
                            w = 6
                            p["Default"] = w
                            w = 1
                            p["Step"] = w
                            w = " s"
                            p["Suffix"] = w
                            J, E = x.AddSlider, x
                        else
                            u(g, O)
                            O, z = {}, "EspCarriedEggs"
                            I, O["Id"] = I + -0x80, z
                            z = "Carried and Dropped Egg ESP"
                            O["Title"] = z
                            z = false
                            O["Default"] = z
                            u, g = B.AddToggle, B
                        end
                    elseif I <= 0x9b then
                        t = t(i, F)
                        G[6][1][G[6][2]], F, k = t, {}, "Runtime"
                        F["Title"] = k
                        k = "0m"
                        I, F["Value"] = 0xd7 - I, k
                        k = "Neutral"
                        F["Status"] = k
                        t, i = L.AddStatus, L
                    else
                        w = w(B, C)
                        u, e = "AutoUpgrades", {}
                        I, e["Id"] = 0x2b, u
                        u = "Auto Buy Upgrades"
                        e["Title"] = u
                        u = "arrow-big-up"
                        e["Icon"] = u
                        u = false
                        e["Default"] = u
                        B, C = J.AddToggle, J
                    end
                elseif I <= 145 then
                    if I > 0x87 then
                        J(E, p)
                        p, w = {}, "FuseMutations"
                        p["Id"] = w
                        w = "Fuse Mutations"
                        p["Title"] = w
                        w = G[14][1][G[14][2]]
                        p["Options"] = w
                        w = true
                        p["Multi"] = w
                        p["Searchable"] = w
                        B = {}
                        w = B
                        I, p["Default"] = 269 - I, w
                        E, J = o, o.AddDropdown
                    elseif I <= 133 then
                        I = I + 316
                        u(g, O)
                        z, O = "Session", {}
                        O["Title"] = z
                        z = "refresh-cw"
                        O["Icon"] = z
                        g, u = H, H.AddSection
                    else
                        v = v(D, b)
                        o, q = "HopValue", {}
                        q["Id"] = o
                        o = "Wait Before Hop"
                        q["Title"] = o
                        o = "Seconds without a matching egg"
                        q["Description"] = o
                        o = 1
                        q["Min"] = o
                        o = 0xc8
                        q["Max"] = o
                        o = 15
                        q["Default"] = o
                        o = 1
                        q["Step"] = o
                        I, o = I + 34, true
                        q["ValueInput"] = o
                        b, D = k, k.AddSlider
                    end
                elseif I > 0x92 then
                    i(F, k)
                    y, k = "Steal Eggs", {}
                    k["Title"] = y
                    y = "hand-grab"
                    k["Icon"] = y
                    y = "Main egg farming controls"
                    k["Description"] = y
                    I, i, F = 201, c.AddSection, c
                else
                    v(D, b)
                    b, q = {}, "LifecycleRarities"
                    b["Id"] = q
                    q = "Lifecycle Rarities"
                    b["Title"] = q
                    q = "Used by filtered placement and hatch"
                    b["Description"] = q
                    q = G[11][1][G[11][2]]
                    b["Options"] = q
                    I, q = 215, true
                    b["Multi"] = q
                    b["Searchable"] = q
                    o = {}
                    q = o
                    b["Default"] = q
                    v, D = F.AddDropdown, F
                end
            elseif I <= 128 then
                if I > 0x7b then
                    if I > 0x7c then
                        J(E, p)
                        p, w = {}, "SellKeepMutated"
                        p["Id"] = w
                        w = "Never Sell Mutated"
                        p["Title"] = w
                        I, w = I + -78, true
                        p["Default"] = w
                        J, E = x.AddToggle, x
                    else
                        J(E, p)
                        I, w, p = 0xf1, "FuseTarget", {}
                        p["Id"] = w
                        w = "Pick Group By"
                        p["Title"] = w
                        w = G[0x1d][1][G[0x1d][2]]
                        p["Options"] = w
                        w = "Highest Rarity"
                        p["Default"] = w
                        E, J = o, o.AddDropdown
                    end
                elseif I >= 121 then
                    if I > 0x79 then
                        J(E, p)
                        w, p = "FuseKeepPerCategory", {}
                        p["Id"] = w
                        w = "Keep Per Pet Type"
                        p["Title"] = w
                        I, w = 245, 0
                        p["Min"] = w
                        w = 20
                        p["Max"] = w
                        w = 0
                        p["Default"] = w
                        w = 1
                        p["Step"] = w
                        J, E = o.AddSlider, o
                    else
                        I = 63
                        J(E, p)
                        w, p = "AutoSellPets", {}
                        p["Id"] = w
                        w = "Auto Sell Pets"
                        p["Title"] = w
                        w = "tags"
                        p["Icon"] = w
                        w = false
                        p["Default"] = w
                        J, E = x.AddToggle, x
                    end
                elseif I <= 114 then
                    i(F, k)
                    y, k = "Fuse Now", {}
                    k["Title"] = y
                    y = "Fuse"
                    k["Text"] = y
                    y = "combine"
                    k["Icon"] = y
                    y = s:Od{G[0x1e]}
                    k["Callback"] = y
                    I, F, i = 0x2b32 / I, r, r.AddButton
                else
                    F = F(k, y)
                    D, v = "Server Hop", {}
                    v["Title"] = D
                    I, D = 7, "server"
                    v["Icon"] = D
                    k, y = c.AddSection, c
                end
            elseif I >= 0x83 then
                if I <= 0x83 then
                    J, E = q(o, x)
                    x = J
                    I = x == nil and 95 or 221
                else
                    u(g, O)
                    O, z = {}, "NoClip"
                    O["Id"] = z
                    O["Title"] = z
                    z = false
                    O["Default"] = z
                    I, u, g = I + 127, C.AddToggle, C
                end
            elseif I <= 129 then
                y, k = "Egg Inventory", {}
                k["Title"] = y
                y, D = s._["tostring"], G[30][1][G[30][2]]
                I, v = 99, D["eggInventoryCount"]
            else
                v(D, b)
                b, q = {}, "AutoSellEggs"
                b["Id"] = q
                q = "Auto Sell Eggs"
                b["Title"] = q
                q = "egg"
                b["Icon"] = q
                q = false
                I, b["Default"] = 47, q
                v, D = F.AddToggle, F
            end
        until false
    end
end,
Ha = function (e)
    return function (d, c)
        local _, b, f
        _ = 144
        while true do
            if _ >= 0x90 then
                d = {[2] = 3, [3] = d}
                _, d[1] = 88, d
                c = {[2] = 3, [3] = c}
                c[1] = c
                b, f = e._["pcall"], e:Bd{c, d}
            else
                b(f)
                return
            end
        end
    end
end,
ue = function (e, g)
    return function ()
        local _, c, b, d
        _ = 0x18
        while true do
            if _ < 220 then
                if _ <= 24 then
                    _, b, d = 0x21, "RobloxNetworkPauseNotification", g[2][1][g[2][2]]
                    c, d = d, d.FindFirstChild
                else
                    d = d(c, b)
                    _ = d and 0xfd - _ or 234
                end
            elseif _ > 220 then
                return
            else
                _, b = 234, g[1][1][g[1][2]]
                c = not b
                d["Enabled"] = c
            end
        end
    end
end,
Ef = function (a, b, c, d)
    a.Df[d] = a.gf(b, c)
    return a.Df[d]
end,
Rb = function (e, a)
    return function ()
        local _, d, c
        _ = 0x14
        repeat
            if _ >= 0x8f then
                if _ >= 0xce then
                    if _ <= 0xce then
                        _, d = 0x146 - _, d(c)
                    else
                        _, c = 206, a[1][1][a[1][2]]
                        c, d = "AutoStealAll", c["isOn"]
                    end
                elseif _ <= 0x8f then
                    return d
                else
                    _, d = 143, d(c)
                end
            elseif _ >= 0x37 then
                if _ > 55 then
                    _ = d and 263 - _ or 0x37
                else
                    _, c = 0xbd, a[1][1][a[1][2]]
                    c, d = "StealBigEggs", c["isOn"]
                end
            elseif _ > 20 then
                d = d(c)
                _ = d and 142 - _ or 0xea
            else
                c = a[1][1][a[1][2]]
                c, _, d = "AutoStealSelected", 0x16, c["isOn"]
            end
        until false
    end
end,
na = function (e)
    return function (d, ...)
        local j, _, c, b, k, i, f, a
        j = 0x5c
        while true do
            if j < 155 then
                if j > 0x4a then
                    if j < 0x7f then
                        if j <= 0x54 then
                            j = i ~= i and 0x46e0 / j or j + 152
                        else
                            b, j, c = d, 0x24, e._["typeof"]
                        end
                    elseif j <= 127 then
                        j = c > b and 143 or 0x6338 / j
                    else
                        c = nil
                        return c
                    end
                elseif j <= 0x31 then
                    if j >= 48 then
                        if j <= 0x30 then
                            k, j, a, c, f = "#", 0x14, e._["select"], 1, e.c(...)
                        else
                            f = f(_)
                            _ = "function"
                            j = f == _ and 0x2059 / j or 184
                        end
                    elseif j <= 0x14 then
                        a = a(k, e.d(f))
                        i, b = 1, a
                        j = b ~= b and 0x8f or j + 0xdb
                    else
                        c = c(b)
                        b = "table"
                        j = c ~= b and 0xfd or 0x54 - j
                    end
                elseif j <= 73 then
                    j = i ~= i and 143 or j + 0x7d
                else
                    j, a = 0x31, a(k, e.d(f))
                    k, f = d[a], e._["typeof"]
                    _ = k
                end
            elseif j < 200 then
                if j > 184 then
                    if j > 193 then
                        k, j, a, f = c, 74, e._["select"], e.c(...)
                    else
                        j = c < b and 0x8f or 0x49
                    end
                elseif j <= 169 then
                    if j <= 155 then
                        j = c > b and 143 or 0x54
                    else
                        return k
                    end
                else
                    c = c + i
                    j = i > 0 and 0x5b48 / j or 200
                end
            elseif j < 0xec then
                if j > 200 then
                    j = c < b and 0x78a8 / j or 198
                else
                    j = i <= 0 and 193 or 0x3908 / j
                end
            elseif j > 239 then
                c = nil
                return c
            elseif j <= 0xec then
                j = i <= 0 and 216 or 434 - j
            else
                j = i > 0 and 155 or 84
            end
        end
    end
end,
ea = function (s, h)
    return function (d, c, w)
        local p, k, v, u, f, o, b, g, j, _, i, t, a, q, e, n, r, l
        j = 61
        while true do
            if j <= 138 then
                if j <= 0x41 then
                    if j >= 41 then
                        if j < 0x36 then
                            if j <= 0x2d then
                                if j > 42 then
                                    b = n[1][n[2]]["Position"]
                                    e = b - f
                                    e, v = 8, e["Magnitude"]
                                    u = v <= e
                                    return u
                                elseif j <= 0x29 then
                                    n = false
                                    return n
                                else
                                    j, p = 180, h[1][1][h[1][2]]
                                    p, a = n[1][n[2]], p["stripCheatMovers"]
                                end
                            else
                                j, v = j + 7, c[1][c[2]]
                            end
                        elseif j > 0x3d then
                            if j > 0x3f then
                                n = n(a, p)
                                a, d = h[1][1][h[1][2]], n
                                j, n = 199, a["getRoot"]
                            else
                                v = h[2][1][h[2][2]]
                                u = not v
                                j = u and 142 or j + 0x5c
                            end
                        elseif j > 0x38 then
                            j, c = 0xca, {[2] = 3, [3] = c}
                            c[1] = c
                            a, p = s._["typeof"], d
                        elseif j > 0x36 then
                            j, v = 0xc6 - j, v()
                            u = not v
                        else
                            a(p)
                            p = h[1][1][h[1][2]]
                            a = p["_moveTween"]
                            j = a and 89 or 105
                        end
                    elseif j < 19 then
                        if j <= 11 then
                            if j >= 5 then
                                if j <= 5 then
                                    j = 0x226 / j
                                    p(f)
                                    f = h[1][1][h[1][2]]
                                    r, p, _, f = n[1][n[2]]["Position"], f["groundedY"], d.Z, d.X
                                    r = r.Y
                                else
                                    p = false
                                    j, a["Sit"] = j + 236, p
                                    p = true
                                    a["PlatformStand"] = p
                                end
                            else
                                u = u()
                                a = u
                                j = a and 0x162 / j or 182
                            end
                        else
                            u = u()
                            n[1][n[2]] = u
                            u = not n[1][n[2]]
                            j = u and 0xe3 or 45
                        end
                    elseif j > 31 then
                        j, t = j + 188, s._["Vector3"]
                        g, i, l = _.X, f.X, t["new"]
                        i, g, k, t = 0, f.Z, _.Z, i - g
                        g = g - k
                    elseif j >= 30 then
                        if j > 0x1e then
                            v = v(e, b, q)
                            e = {}
                            j, e["CFrame"] = 0x69 - j, t
                            g, k = g.Create, g
                        else
                            j, g = 0x88, s._["CFrame"]
                            k, i, g = f + l, g["lookAt"], f
                        end
                    else
                        u = u()
                        n[1][n[2]], j, u = u, 2, v["getHumanoid"]
                    end
                elseif j >= 0x64 then
                    if j >= 0x82 then
                        if j >= 136 then
                            if j > 0x88 then
                                u = false
                                return u
                            else
                                j, i = 0x113 - j, i(g, k)
                                t = i
                            end
                        elseif j > 130 then
                            u(v)
                            v, j, u = g[1][g[2]], 91, g[1][g[2]].Play
                        else
                            j, v, u = 183, nil, h[1][1][h[1][2]]
                            u["_moveTween"] = v
                        end
                    elseif j > 110 then
                        j, t, l = 328 - j, s:pd{n}, s._["pcall"]
                    elseif j >= 105 then
                        if j <= 0x69 then
                            p = h[1][1][h[1][2]]
                            j, a = 0x47c7 / j, p["getHumanoid"]
                        else
                            p = p(f, _, r)
                            _ = s._["Vector3"]
                            l, f, j, _ = 2, _["new"], 0x5a3c / j, d.X
                            l, r = d.Z, p + l
                        end
                    else
                        j = n and 0x29 or 0x251c / j
                    end
                elseif j >= 0x59 then
                    if j < 93 then
                        if j > 0x59 then
                            u(v)
                            v = h[1][1][h[1][2]]
                            u, j, e = v["waitFor"], 0x12c - j, 0.35
                            b, e, v = s:qd{g, c, h[2], k}, 0.03, i + e
                        else
                            a, j, p = s._["pcall"], 75, s:od{h[1]}
                        end
                    elseif j > 93 then
                        a = h[1][1][h[1][2]]
                        j, a, p, n = j + -30, d, true, a["clampToCorridor"]
                        p = w == p
                    else
                        v, j, u = s:sd{n}, 0x107 - j, s._["pcall"]
                    end
                elseif j >= 0x4b then
                    if j > 0x4b then
                        k = h[4][1][h[4][2]]
                        g = k["MoveTimeout"]
                        j = i > g and 0xe9 - j or 241
                    else
                        a(p)
                        p, j, a = nil, 0x69, h[1][1][h[1][2]]
                        a["_moveTween"] = p
                    end
                else
                    g = g(k, u, v, e)
                    g = {[2] = 3, [3] = g}
                    g[1] = g
                    j, k = 205 - j, h[1][1][h[1][2]]
                    k["_moveTween"] = g[1][g[2]]
                    k = false
                    k = {[2] = 3, [3] = k}
                    k[1] = k
                    u, v = s._["pcall"], s:nd{k, g}
                end
            elseif j > 193 then
                if j > 0xd9 then
                    if j > 0xf1 then
                        if j > 0xf7 then
                            a = false
                            return a
                        else
                            j, f, p = j + -0xf2, s:rd{n}, s._["pcall"]
                        end
                    elseif j >= 239 then
                        if j > 239 then
                            u, e, g = n[1][n[2]], s._["TweenInfo"], h[3][1][h[3][2]]
                            e, v, j, o = i, e["new"], 31, s._["Enum"]
                            q = o["EasingStyle"]
                            q, b = o["EasingDirection"], q["Linear"]
                            q = q["Out"]
                        else
                            a = h[2][1][h[2][2]]
                            j, n = 0x153 - j, not a
                        end
                    elseif j <= 0xdc then
                        l = l(t, i, g)
                        t, i, g = nil, l["Magnitude"], 0.05
                        j = i > g and 250 - j or 0xd6
                    else
                        u = false
                        return u
                    end
                elseif j >= 0xd1 then
                    if j >= 0xd6 then
                        if j > 0xd6 then
                            l(t)
                            t = h[1][1][h[1][2]]
                            j, l, t, g = 193, t["placeRoot"], n[1][n[2]], s._["CFrame"]
                            g, u, k, i = d.X, d.Z, p, g["new"]
                        else
                            g = s._["CFrame"]
                            j, i, g = 0x8842 / j, g["new"], f
                        end
                    elseif j <= 0xd1 then
                        u(v, e, b)
                        v = h[1][1][h[1][2]]
                        u = v["_moveTween"]
                        j = u == g[1][g[2]] and 0x82 or j + -0x1a
                    else
                        f = f(_, r, l)
                        _ = n[1][n[2]]["Position"]
                        l = f - _
                        t, r = h[4][1][h[4][2]], l["Magnitude"]
                        l = t["ArriveDistance"]
                        j = r <= l and j + -54 or 0xf2 - j
                    end
                elseif j > 199 then
                    a = a(p)
                    p = "Vector3"
                    n = a ~= p
                    j = n and j + -0x66 or 239
                elseif j > 198 then
                    n = n()
                    n = {[2] = 3, [3] = n}
                    n[1] = n
                    a = not n[1][n[2]]
                    j = a and 0xc0c8 / j or 42
                elseif j > 0xc2 then
                    l(t, s.d(i))
                    l = true
                    return l
                else
                    g = g()
                    i, g = r / g, 0.05
                    j = i < g and 0xbc or 0x3d62 / j
                end
            elseif j < 172 then
                if j > 0x9b then
                    if j < 0xa3 then
                        j = a and 0x97 or 111
                    elseif j > 163 then
                        u(v)
                        v = s._["Vector3"]
                        u = v["zero"]
                        j, n[1][n[2]]["AssemblyLinearVelocity"] = 63, u
                        u = v["zero"]
                        n[1][n[2]]["AssemblyAngularVelocity"] = u
                    else
                        i = i(g)
                        j, t = j + -0x18, i
                    end
                elseif j > 0x97 then
                    if j > 152 then
                        u = c[1][c[2]]
                        j = u and 204 - j or 0x55fa / j
                    else
                        j, g = 0xf1, h[4][1][h[4][2]]
                        i = g["MoveTimeout"]
                    end
                elseif j > 142 then
                    l = false
                    j, a["PlatformStand"] = 262 - j, l
                elseif j <= 0x8b then
                    k = h[1][1][h[1][2]]
                    j, g = j + 55, k["stealSpeed"]
                else
                    j = u and 0x8a or 172
                end
            elseif j > 0xb6 then
                if j > 0xbc then
                    j, i = 0xc6, s.c(i(g, k, u))
                elseif j > 183 then
                    j, i = 0x3b7c / j, 0.05
                else
                    j, v = 0xd95 / j, h[1][1][h[1][2]]
                    u = v["getRoot"]
                end
            elseif j <= 177 then
                if j >= 0xaf then
                    if j > 175 then
                        j, u = 0x167 - j, false
                        a["PlatformStand"] = u
                    else
                        a = a()
                        j = a and 11 or 0xa8d9 / j
                    end
                else
                    v = h[1][1][h[1][2]]
                    j, u = j + -0x9b, v["getRoot"]
                end
            elseif j > 180 then
                j = n[1][n[2]] and 0x421e / j or 63
            else
                j = 234 - j
                a(p)
                p = h[1][1][h[1][2]]
                p, a = n[1][n[2]], p["stopSoftMove"]
            end
        end
    end
end,
hd = function (e, a)
    return function ()
        local d, c, _
        _ = 0x7c
        repeat
            if _ <= 124 then
                d = a[1][1][a[1][2]]
                d, _, c = d.GetPivot, 196, d
            else
                d = e.c(d(c))
                return e.d(d)
            end
        until false
    end
end,
Te = function (e, g)
    return function ()
        local d, _, c, b
        _ = 0x68
        repeat
            if _ < 104 then
                c = c(b)
                b = true
                d = c == b
                g[2][1][g[2][2]] = d
                return
            else
                b = g[1][1][g[1][2]]
                _, b, c = 61, g[3][1][g[3][2]], b["RequestHatchEgg"]
            end
        until false
    end
end,
cc = function (e)
    return function (d)
        local b, i, g, j, a, c
        j = 0x9f
        repeat
            if j >= 111 then
                if j >= 169 then
                    if j >= 0xb8 then
                        if j <= 184 then
                            g = d[b]
                            j, c[b] = 0x10a - j, g
                        else
                            b = b(i)
                            i = "table"
                            j = b ~= i and 0x1a2 - j or j + -0xee
                        end
                    elseif j <= 169 then
                        return c
                    else
                        j = a > 0 and j + -0x3c or 88
                    end
                elseif j > 0x9f then
                    j = a ~= a and j + -55 or j + 17
                elseif j < 112 then
                    j = b > i and j + 1 or j + -0x17
                elseif j > 0x70 then
                    b = {}
                    b, i, j, c = e._["type"], d, 249, b
                else
                    return c
                end
            elseif j <= 0x33 then
                if j > 29 then
                    if j <= 0x22 then
                        j = b < i and 112 or 0xda - j
                    else
                        j = a <= 0 and 0x22 or 184
                    end
                elseif j < 0x16 then
                    b, i = 1, #d
                    a = b
                    j = i ~= i and 123 - j or 182 - j
                elseif j <= 22 then
                    j = b > i and 0x70 or 0x55
                else
                    j = b < i and 141 - j or 167
                end
            elseif j <= 85 then
                if j > 0x52 then
                    j = a <= 0 and 0x72 - j or j + 0x52
                else
                    b = b + a
                    j = a > 0 and 0x70c / j or 85
                end
            else
                j = a ~= a and 0xbb0 / j or 51
            end
        until false
    end
end,
td = function (e, a)
    return function ()
        local d
        d = true
        a[1][1][a[1][2]] = d
        return
    end
end,
Eb = function (s, h)
    return function ()
        local a, f, e, r, u, m, d, t, g, k, i, n, _, o, p, j, c, l
        j = 0x39
        while true do
            if j <= 0x8f then
                if j <= 98 then
                    if j > 57 then
                        if j <= 92 then
                            if j <= 0x51 then
                                a, p = c(m, n)
                                n = a
                                j = n == nil and 0xb8 - j or 0x2d3f / j
                            else
                                t = h[2][1][h[2][2]]
                                g, l, i = p["Name"], t["drawEspAt"], "player_"
                                t, k, i = i .. g, s._["string"], _["Position"]
                                e, k, u, g = s._["math"], "%s\n%d studs", p["DisplayName"], k["format"]
                                j, e, o = j + -47, r, e["floor"]
                            end
                        else
                            j = 0x1f02 / j
                            l(t, i, g, k, u)
                        end
                    elseif j >= 0x1b then
                        if j < 0x2d then
                            c = c(m)
                            d = not c
                            j = d and 203 or 132
                        elseif j > 45 then
                            m = h[2][1][h[2][2]]
                            j, m, c = 27, "EspPlayers", m["isOn"]
                        else
                            j, o = j + 77, s.c(o(e))
                        end
                    elseif j <= 10 then
                        i, t = _["Position"], d["Position"]
                        j, l = j + 145, t - i
                        r = l["Magnitude"]
                    else
                        r = d
                        j = r and 10 or 155
                    end
                elseif j >= 132 then
                    if j < 133 then
                        j, c = 289 - j, h[2][1][h[2][2]]
                        d = c["getRoot"]
                    elseif j > 0x85 then
                        f = h[3][1][h[3][2]]
                        j = p ~= f and 0x18b - j or 0xe0 - j
                    else
                        j, _ = 0x17a - j, _(r, l)
                    end
                elseif j >= 122 then
                    if j <= 0x7a then
                        g = g(k, u, s.d(o))
                        j, u = 199, s._["Color3"]
                        u, e, o, k = 0x78, 255, 190, u["fromRGB"]
                    else
                        j, r = j + -35, 0
                    end
                else
                    return
                end
            elseif j > 0xc7 then
                if j >= 244 then
                    if j > 245 then
                        f = p["Character"]
                        _ = f
                        j = _ and 0xf030 / j or 245
                    elseif j > 0xf4 then
                        r = _
                        j = r and 0x1d3 - j or 178
                    else
                        _, j, r, l = f.FindFirstChild, 377 - j, f, "HumanoidRootPart"
                    end
                elseif j <= 203 then
                    return
                else
                    l = h[2][1][h[2][2]]
                    l, j, r = _["Position"], 0x1a3 - j, l["withinEspRange"]
                end
            elseif j >= 0xa7 then
                if j <= 197 then
                    if j > 178 then
                        j, r = 178, r(l)
                    elseif j <= 167 then
                        c, m, n = c(s.d(m))
                        c, m, n = s.b(c, m, n)
                        a, p = c(m, n)
                        n = a
                        j = n == nil and 0x67 or j + -24
                    else
                        j = r and 0x9bc / j or j + -0x61
                    end
                else
                    k = k(u, o, e)
                    j, u = j + -101, f
                end
            elseif j >= 155 then
                if j <= 0x9b then
                    j = r and 0x5c or 282 - j
                else
                    j, d = 153, d()
                    c, m = s._["ipairs"], h[1][1][h[1][2]]
                    n, m = m, m.GetPlayers
                end
            else
                j, m = 0xa7, s.c(m(n))
            end
        end
    end
end,
Dc = function (e, h)
    return function (d)
        local c, a, b, _, f
        _ = 0x87
        repeat
            if _ >= 0x90 then
                if _ <= 163 then
                    if _ > 154 then
                        c = c()
                        b = not c
                        _ = b and 0x9a or 0xcb
                    elseif _ < 145 then
                        _, b = 0x133 - _, h[1][1][h[1][2]]
                        c = b["getPetAreaStandPosition"]
                    elseif _ > 145 then
                        b = false
                        return b
                    else
                        b = h[1][1][h[1][2]]
                        _, c = 171, b["isNearPlot"]
                    end
                elseif _ > 203 then
                    _, b = 122, d
                elseif _ <= 171 then
                    c = c()
                    _ = c and 0x36c6 / _ or 315 - _
                else
                    _, f = 0x51, h[1][1][h[1][2]]
                    a, f, b = true, c, f["travelTo"]
                end
            elseif _ < 0x7a then
                if _ > 82 then
                    _ = c and 0x3656 / _ or 0x91
                elseif _ <= 81 then
                    b = e.c(b(f, a))
                    return e.d(b)
                else
                    c = true
                    return c
                end
            elseif _ >= 130 then
                if _ > 0x82 then
                    c = d
                    _ = c and 0xf4 or 107
                else
                    c = false
                    return c
                end
            else
                _, b = 0x6b, b()
                c = not b
            end
        until false
    end
end,
ed = function (e, h)
    return function ()
        local a, i, d, b, c, _, g
        _ = 0xac
        while true do
            if _ > 113 then
                if _ < 149 then
                    _ = 1
                    c(b, i, a)
                    c = e._["tick"]
                elseif _ > 0x95 then
                    c = h[2][1][h[2][2]]
                    d = c["CurrentCamera"]
                    _ = d and 107 or 0x71
                else
                    _, i = _ + -0x45, i(a, g)
                    a, c, b = d["CFrame"], c.Button2Down, c
                end
            elseif _ <= 0x50 then
                if _ > 0x3d then
                    c(b, i, a)
                    c, _, a = h[1][1][h[1][2]], _ + -0x13, e._["Vector2"]
                    i, a = a["new"], 0
                    g = a
                elseif _ > 1 then
                    i = i(a, g)
                    a, b, _, c = d["CFrame"], c, 145, c.Button2Up
                else
                    c = c()
                    _, h[3][1][h[3][2]] = 113 / _, c
                end
            elseif _ > 107 then
                return
            else
                a, c = e._["Vector2"], h[1][1][h[1][2]]
                a, _, i = 0, 0x95, a["new"]
                g = a
            end
        end
    end
end,
dd = function (b)
    return function ()
        return
    end
end,
ab = function (e, h)
    return function ()
        local b, a, f, c, g, i, _, k, j, d
        j = 133
        while true do
            if j < 112 then
                if j >= 72 then
                    if j <= 0x6c then
                        if j >= 0x61 then
                            if j > 97 then
                                j, b = j + 0x53, b(i, a)
                            else
                                d = nil
                                return d
                            end
                        else
                            c = h[1][1][h[1][2]]
                            j, d = 0xba, c["GetPlotData"]
                        end
                    else
                        j, a = 0x46, a(k, f)
                        i = not a
                    end
                elseif j < 68 then
                    j, a, f = j + 10, b["Position"], e._["Vector3"]
                    _, k, f = 4, f["new"], 0
                    g = f
                elseif j <= 0x44 then
                    k = k(f, _, g)
                    i = a + k
                    return i
                else
                    j = i and 254 - j or 0x80 - j
                end
            elseif j >= 176 then
                if j < 186 then
                    if j <= 0xb0 then
                        b = c
                        j = b and 0x9c or 0x8350 / j
                    else
                        i = nil
                        return i
                    end
                elseif j > 0xba then
                    i = not b
                    j = i and 261 - j or j + -0x2c
                else
                    d = d()
                    c = d
                    j = c and 298 - j or 0x16a - j
                end
            elseif j > 147 then
                j, i, a, b = 0x6c, c, "TreadmillBottom", c.FindFirstChild
            elseif j <= 0x85 then
                if j <= 112 then
                    j, c = 176, d["PlotFolder"]
                else
                    b = h[1][1][h[1][2]]
                    c = b["GetPlotData"]
                    d = not c
                    j = d and 0x61 or 72
                end
            else
                k, f, j, a = b, "BasePart", 0x3f2a / j, b.IsA
            end
        end
    end
end,
he = function (e, a)
    return function ()
        local _, c, d
        _ = 0x67
        while true do
            if _ < 103 then
                d(c)
                return
            else
                d = a[1][1][a[1][2]]
                c, _, d = d, 6, d.Unload
            end
        end
    end
end,
ga = function (e, h)
    return function ()
        local d, c, f, a, _, b
        _ = 0x5b
        while true do
            if _ < 78 then
                if _ > 0x36 then
                    _ = 0x5a - _
                    d(c, b, f, a)
                elseif _ <= 30 then
                    return
                else
                    c = c()
                    d = not c
                    _ = d and 145 or 0x654 / _
                end
            elseif _ > 91 then
                b = e._["os"]
                _, c = _ + -67, b["clock"]
            elseif _ <= 78 then
                c = c()
                b = 0x1e
                _, d = 60, c + b
                h[1][1][h[1][2]], c = d, h[2][1][h[2][2]]
                b, d, c, f, a = "No free egg spots left", c["notify"], "Farm", "Warning", 4
            else
                b = h[2][1][h[2][2]]
                _, c = 0x36, b["isPlotFull"]
            end
        end
    end
end,
Ve = function (e, a)
    return function ()
        local b, d, _, c
        _ = 0x14
        while true do
            if _ > 20 then
                d = e.c(d(c, b))
                return e.d(d)
            else
                _, c = 195, a[2][1][a[2][2]]
                b, d, c = a[3][1][a[3][2]], c["RequestCarryAreaEgg"], a[1][1][a[1][2]]
            end
        end
    end
end,
u = function (e, h)
    return function ()
        local _, f, c, b, d
        _ = 121
        repeat
            if _ > 121 then
                if _ > 0xdf then
                    return
                else
                    d = d(c)
                    b = h[1][1][h[1][2]]
                    c, b = d - b, 5
                    _ = c < b and 0xed or 0x61 / _
                end
            elseif _ > 0x6f then
                _, d = 0xdf, h[2][1][h[2][2]]
                d, c = d.GetServerTimeNow, d
            elseif _ <= 0x5e then
                c(b)
                return
            else
                b, h[1][1][h[1][2]] = h[4][1][h[4][2]], d
                c, _, f = b["netCall"], 94, h[3][1][h[3][2]]
                b = f["Backpack"]
                b = b["EQUIP_BEST"]
            end
        until false
    end
end,
oc = function (e, h)
    return function ()
        local f, a, d, c, _, b
        _ = 0xf7
        while true do
            if _ >= 136 then
                if _ < 204 then
                    if _ <= 0x88 then
                        _, c = 0xc5, 15
                    else
                        b = 60
                        d, _, f = c * b, 0x9cfc / _, e._["os"]
                        b = f["clock"]
                    end
                elseif _ <= 225 then
                    if _ > 0xcc then
                        b = e._["os"]
                        _, c = 11, b["clock"]
                    else
                        b = b()
                        f = h[1][1][h[1][2]]
                        c = b - f
                        _ = c < d and 111 or _ + 0x15
                    end
                else
                    c, f = e._["tonumber"], h[2][1][h[2][2]]
                    _, b, f, a = 1, f["optionValue"], "WebhookInterval", 15
                end
            elseif _ > 89 then
                if _ > 0x6f then
                    c = e.c(c())
                    return e.d(c)
                else
                    c = false
                    return c
                end
            elseif _ > 11 then
                c = c(e.d(b))
                _ = c and 286 - _ or 0x88
            elseif _ <= 1 then
                _, b = 90 - _, e.c(b(f, a))
            else
                c = c()
                h[1][1][h[1][2]], b = c, h[2][1][h[2][2]]
                _, c = 0x85, b["sendSummary"]
            end
        end
    end
end,
Ie = function (e, g)
    return function ()
        local _, d, c, b
        _ = 187
        while true do
            if _ <= 0xbb then
                _, b = 235, e._["settings"]
            else
                b = b()
                c = b["Rendering"]
                d = c["QualityLevel"]
                g[1][1][g[1][2]] = d
                return
            end
        end
    end
end,
Ea = function (s, h)
    return function ()
        local k, t, r, u, a, b, g, p, j, i, l, m, f, o, c, d, n, _, e
        j = 193
        repeat
            if j >= 0x95 then
                if j > 0xc6 then
                    if j >= 0xe8 then
                        if j < 0xf9 then
                            j, o = 0x2c, "Idle"
                        elseif j > 0xf9 then
                            j, u = 0x6eb / j, s.c(u(o))
                        else
                            j = 25
                            r(l, t, i, g, k)
                        end
                    elseif j < 226 then
                        j = r and 402 - j or 0xf9 - j
                    elseif j <= 0xe2 then
                        j, r = j + -159, _
                    else
                        j, g = 0xe0af / j, g(k, u, o)
                        k = p[1][p[2]]
                    end
                elseif j < 193 then
                    if j < 179 then
                        if j > 149 then
                            l = h[2][1][h[2][2]]
                            r, j, i, t = l["drawEspAt"], 0x8580 / j, a["Name"], "guard_"
                            g, l, t = s._["string"], t .. i, _["Position"]
                            k, o, b, g, u, e, i = a["Name"], p[1][p[2]].GetAttribute, "GuardState", "Guard %s\n%s", s._["tostring"], p[1][p[2]], g["format"]
                        else
                            p = p(f, _)
                            j, p = 0xc6, {[2] = 3, [3] = p}
                            p[1] = p
                            f, _ = s._["pcall"], s:xd{p}
                        end
                    elseif j <= 0xb3 then
                        d, c, m = d(s.d(c))
                        d, c, m = s.b(d, c, m)
                        n, a = d(c, m)
                        m = n
                        j = m == nil and 194 or j + -0x59
                    else
                        o = o(e, b)
                        j = o and 44 or 232
                    end
                elseif j > 0xc5 then
                    f, _ = f(_)
                    r = f
                    j = r and j + 28 or j + -0x83
                elseif j <= 194 then
                    if j > 0xc1 then
                        return
                    else
                        m = h[2][1][h[2][2]]
                        j, c, m = 0x45, m["isOn"], "EspGuards"
                    end
                else
                    c = h[1][1][h[1][2]]
                    j, d = 0x422e / j, not c
                end
            elseif j >= 0x45 then
                if j <= 0x5c then
                    if j <= 90 then
                        if j >= 0x56 then
                            if j > 0x56 then
                                f, j, _, p = a, 0x95, "Guard", a.FindFirstChild
                            else
                                j = d and 0x90 or 1
                            end
                        else
                            c = c(m)
                            d = not c
                            j = d and 0x56 or 197
                        end
                    else
                        n, a = d(c, m)
                        m = n
                        j = m == nil and 194 or j + -2
                    end
                elseif j >= 0x90 then
                    if j <= 0x90 then
                        return
                    else
                        j, r = 0x7fc0 / j, r(l)
                    end
                else
                    j, c = 179, s.c(c(m))
                end
            elseif j >= 25 then
                if j > 44 then
                    j = r and j + -45 or 0xe0
                elseif j <= 25 then
                    j = 0x5c
                else
                    j = 0xfd
                end
            elseif j < 7 then
                j, d, c = 0x64 / j, s._["ipairs"], h[1][1][h[1][2]]
                m, c = c, c.GetChildren
            elseif j <= 7 then
                j, i = 0xe7, i(g, k, s.d(u))
                k = s._["Color3"]
                k, u, o, g = 0xff, 0x8c, 90, k["fromRGB"]
            else
                l = h[2][1][h[2][2]]
                l, j, r = _["Position"], j + 124, l["withinEspRange"]
            end
        until false
    end
end,
jd = function (e, h)
    return function ()
        local b, c, k, f, d, _, j, i, a
        j = 47
        repeat
            if j <= 147 then
                if j > 0x6f then
                    if j < 127 then
                        if j > 0x77 then
                            b, j, a, i = c.FindFirstChild, 0x12e - j, "Left", c
                        else
                            f = nil
                            k = a ~= f
                            j = k and 0x16b - j or j + 0x20
                        end
                    elseif j > 127 then
                        k, a, j, i = "Tools", b, 17, b.FindFirstChild
                    else
                        i, b, j, c = "Elements", d, 0x179 - j, d.FindFirstChild
                    end
                elseif j >= 0x4d then
                    if j < 0x55 then
                        d = d(c, b)
                        c = d
                        j = c and j + 50 or 0xfc
                    elseif j > 0x55 then
                        j, a = 0x3399 / j, a(k, f)
                    else
                        a = i
                        j = a and 0x4565 / j or 119
                    end
                elseif j > 17 then
                    j, b, d = 0x4d, "PlayerGui", h[1][1][h[1][2]]
                    c, d = d, d.FindFirstChild
                else
                    j, i = 0x5a5 / j, i(a, k)
                end
            elseif j >= 0xda then
                if j > 0xfa then
                    b = c
                    j = b and 0x7c or 0xda
                elseif j > 244 then
                    j, c = 0xfc, c(b, i)
                elseif j > 0xda then
                    j, _, f = j + -0x5d, true, a["Visible"]
                    k = f == _
                else
                    i = b
                    j = i and 365 - j or j + -0x85
                end
            elseif j < 0xb2 then
                return k
            elseif j > 178 then
                f, j, k, a = "DoubleYourSpeed", 0x5a9f / j, i, i.FindFirstChild
            else
                j, b = j + 0x28, b(i, a)
            end
        until false
    end
end,
Oc = function (e, h)
    return function (d, c, b, i)
        local f, _, k, a, j, g
        j = 181
        while true do
            if j <= 0x83 then
                if j < 53 then
                    if j < 19 then
                        if j <= 0 then
                            j = k and 0x7b or 0x83
                        else
                            k = e.c(k(f, _))
                            return e.d(k)
                        end
                    elseif j <= 0x13 then
                        j = k and 0x11e3 / j or 0x35
                    else
                        j, f = 0x21 - j, f(_, g)
                        k = not f
                    end
                elseif j > 0x77 then
                    if j <= 123 then
                        k = false
                        return k
                    else
                        k = h[1][1][h[1][2]]
                        j, k, a = 0x3ce5 / j, d["AssetCategory"], k["resolveRarity"]
                    end
                elseif j >= 0x71 then
                    if j > 0x71 then
                        a = a(k)
                        _, j, f = a, 0xd7, e._["typeof"]
                    else
                        f, j, a = e._["typeof"], 0x69f0 / j, d["AreaId"]
                        _ = a
                    end
                else
                    f = h[1][1][h[1][2]]
                    f, j, _, k = i, 8, d, f["matchesMutationFilter"]
                end
            elseif j <= 215 then
                if j >= 181 then
                    if j <= 181 then
                        j = c and 113 or 131
                    else
                        f = f(_)
                        _ = "string"
                        k = f ~= _
                        j = k and 0x13 or 153
                    end
                elseif j <= 153 then
                    _ = h[1][1][h[1][2]]
                    j, f, _, g = j + 92, _["selectionAllows"], b, a
                else
                    _ = h[1][1][h[1][2]]
                    j, f, g, _ = 33, _["selectionAllows"], a, c
                end
            elseif j < 241 then
                f = f(_)
                _ = "string"
                k = f ~= _
                j = k and 0 or 0xa5
            elseif j > 241 then
                j, f = 19, f(_, g)
                k = not f
            else
                k = false
                return k
            end
        end
    end
end,
gf = function (e)
    local c, f, d, b
    f = string
    d, c, f = f.char, f.byte, bit32
    b = f.bxor
    d = {[2] = 3, [3] = d}
    d[1] = d
    c = {[2] = 3, [3] = c}
    c[1] = c
    b = {[2] = 3, [3] = b}
    b[1] = b
    f = e:hf{b, d, c}
    return f
end,
ja = function (e, h)
    return function ()
        local g, m, j, a, p, n, i, c, f, _, r, l, d, b, k
        j = 57
        while true do
            if j >= 0x86 then
                if j <= 0xc5 then
                    if j > 0x9b then
                        if j < 193 then
                            if j <= 169 then
                                j = n and 0x78cf / j or j + 24
                            else
                                j = n and j + -0x31 or 41
                            end
                        elseif j <= 193 then
                            j, n = j + -10, not m[1][m[2]]
                        else
                            j, f = 0x4791 / j, e.c(f(_))
                        end
                    elseif j >= 139 then
                        if j > 151 then
                            j, f, p = 0xfa, e:vd{n, m}, e._["pcall"]
                        elseif j <= 0x8b then
                            g, b, j, i = "Tool", l.IsA, 0x5f, l
                        else
                            return
                        end
                    elseif j <= 0x86 then
                        return
                    else
                        j = i and 0x7cd8 / j or 0x7c50 / j
                    end
                elseif j < 0xea then
                    if j < 224 then
                        if j <= 212 then
                            j, n = 169, not c
                        else
                            f, j, _, p = d.GetChildren, 197, d, e._["ipairs"]
                        end
                    elseif j > 224 then
                        j = n[1][n[2]] and 0x9b or 0x31
                    else
                        j, i = 0x7700 / j, b > a
                    end
                elseif j >= 238 then
                    if j <= 0xee then
                        c = c(m, n)
                        j, n = j + -237, h[1][1][h[1][2]]
                        m = n["getHumanoid"]
                    else
                        j = 49
                        p(f)
                    end
                elseif j > 0xea then
                    j, a, n[1][n[2]] = 234, b, l
                else
                    r, l = p(f, _)
                    _ = r
                    j = _ == nil and 220 or 0x8b
                end
            elseif j < 0x39 then
                if j > 0x1e then
                    if j < 41 then
                        k, i = h[1][1][h[1][2]], h[3][1][h[3][2]]
                        j, k, g = 0x1c, l["Name"], k["gearBaseName"]
                    elseif j > 41 then
                        return
                    else
                        j, a, n = 125, -1, nil
                        n = {[2] = 3, [3] = n}
                        n[1] = n
                        p, _, f = e._["ipairs"], c, c.GetChildren
                    end
                elseif j > 0x12 then
                    if j <= 28 then
                        g = g(k)
                        b = i[g]
                        i = b
                        j = i and 99 or 109
                    else
                        r, l = p(f, _)
                        _ = r
                        j = _ == nil and 0x1b12 / j or j + -0x18
                    end
                elseif j >= 6 then
                    if j > 6 then
                        g = g(k)
                        b = i[g]
                        i = b
                        j = i and 0xe0 or 0x9a - j
                    else
                        j, g, i, b = 0x25e / j, "Tool", l, l.IsA
                    end
                else
                    m = m()
                    m = {[2] = 3, [3] = m}
                    m[1] = m
                    n = not d
                    j = n and 0xa9 or 0xd4
                end
            elseif j < 99 then
                if j > 93 then
                    b = b(i, g)
                    j = b and 225 - j or 234
                elseif j > 71 then
                    p, f, _ = p(e.d(f))
                    p, f, _ = e.b(p, f, _)
                    r, l = p(f, _)
                    _ = r
                    j = _ == nil and 0x53eb / j or 6
                elseif j <= 0x39 then
                    c = h[2][1][h[2][2]]
                    j, m, d, c, n = 0xee, c, c["Character"], c.FindFirstChildOfClass, "Backpack"
                else
                    p, f, _ = p(e.d(f))
                    p, f, _ = e.b(p, f, _)
                    r, l = p(f, _)
                    _ = r
                    j = _ == nil and 220 or 139
                end
            elseif j <= 109 then
                if j < 0x65 then
                    j, i = 0x2a27 / j, b >= a
                elseif j > 0x65 then
                    j = i and 151 or 139 - j
                else
                    b = b(i, g)
                    j = b and 36 or 0x1e
                end
            elseif j > 125 then
                k, i = h[1][1][h[1][2]], h[3][1][h[3][2]]
                j, g, k = 18, k["gearBaseName"], l["Name"]
            else
                j, f = 71, e.c(f(_))
            end
        end
    end
end,
nc = function (e, g)
    return function ()
        local b, c, d
        b, d = g[1][1][g[1][2]], g[2][1][g[2][2]]
        c = b["gethui"]
        d["gethui"] = c
        return
    end
end,
Oa = function (e, a)
    return function ()
        local d, _, c
        _ = 0x67
        repeat
            if _ < 0x95 then
                if _ > 0x67 then
                    if _ > 110 then
                        _ = 221
                        d(c)
                        c = a[3][1][a[3][2]]
                        d = c["isDoubleSpeedVisible"]
                    else
                        c = a[3][1][a[3][2]]
                        _, d = 0x2418 / _, c["dismountTreadmill"]
                    end
                elseif _ < 84 then
                    d()
                    _, c = 0x11a2 / _, e._["task"]
                    d, c = c["wait"], 0.1
                elseif _ <= 84 then
                    _ = 0x10e - _
                    d()
                else
                    d = false
                    _, a[2][1][a[2][2]], d, c = 187, d, e._["pcall"], e:Gd{a[1], a[3]}
                end
            elseif _ >= 0xbb then
                if _ <= 0xd0 then
                    if _ <= 0xbb then
                        _ = 336 - _
                        d(c)
                        c = a[3][1][a[3][2]]
                        d = c["isDoubleSpeedVisible"]
                    else
                        _, c = 0x1e10 / _, a[3][1][a[3][2]]
                        d = c["dismountTreadmill"]
                    end
                else
                    d = d()
                    _ = d and 0x6e or 0xba
                end
            elseif _ <= 0x95 then
                d = d()
                _ = d and 0xd0 or 186
            else
                return
            end
        until false
    end
end,
bc = function (e, h)
    return function ()
        local _, c, i, d, a, b
        _ = 0x2b
        while true do
            if _ <= 0x75 then
                if _ < 0x67 then
                    if _ > 0x2b then
                        c = true
                        d["Jump"] = c
                        a = e._["Enum"]
                        i = a["HumanoidStateType"]
                        _, i, c, b = _ + 128, i["Jumping"], d.ChangeState, d
                    else
                        d, _, c = e._["pcall"], 0x67, e:Pe()
                    end
                elseif _ <= 0x67 then
                    d(c)
                    c = h[1][1][h[1][2]]
                    _, d = _ + 0x6c, c["getHumanoid"]
                else
                    return
                end
            elseif _ <= 0xcd then
                _ = 117
                c(b, i)
            else
                d = d()
                _ = d and 0x4d or 0x75
            end
        end
    end
end,
Vd = function (e, g)
    return function (d)
        local c, _, b
        _ = 27
        while true do
            if _ <= 0x1b then
                _, b = 0x3d, g[1][1][g[1][2]]
                c, b = b["applyRendering"], d
            else
                c(b)
                return
            end
        end
    end
end,
Bb = function (e, g)
    return function ()
        local c, d, f, _, b
        _ = 102
        while true do
            if _ < 0x40 then
                if _ <= 1 then
                    d = d(e.d(c))
                    _ = d and 122 or 18 - _
                else
                    _, d = _ + 105, 0x7d0
                end
            elseif _ <= 102 then
                if _ > 64 then
                    b, d = g[1][1][g[1][2]], e._["tonumber"]
                    b, _, f, c = "EspDistance", 0x40, 0x7d0, b["optionValue"]
                else
                    _, c = 64 / _, e.c(c(b, f))
                end
            else
                return d
            end
        end
    end
end,
uc = function (e, g)
    return function ()
        local c, d, b, _
        _ = 225
        while true do
            if _ <= 191 then
                if _ >= 187 then
                    if _ > 187 then
                        return d
                    else
                        c = c()
                        _, d = 191, not c
                    end
                elseif _ > 14 then
                    b = g[2][1][g[2][2]]
                    _, c = 0x6644 / _, b["eggInventoryFull"]
                else
                    _ = d and 0x9a - _ or _ + 0xb1
                end
            elseif _ >= 225 then
                if _ <= 225 then
                    c = g[2][1][g[2][2]]
                    _, d = 247, c["stealingEnabled"]
                else
                    d = d()
                    _ = d and 0xbf0a / _ or 14
                end
            else
                _, c = 0xad4 / _, g[1][1][g[1][2]]
                d = not c
            end
        end
    end
end,
Ob = function (e, h)
    return function ()
        local n, m, a, c, _, d, l, g, j, k, f
        j = 0xfb
        while true do
            if j < 0x5d then
                if j > 25 then
                    if j >= 87 then
                        if j > 90 then
                            j, a = 0xb5 - j, nil
                        elseif j > 87 then
                            n["WaterReflectance"] = a
                            k = {}
                            a = k
                            n["Effects"] = a
                            m = n
                            j, h[2][1][h[2][2]], m, n = 0xb8, m, e._["pcall"], e:Je()
                        else
                            j, a = 107, d["WaterReflectance"]
                        end
                    elseif j < 54 then
                        j, n, m = 0x84, h[1][1][h[1][2]], e._["ipairs"]
                        a, n = n, n.GetDescendants
                    elseif j > 54 then
                        j = a and j + -54 or j + 149
                    else
                        j = 204
                        _(g, l)
                    end
                elseif j < 14 then
                    if j <= 2 then
                        if j <= 1 then
                            j, _ = j + 176, f["Enabled"]
                        else
                            return
                        end
                    else
                        n["WaterWaveSize"] = a
                        a = d
                        j = a and 0x57 or j + 0x62
                    end
                elseif j <= 0x18 then
                    if j >= 0x16 then
                        if j <= 22 then
                            d = d(c, m)
                            j, c = 93, nil
                            c = {[2] = 3, [3] = c}
                            c[1] = c
                            n, m = e:Ie{c}, e._["pcall"]
                        else
                            _(g, l)
                            g = h[6][1][h[6][2]]
                            j, g, _, l = 54, f, g["setEffectEnabled"], false
                        end
                    else
                        m, n, a = m(e.d(n))
                        m, n, a = e.b(m, n, a)
                        k, f = m(n, a)
                        a = k
                        j = a == nil and 199 or 0x96
                    end
                else
                    m = 0
                    j, d["WaterWaveSize"] = 0x33 - j, m
                    d["WaterReflectance"] = m
                end
            elseif j >= 0xb5 then
                if j < 204 then
                    if j >= 184 then
                        if j <= 184 then
                            m(n)
                            m, n = h[5][1][h[5][2]], false
                            m["GlobalShadows"] = n
                            n = 0xf4240
                            m["FogEnd"] = n
                            j = d and 0xd1 - j or 0x1a
                        else
                            n = h[1][1][h[1][2]]
                            j, a, m = 0x138 - j, e:He{h[6], h[3]}, n["DescendantAdded"]
                            n, m = m, m.Connect
                        end
                    else
                        d, m = h[1][1][h[1][2]], "Terrain"
                        c, j, d = d, 0x16, d.FindFirstChildOfClass
                    end
                elseif j < 0xdd then
                    if j <= 204 then
                        k, f = m(n, a)
                        a = k
                        j = a == nil and 199 or 0x96
                    else
                        j, a = 9, nil
                    end
                elseif j <= 221 then
                    j, a = 0x11c - j, d["WaterWaveSize"]
                else
                    d = h[2][1][h[2][2]]
                    j = d and 2 or 181
                end
            elseif j >= 0x84 then
                if j <= 150 then
                    if j <= 0x91 then
                        if j > 132 then
                            g = e._["table"]
                            l, j, _ = h[2][1][h[2][2]], 0xd98 / j, g["insert"]
                            g, l = l["Effects"], f
                        else
                            j, n = j + -118, e.c(n(a))
                        end
                    else
                        g, l = h[3][1][h[3][2]], f["ClassName"]
                        _ = g[l]
                        j = _ and 0x97 - j or j + 27
                    end
                else
                    j = _ and 0x6441 / j or j + 27
                end
            elseif j <= 107 then
                if j <= 93 then
                    m(n)
                    n = {}
                    n["QualityLevel"] = c[1][c[2]]
                    k = h[5][1][h[5][2]]
                    a = k["GlobalShadows"]
                    n["GlobalShadows"] = a
                    a = k["FogEnd"]
                    n["FogEnd"] = a
                    n["Terrain"] = d
                    a = d
                    j = a and 0xdd or 63
                else
                    j = a and 0x5a or j + -0x10
                end
            else
                m = m(n, a)
                h[4][1][h[4][2]] = m
                return
            end
        end
    end
end,
if_ = function (e)
    local f, b, d, c
    f = string
    f, d, c = bit32, f.char, f.byte
    b = f.bxor
    d = {[2] = 3, [3] = d}
    d[1] = d
    c = {[2] = 3, [3] = c}
    c[1] = c
    b = {[2] = 3, [3] = b}
    b[1] = b
    f = e:jf{b, d, c}
    return f
end,
Db = function (e, h)
    return function (d)
        local c, b, _, f
        _ = 235
        repeat
            if _ >= 0xa4 then
                if _ <= 0xd3 then
                    if _ >= 194 then
                        if _ <= 0xc2 then
                            _ = d[1][d[2]] and _ + 17 or 240 - _
                        else
                            f = h[3][1][h[3][2]]
                            _, b = 164, f["buildRenderOverlay"]
                        end
                    else
                        _ = _ + 63
                        b()
                    end
                elseif _ <= 0xe3 then
                    return
                else
                    _, d = 32, {[2] = 3, [3] = d}
                    d[1] = d
                    c, b = e._["pcall"], e:De{d, h[2]}
                end
            elseif _ > 0x2e then
                _ = _ + 77
                b()
            elseif _ > 0x20 then
                f = h[3][1][h[3][2]]
                _, b = 150, f["destroyRenderOverlay"]
            elseif _ <= 0x12 then
                _, h[1][1][h[1][2]] = 212 - _, d[1][d[2]]
            else
                c = c(b)
                _ = c and 0x12 or _ + 162
            end
        until false
    end
end,
o = function (e, h)
    return function (d)
        local f, c, _, b
        _ = 0x1b
        while true do
            if _ > 0x83 then
                if _ > 248 then
                    if _ <= 251 then
                        b = b(f)
                        f = "table"
                        _, c = 58, b == f
                    else
                        _, b = 8, c["DisplayName"]
                    end
                elseif _ > 225 then
                    f = h[1][1][h[1][2]]
                    b, f = f["Directory"], d
                    _ = f and _ + -84 or 0x7ee8 / _
                elseif _ < 0xb8 then
                    c = b[f]
                    b = c
                    _ = b and 0xff or 0x520 / _
                elseif _ <= 0xb8 then
                    c = e.c(c(b))
                    return e.d(c)
                else
                    _ = _ + -41
                end
            elseif _ <= 0x4d then
                if _ < 0x1b then
                    if _ <= 8 then
                        _ = b and _ + 111 or 0x4d
                    else
                        f, b = h[1][1][h[1][2]], e._["typeof"]
                        _, f = 251, f["Directory"]
                    end
                elseif _ >= 58 then
                    if _ > 58 then
                        b, c = d, e._["tostring"]
                        _ = b and 225 or _ + 15
                    else
                        _ = c and 0xf8 or 0x4d
                    end
                else
                    c = h[1][1][h[1][2]]
                    _ = c and 19 or 58
                end
            elseif _ > 0x77 then
                _, f = 0xa4, ""
            elseif _ > 92 then
                b = c["DisplayName"]
                return b
            else
                _, b = 225, "Unknown"
            end
        end
    end
end,
Je = function (e)
    return function ()
        local d, _, c, b, f
        _ = 0xaf
        repeat
            if _ >= 0xaf then
                _, c = 7, e._["settings"]
            else
                c = c()
                d, f = c["Rendering"], e._["Enum"]
                b = f["QualityLevel"]
                c = b["Level01"]
                d["QualityLevel"] = c
                return
            end
        until false
    end
end,
yc = function (e, h)
    return function (d)
        local a, _, c, b, f
        _ = 97
        while true do
            if _ >= 97 then
                _, f = 95, h[1][1][h[1][2]]
                b, a, f = f["getState"], false, d
            else
                b = b(f, a)
                f = true
                c = b == f
                return c
            end
        end
    end
end,
kf = function (e)
    local i, d, a, b, c
    b = string
    d, c = b.char, b.gsub
    d = {[2] = 3, [3] = d}
    d[1] = d
    c = {[2] = 3, [3] = c}
    c[1] = c
    a = bit32
    b, i = a.rshift, a.band
    b = {[2] = 3, [3] = b}
    b[1] = b
    i = {[2] = 3, [3] = i}
    i[1] = i
    a = e:lf{b, c, i, d}
    return a
end,
Me = function (e, h)
    return function ()
        local b, d, i, c, _, a
        _ = 0xb3
        while true do
            if _ <= 0x9a then
                if _ < 0x5e then
                    if _ >= 13 then
                        if _ > 13 then
                            _, c = 0x1c52 / _, c(b)
                            a = e._["Enum"]
                            i = a["HumanoidStateType"]
                            b = i["FallingDown"]
                            d = c == b
                        else
                            c = h[1][1][h[1][2]]
                            c, _, b = c.GetState, 0xf7 - _, c
                        end
                    else
                        c = c(b)
                        a = e._["Enum"]
                        i = a["HumanoidStateType"]
                        b = i["Ragdoll"]
                        d = c == b
                        _ = d and 125 or _ + 86
                    end
                elseif _ <= 125 then
                    if _ <= 94 then
                        c = h[1][1][h[1][2]]
                        b, _, c = c, 0x3a, c.GetState
                    else
                        _ = d and 154 or 0x8a - _
                    end
                else
                    _ = d and _ + 0x30 or _ + 75
                end
            elseif _ >= 0xe4 then
                if _ > 229 then
                    c = c(b)
                    a = e._["Enum"]
                    i = a["HumanoidStateType"]
                    b = i["PlatformStanding"]
                    _, d = _ + -80, c == b
                elseif _ <= 0xe4 then
                    _ = 0xe5
                    d(c, b)
                else
                    return
                end
            elseif _ > 0xb3 then
                i, d = e._["Enum"], h[1][1][h[1][2]]
                b = i["HumanoidStateType"]
                _, d, b, c = 0x1ae - _, d.ChangeState, b["Running"], d
            else
                c = h[1][1][h[1][2]]
                b, _, c = c, 8, c.GetState
            end
        end
    end
end,
Wa = function (e, h)
    return function ()
        local c, b, d, f, _
        _ = 0x5f
        while true do
            if _ > 0x84 then
                if _ > 0xa7 then
                    if _ > 0xb7 then
                        f = d["Position"]
                        b, f = f.Y, 3
                        c = b + f
                        return c
                    else
                        _, c = 0x34, 0x46
                    end
                elseif _ >= 0x96 then
                    if _ <= 150 then
                        _, c = _ + -0x4b, h[1][1][h[1][2]]
                        d = c["getRoot"]
                    else
                        _ = c and 0x21ec / _ or _ + 0x10
                    end
                elseif _ > 139 then
                    _, c = _ + -4, c(b, f)
                else
                    _ = c and 0x7548 / _ or 0x5172 / _
                end
            elseif _ <= 75 then
                if _ < 0x37 then
                    if _ > 0x12 then
                        return c
                    else
                        b = d["Position"]
                        _, c = _ + 149, b.Y
                    end
                elseif _ <= 0x37 then
                    d, b = h[2][1][h[2][2]], "GameplayZ"
                    d, _, c = d.FindFirstChild, 132, d
                else
                    d = d()
                    c = d
                    _ = c and 0x5d - _ or 0xa7
                end
            elseif _ >= 0x82 then
                if _ > 130 then
                    d = d(c, b)
                    c = d
                    _ = c and 130 or 0x8b
                else
                    c, _, f, b = d.IsA, 143, "BasePart", d
                end
            else
                d = h[2][1][h[2][2]]
                _ = d and 0x37 or 150
            end
        end
    end
end,
fb = function (e, h)
    return function (d)
        local a, k, i, f, b, j, _, c
        j = 74
        repeat
            if j <= 87 then
                if j <= 74 then
                    if j > 48 then
                        if j <= 49 then
                            b = true
                            i, h[2][1][h[2][2]] = h[1][1][h[1][2]], b
                            j, b, a, f, i, k = j + 81, i["notify"], "FPS cap is not supported by your executor", 4, "FPS", "Warning"
                        else
                            c = e._["setfpscap"]
                            j = c and 0x96 or 48
                        end
                    elseif j > 30 then
                        c = e._["syn"]
                        j = c and 0xeb or 198 - j
                    elseif j <= 3 then
                        j, _, f = j + 212, 0x168, 15
                    else
                        b = e.c(b(i, e.d(a)))
                        return e.d(b)
                    end
                elseif j >= 0x52 then
                    if j > 82 then
                        i = h[2][1][h[2][2]]
                        b = not i
                        j = b and 136 - j or 0x1bde / j
                    else
                        b = false
                        return b
                    end
                else
                    j, k = 3, 0x3c
                end
            elseif j >= 0xbb then
                if j < 0xd7 then
                    if j > 0xbb then
                        k = k(f)
                        j = k and 0x234 / j or j + -109
                    else
                        k, i, b = e._["math"], c, e._["pcall"]
                        f, j, a, k = d, 0x8954 / j, k["clamp"], e._["tonumber"]
                    end
                elseif j > 0xd7 then
                    j, b = 0x181 - j, e._["syn"]
                    c = b["set_fps_cap"]
                else
                    j, a = 0x1e, e.c(a(k, f, _))
                end
            elseif j < 0x8c then
                j = j + -48
                b(i, a, k, f)
            elseif j > 140 then
                b, j, i = e._["typeof"], j + -10, c
            else
                b = b(i)
                i = "function"
                j = b ~= i and 227 - j or 187
            end
        until false
    end
end,
Oe = function (e, a)
    return function ()
        local _, d, c
        _ = 0xc1
        repeat
            if _ < 0xc1 then
                d(c)
                return
            else
                d = a[1][1][a[1][2]]
                d, _, c = d.Destroy, 7, d
            end
        until false
    end
end,
Pd = function (e, h)
    return function ()
        local i, g, d, a, c, f, j, b
        j = 21
        while true do
            if j < 0x9f then
                if j <= 98 then
                    if j < 0x46 then
                        if j <= 1 then
                            j = j + 160
                            d(c)
                        else
                            c = h[2][1][h[2][2]]
                            d = not c
                            j = d and 92 or 0xfa
                        end
                    elseif j < 0x5c then
                        d(c)
                        c, d = nil, h[4][1][h[4][2]]
--===== [Runtime] Global run / shutdown state flags =====
                        d["__MMB_HUB_RUNNING"] = c
                        c = nil
                        d["__MMB_HUB_SHUTDOWN"] = c
                        return
                    elseif j > 0x5c then
                        d(c)
                        c = h[1][1][h[1][2]]
                        j, c = 0x80, c["destroyRenderOverlay"]
                    else
                        return
                    end
                elseif j <= 124 then
                    if j > 117 then
                        j = 0xf0
                        g(f)
                    elseif j <= 101 then
                        j, d, c = j + -0x64, e._["pcall"], e:ie{h[5]}
                    else
                        j = 0xea
                        d(c)
                        c = e:ee{h[1]}
                    end
                else
                    d(c)
                    c = h[1][1][h[1][2]]
                    j, c = 0x17e - j, c["clearAllEsp"]
                end
            elseif j <= 0xe0 then
                if j < 174 then
                    if j < 161 then
                        j = 229 - j
                        d(c)
                        d, c = e._["pcall"], e:he{h[6]}
                    elseif j <= 0xa1 then
                        c, j, d = h[3][1][h[3][2]], 0xca, e._["ipairs"]
                    else
                        a = {[2] = 3, [3] = a}
                        a[1] = a
                        g, j, f = e._["pcall"], 297 - j, e:fe{a}
                    end
                elseif j <= 0xca then
                    if j > 0xae then
                        d, c, b = d(c)
                        d, c, b = e.b(d, c, b)
                        i, a = d(c, b)
                        b = i
                        j = b == nil and 0xe0 or 0x8882 / j
                    else
                        d(c)
                        j, c = 0x4f86 / j, e:ge{h[1]}
                    end
                else
                    c = h[1][1][h[1][2]]
                    c, j, d = h[3][1][h[3][2]], 383 - j, c["clearTable"]
                end
            elseif j > 250 then
                d(c)
                d = h[5][1][h[5][2]]
                j = d and 0x65 or 161
            elseif j >= 240 then
                if j > 0xf0 then
                    d = false
                    d, h[2][1][h[2][2]], c = e._["pcall"], d, h[1][1][h[1][2]]
                    j, c = 0xae, c["stopTreadmillTraining"]
                else
                    i, a = d(c, b)
                    b = i
                    j = b == nil and 0xd200 / j or 0xa230 / j
                end
            else
                j = 98
                d(c)
                c = h[1][1][h[1][2]]
                c = c["disableFpsBoost"]
            end
        end
    end
end,
xb = function (e, h)
    return function ()
        local l, g, d, _, a, j, m, i, k, f, c
        j = 49
        repeat
            if j >= 0x7a then
                if j < 180 then
                    if j >= 139 then
                        if j <= 171 then
                            if j <= 0x9c then
                                if j <= 139 then
                                    c = false
                                    h[1][1][h[1][2]] = c
                                    return c
                                else
                                    f, _ = k["AreaId"], "Forest"
                                    j = f == _ and 0xb6 or 208
                                end
                            else
                                m = m()
                                i = not m
                                j = i and 213 - j or 177 - j
                            end
                        elseif j > 0xae then
                            a = h[2][1][h[2][2]]
                            a, f, k, j, i = c.X, c.Y, c.Z, 0x68, a["groundedY"]
                        else
                            d = true
                            h[1][1][h[1][2]], c, i, d = d, e._["ipairs"], h[2][1][h[2][2]], nil
                            j, m = 196, i["getAreaEggs"]
                        end
                    elseif j < 0x7f then
                        if j <= 0x7a then
                            d = false
                            return d
                        else
                            return i
                        end
                    elseif j <= 0x7f then
                        a = not i
                        j = a and 50 or 0x3d05 / j
                    else
                        j, k = 180, h[2][1][h[2][2]]
                        k, a = d, k["tryCarryEgg"]
                    end
                elseif j < 231 then
                    if j >= 196 then
                        if j > 208 then
                            j, m = 0x1e, h[2][1][h[2][2]]
                            c, m = m["getSlotEggPosition"], d
                        elseif j <= 0xc4 then
                            j, m = j + -0x66, e.c(m())
                        else
                            a, k = c(m, i)
                            i = a
                            j = i == nil and 319 - j or 156
                        end
                    elseif j <= 0xb4 then
                        a = a(k)
                        i = not a
                        j = i and 219 - j or 0x4650 / j
                    else
                        _ = h[2][1][h[2][2]]
                        _, j, f = k["Uid"], 0x62, _["findEggInstanceByUid"]
                    end
                elseif j >= 235 then
                    if j > 0xf1 then
                        i = i()
                        m = i
                        j = m and j + -0x48 or 389 - j
                    elseif j <= 235 then
                        j, a = 0, h[2][1][h[2][2]]
                        i = a["stealingEnabled"]
                    else
                        j, k = 0x788 / j, h[2][1][h[2][2]]
                        f, a = k, k["stealAlong"]
                        _, f, k = c, m["Position"], f["buildStealPath"]
                    end
                elseif j > 0xe7 then
                    j = 0x8a
                    a(k, e.d(f))
                else
                    a = a(k, f)
                    i = not a
                    j = i and 28 or 9
                end
            elseif j < 50 then
                if j < 0x1c then
                    if j > 8 then
                        j, a = 0xfb, h[2][1][h[2][2]]
                        i = a["getRoot"]
                    elseif j > 6 then
                        k = k(f, _)
                        j, f = 0x738 / j, h[2][1][h[2][2]]
                        f = f["stealingEnabled"]
                    elseif j > 0 then
                        j, i = 0xfc / j, not c
                    else
                        j, i = 127, i()
                    end
                elseif j <= 39 then
                    if j > 0x1e then
                        i = false
                        h[1][1][h[1][2]] = i
                        return i
                    elseif j > 28 then
                        c = c(m)
                        i = h[2][1][h[2][2]]
                        j, m = 0xab, i["getRoot"]
                    else
                        i = false
                        h[1][1][h[1][2]] = i
                        return i
                    end
                elseif j <= 42 then
                    j = i and 160 - j or 0xf1
                else
                    m = h[2][1][h[2][2]]
                    j, c = 0x35, m["stealingEnabled"]
                end
            elseif j <= 98 then
                if j < 0x5b then
                    if j <= 0x35 then
                        if j <= 0x32 then
                            j, a = 0x1806 / j, false
                            h[1][1][h[1][2]] = a
                        else
                            c = c()
                            d = not c
                            j = d and 122 or 0xe3 - j
                        end
                    else
                        i(a)
                        i = h[3][1][h[3][2]]
                        j = i and 0x3192 / j or 127
                    end
                elseif j < 94 then
                    j, f = 0xea, e.c(f(_, g, l))
                elseif j <= 94 then
                    c, m, i = c(e.d(m))
                    c, m, i = e.b(c, m, i)
                    a, k = c(m, i)
                    i = a
                    j = i == nil and 0x28c2 / j or 250 - j
                else
                    f = f(_)
                    d = f
                    j = d and 0x6f or j + 110
                end
            elseif j > 0x6f then
                i = false
                h[1][1][h[1][2]] = i
                return i
            elseif j < 0x68 then
                a = e._["task"]
                i, j, a = a["wait"], 154 - j, 3
            elseif j <= 0x68 then
                i = i(a, k, f)
                k = h[2][1][h[2][2]]
                k, a, _ = m, k["placeRoot"], e._["CFrame"]
                l, f, j, _, g = c.Z, _["new"], 91, c.X, i
            else
                c = not d
                j = c and 0x8b or 0xe3
            end
        until false
    end
end,
wc = function (e, g)
    return function ()
        local d, b, f, c, _
        _ = 141
        repeat
            if _ < 154 then
                if _ > 0x85 then
                    b, d = g[1][1][g[1][2]], e._["tostring"]
                    f, _, c, b = "", 0xbe, b["optionValue"], "WebhookPingId"
                elseif _ >= 28 then
                    if _ > 28 then
                        _, b = 154, e._["string"]
                        f, b, c = d, "<@%s>", b["format"]
                    else
                        c = nil
                        return c
                    end
                else
                    _ = 235
                end
            elseif _ > 197 then
                if _ > 0xce then
                    d = d(c)
                    _, b, f, d, c = 0xc5, "%D", "", d.gsub, d
                else
                    _, c = 0xd7 - _, ""
                end
            elseif _ > 190 then
                d = d(c, b, f)
                c = ""
                _ = d == c and 28 or 330 - _
            elseif _ > 0x9a then
                c = c(b, f)
                _ = c and 0x6ae / _ or 0xce
            else
                c = e.c(c(b, f))
                return e.d(c)
            end
        until false
    end
end,
Xa = function (e, h)
    return function ()
        local a, j, g, b, c, f, i, d
        j = 253
        while true do
            if j > 0x84 then
                if j >= 208 then
                    if j < 233 then
                        if j >= 0xd9 then
                            if j > 217 then
                                j, d = j + -173, h[1][1][h[1][2]]
                            else
                                j = 0x937e / j
                                i(e.d(a))
                            end
                        else
                            i = 0
                            a, h[5][1][h[5][2]] = h[7][1][h[7][2]], i
                            j, a, i = 450 - j, "No matching eggs in this server", a["serverHop"]
                        end
                    elseif j >= 246 then
                        if j > 246 then
                            d = h[2][1][h[2][2]]
                            j = d and 0x33 or 224
                        else
                            j = j + -0x97
                            i(a)
                        end
                    elseif j > 233 then
                        j = 0x7cc8 / j
                        i(a)
                    else
                        i = "After Steal Count"
                        j = d == i and 165 or 0x47
                    end
                elseif j > 168 then
                    if j > 198 then
                        i = 0
                        h[5][1][h[5][2]] = i
                        return
                    elseif j > 174 then
                        b = b()
                        i = "Timed Interval"
                        j = d == i and 45 or 431 - j
                    else
                        return
                    end
                elseif j <= 165 then
                    if j > 153 then
                        i = h[4][1][h[4][2]]
                        j = i >= c and j + -0x43 or 0xae
                    elseif j > 0x88 then
                        j, i = j + 0x2d, e._["os"]
                        b = i["clock"]
                    else
                        j, c = 153, 15
                    end
                else
                    c = c(e.d(b))
                    j = c and j + -15 or 136
                end
            elseif j >= 72 then
                if j >= 0x66 then
                    if j > 0x6b then
                        return
                    elseif j <= 0x69 then
                        if j > 0x66 then
                            a = h[7][1][h[7][2]]
                            j, i, a = 246, a["serverHop"], "Interval reached"
                        else
                            j, a = j + 0x73, e.c(a(g, f))
                        end
                    else
                        j, h[5][1][h[5][2]] = 239 - j, b
                    end
                elseif j <= 0x5f then
                    if j < 86 then
                        c = h[7][1][h[7][2]]
                        d, j, b, c = c["optionValue"], 0x14, h[3][1][h[3][2]], "HopMode"
                        b = b[1]
                    elseif j <= 86 then
                        j, b = 0x3870 / j, e.c(b(i, a))
                    else
                        return
                    end
                else
                    a = h[7][1][h[7][2]]
                    i, j, g = a["serverHop"], 0xc8 - j, e._["string"]
                    g, a, f = "Stole %d eggs", g["format"], h[4][1][h[4][2]]
                end
            elseif j >= 0x2d then
                if j >= 68 then
                    if j <= 68 then
                        a = h[5][1][h[5][2]]
                        i = b - a
                        j = i >= c and j + 140 or j + 0x40
                    else
                        a = h[7][1][h[7][2]]
                        j, i = 29, a["pickStealTarget"]
                    end
                elseif j > 45 then
                    j = d and 30 or 0xe58 / j
                else
                    a = h[6][1][h[6][2]]
                    g, i = 0x3c, b - a
                    a = c * g
                    j = i >= a and 0x1275 / j or 0x10b3 / j
                end
            elseif j <= 29 then
                if j > 20 then
                    i = i()
                    a = nil
                    j = i ~= a and 0x16a8 / j or j + -14
                elseif j > 15 then
                    d = d(c, b)
                    i, c = h[7][1][h[7][2]], e._["tonumber"]
                    a, j, b, i = 15, 0x56, i["optionValue"], "HopValue"
                else
                    i, a = h[5][1][h[5][2]], 0
                    j = i == a and 107 or j + 53
                end
            else
                return
            end
        end
    end
end,
kd = function (e, g)
    return function ()
        local _, d, c, b
        _ = 36
        while true do
            if _ >= 0x56 then
                if _ > 170 then
                    _, c = 64, g[2][1][g[2][2]]
                    d = c["Parent"]
                elseif _ > 96 then
                    c, _, d = g[1][1][g[1][2]], 0, g[3][1][g[3][2]]
                    d["CFrame"] = c
                elseif _ <= 86 then
                    d, b = g[2][1][g[2][2]], g[1][1][g[1][2]]
                    c, _, d = d, 96, d.PivotTo
                else
                    _ = _ + -0x60
                    d(c, b)
                end
            elseif _ < 36 then
                d, b = g[3][1][g[3][2]], e._["Vector3"]
                c = b["zero"]
                d["AssemblyLinearVelocity"] = c
                c = b["zero"]
                d["AssemblyAngularVelocity"] = c
                return
            elseif _ <= 0x24 then
                d = g[2][1][g[2][2]]
                _ = d and 0xda or 0x40
            else
                _ = d and 86 or _ + 0x6a
            end
        end
    end
end,
Rd = function (e, g)
    return function (d)
        local b, _, c
        _ = 0x9c
        repeat
            if _ >= 65 then
                if _ < 156 then
                    return
                elseif _ <= 0x9c then
                    c = not d
                    _ = c and 0xfe or 0x41
                else
                    b = g[1][1][g[1][2]]
                    _, c = _ + -0xbe, b["getHumanoid"]
                end
            elseif _ <= 4 then
                b = false
                _, c["PlatformStand"] = 0x41, b
            else
                c = c()
                _ = c and _ + -0x3c or 0x41
            end
        until false
    end
end,
ne = function (e, a)
    return function ()
        local b, c, _, d
        _ = 80
        repeat
            if _ <= 0x50 then
                b, d = a[1][1][a[1][2]], a[2][1][a[2][2]]
                c, _, d = d, 0x66, d.EquipTool
            else
                d(c, b)
                return
            end
        until false
    end
end,
Jb = function (e, a)
    return function ()
        local d, c
        d, c = a[2][1][a[2][2]], e:Fe{a[1]}
        d["gethui"] = c
        return
    end
end,
tc = function (e, h)
    return function (d, c)
        local b, g, i, a, _
        _ = 129
        repeat
            if _ > 0xa5 then
                if _ <= 186 then
                    b, _, a, g = h[1][1][h[1][2]], 0xe8, d, c
                    i, b = b, b.FireServer
                else
                    b(i, a, g)
                    b = true
                    return b
                end
            elseif _ > 129 then
                b = b(i, a)
                _ = b and 246 - _ or 0x77e2 / _
            elseif _ < 81 then
                b = e.c(b(i, a, g))
                return e.d(b)
            elseif _ <= 81 then
                b, g, a = h[1][1][h[1][2]], c, d
                i, _, b = b, 0x1b, b.InvokeServer
            else
                b, a = h[1][1][h[1][2]], "RemoteFunction"
                b, _, i = b.IsA, 165, b
            end
        until false
    end
end,
Qb = function (e, g)
    return function (d)
        local _, c, b, f
        _ = 34
        while true do
            if _ > 34 then
                c(b, f)
                return d
            else
                _, b = 243, e._["table"]
                c, b, f = b["insert"], g[1][1][g[1][2]], d
            end
        end
    end
end,
Ta = function (e, h)
    return function ()
        local f, n, l, m, c, a, g, j, k, _, d
        j = 0x90
        repeat
            if j <= 110 then
                if j <= 41 then
                    if j <= 33 then
                        if j >= 0x13 then
                            if j >= 0x14 then
                                if j <= 0x14 then
                                    j, g = j + 111, g(l)
                                    l = "string"
                                    _ = g == l
                                else
                                    j, m, n = 0x181b / j, e._["typeof"], d
                                end
                            else
                                m = h[1][1][h[1][2]]
                                j, c = 41, m["GetAreaEggSnapshot"]
                            end
                        elseif j <= 1 then
                            return c
                        else
                            j, m, n = 0xb3, e._["typeof"], d["Records"]
                        end
                    elseif j > 0x26 then
                        j, c = j + -8, c()
                        d = c
                    elseif j <= 35 then
                        if j > 0x22 then
                            j, g = 38, e._["table"]
                            _, l, g = g["insert"], f, c
                        else
                            m = m(n)
                            n = "table"
                            c = m ~= n
                            j = c and 0xdf2 / j or 0x5e
                        end
                    else
                        j = 80
                        _(g, l)
                    end
                elseif j >= 0x66 then
                    if j > 105 then
                        j, g, l = j + 142, e._["typeof"], f
                    elseif j <= 0x68 then
                        if j <= 102 then
                            m, n, a = m(n)
                            m, n, a = e.b(m, n, a)
                            k, f = m(n, a)
                            a = k
                            j = a == nil and 1 or 0x2bd4 / j
                        else
                            j = j + -0x55
                            c(m)
                        end
                    else
                        j = c and 160 or 33
                    end
                elseif j >= 94 then
                    if j > 0x5e then
                        j, m, c = 104, h[1][1][h[1][2]], e._["pcall"]
                        m = m["RequestAreaEggSnapshot"]
                    else
                        m, j, n = e._["typeof"], 0xe2 - j, d["Records"]
                    end
                else
                    k, f = m(n, a)
                    a = k
                    j = a == nil and 0x50 / j or j + 0x1e
                end
            elseif j <= 179 then
                if j > 155 then
                    if j <= 0xaa then
                        if j <= 160 then
                            m = h[1][1][h[1][2]]
                            c = m["RequestAreaEggSnapshot"]
                            j = c and 101 or 19
                        else
                            c = {}
                            d = c
                            return d
                        end
                    else
                        m = m(n)
                        n = "table"
                        j, c = j + 59, m ~= n
                    end
                elseif j < 132 then
                    if j > 112 then
                        j = _ and 166 - j or 0x50
                    else
                        d = d()
                        m, j, n = e._["typeof"], 0x92 - j, d
                    end
                elseif j <= 144 then
                    if j > 0x84 then
                        m = h[1][1][h[1][2]]
                        c = m["GetAreaEggSnapshot"]
                        d = not c
                        j = d and 0xaa or 235
                    else
                        m = m(n)
                        n = "table"
                        j, c = 237 - j, m ~= n
                    end
                else
                    j, g, l = 0xc1c / j, e._["typeof"], f["Uid"]
                end
            elseif j >= 0xeb then
                if j > 238 then
                    g = g(l)
                    l = "table"
                    _ = g == l
                    j = _ and 155 or 131
                elseif j <= 235 then
                    j, c = 0x70, h[1][1][h[1][2]]
                    d = c["GetAreaEggSnapshot"]
                else
                    j = c and 223 or 0xcf
                end
            elseif j < 207 then
                m = m(n)
                n = "table"
                c = m ~= n
                j = c and 0xadda / j or 13
            elseif j > 0xcf then
                m = {}
                c = m
                return c
            else
                j, m = 309 - j, {}
                n, m, c = d["Records"], e._["pairs"], m
            end
        until false
    end
end,
Pb = function (e, h)
    return function (d, c)
        local i, b, _, a
        _ = 176
        while true do
            if _ <= 0xb0 then
                if _ < 136 then
                    if _ > 27 then
                        _, i = 230, 0
                    else
                        i = false
                        return i
                    end
                elseif _ > 136 then
                    i = e._["os"]
                    _, b = 136, i["clock"]
                else
                    b = b()
                    a = h[1][1][h[1][2]]
                    i = a[d]
                    _ = i and 0x7a30 / _ or 0x1760 / _
                end
            elseif _ > 0xca then
                _ = b < i and 0x1842 / _ or 0x1b0 - _
            else
                a, i = b + c, h[1][1][h[1][2]]
                i[d] = a
                i = true
                return i
            end
        end
    end
end,
me = function (e, a)
    return function ()
        local d, c, _
        _ = 0x19
        while true do
            if _ >= 0x72 then
                if _ >= 145 then
                    if _ > 0x91 then
                        _ = 360 - _
                        d()
                    else
                        _, c = _ + 101, a[1][1][a[1][2]]
                        d = c["unload"]
                    end
                else
                    return
                end
            elseif _ <= 0x19 then
                _, d = 0x32, a[2][1][a[2][2]]
                c, d = d, d.Await
            else
                d = d(c)
                _ = d and 145 or _ + 0x40
            end
        end
    end
end,
c = function (...)
    return {[1] = {...}, [2] = select("#", ...)}
end,
Yb = function (e, h)
    return function (d)
        local a, c, i, _, b
        _ = 200
        while true do
            if _ < 0xb0 then
                _, i = 176, e.c(i(a))
            elseif _ <= 176 then
                b = b(e.d(i))
                i = nil
                c = b ~= i
                return c
            else
                b, a = e._["next"], h[1][1][h[1][2]]
                _, i, a = 38, a["multiSelected"], d
            end
        end
    end
end,
I = function (e, g)
    return function (d)
        local b, c, _
        _ = 9
        repeat
            if _ > 154 then
                if _ < 0xc8 then
                    if _ > 0xc6 then
                        b = g[1][1][g[1][2]]
                        c, _, b = b["getZoneLaneCenter"], 0x12, d
                    elseif _ > 176 then
                        c = "Lobby Entry"
                        _ = d == c and _ + -0x32 or 397 - _
                    elseif _ <= 0xa8 then
                        b = g[1][1][g[1][2]]
                        _, c = 0x190 - _, b["getBasePosition"]
                    else
                        c = e.c(c())
                        return e.d(c)
                    end
                elseif _ >= 0xe5 then
                    if _ > 0xe8 then
                        c = "Pet Area"
                        _ = d == c and 100 or 110
                    elseif _ <= 0xe5 then
                        c = "Base"
                        _ = d == c and 0x18d - _ or 248
                    else
                        c = e.c(c())
                        return e.d(c)
                    end
                elseif _ > 200 then
                    _, b = _ + -0x23, g[1][1][g[1][2]]
                    c = b["getTreadmillStand"]
                else
                    c = "Fuse Machine"
                    _ = d == c and 0x5078 / _ or 0x18e - _
                end
            elseif _ > 100 then
                if _ > 0x94 then
                    if _ <= 0x99 then
                        c = e.c(c())
                        return e.d(c)
                    else
                        c = e.c(c())
                        return e.d(c)
                    end
                elseif _ < 0x6e then
                    _, b = 0x3d8f / _, g[1][1][g[1][2]]
                    c = b["getFuseMachinePosition"]
                elseif _ <= 110 then
                    c = "Treadmill"
                    _ = d == c and 0xd3 or _ + 0x5a
                else
                    b = g[1][1][g[1][2]]
                    _, c = 33, b["getEntryPosition"]
                end
            elseif _ >= 33 then
                if _ >= 0x33 then
                    if _ > 0x33 then
                        b = g[1][1][g[1][2]]
                        _, c = _ + 54, b["getPetAreaStandPosition"]
                    else
                        c = nil
                        return c
                    end
                else
                    c = e.c(c())
                    return e.d(c)
                end
            elseif _ >= 0x12 then
                if _ <= 0x12 then
                    c = e.c(c(b))
                    return e.d(c)
                else
                    c = c(b)
                    b = "string"
                    _ = c ~= b and _ + 25 or 0x1742 / _
                end
            else
                c, _, b = e._["typeof"], 26, d
            end
        until false
    end
end,
h = function (e, h)
    return function (d, c, m, n, a)
        local f, _, k, l, j, g
        j = 12
        repeat
            if j > 77 then
                if j > 194 then
                    if j <= 0xfc then
                        k = k(f, _)
                        g, j, f = e._["CFrame"], 329 - j, k["anchor"]
                        g, _ = c, g["new"]
                    else
                        j, f = 0x6b94 / j, k["highlight"]
                        f["Adornee"] = a
                        f = k["highlight"]
                        f["FillColor"] = n
                        f = k["highlight"]
                        f["OutlineColor"] = n
                    end
                elseif j >= 0x97 then
                    if j > 151 then
                        j = f and j + -0xa7 or 246 - j
                    else
                        f = k["highlight"]
                        j, f, _ = 0x1a8b / j, f.Destroy, f
                    end
                elseif j <= 108 then
                    _, f = true, h[3][1][h[3][2]]
                    f[d] = _
                    return
                else
                    j, _ = 31, e._["Instance"]
                    _, f = "Highlight", _["new"]
                end
            elseif j >= 0x2d then
                if j < 52 then
                    if j <= 45 then
                        f(_)
                        f = nil
                        j, k["highlight"] = 0x12fc / j, f
                    else
                        j, f = 194, a["Parent"]
                    end
                elseif j > 0x34 then
                    _ = _(g)
                    f["CFrame"] = _
                    f = k["label"]
                    f["Text"] = m
                    f = k["label"]
                    f["TextColor3"] = n
                    f = a
                    j = f and 126 - j or 194
                else
                    f = k["highlight"]
                    j = f and 0x97 or j + 56
                end
            elseif j <= 0x1b then
                if j > 12 then
                    _ = k["highlight"]
                    f = not _
                    j = f and 176 - j or 0xff
                else
                    f = h[2][1][h[2][2]]
                    f, j, k, _ = d, 252, f["ensureEspEntry"], n
                end
            else
                j, f = 0xff, f(_)
                _ = 0.6
                f["FillTransparency"] = _
                _ = 0
                f["OutlineTransparency"] = _
                l = e._["Enum"]
                g = l["HighlightDepthMode"]
                _ = g["AlwaysOnTop"]
                f["DepthMode"] = _
                _ = h[1][1][h[1][2]]
                f["Parent"] = _
                k["highlight"] = f
            end
        until false
    end
end,
q = function (e, h)
    return function (d)
        local c, n, b, k, l, o, f, a, j, _, m
        j = 164
        repeat
            if j >= 0x81 then
                if j <= 0xc6 then
                    if j > 172 then
                        if j > 193 then
                            if j < 196 then
                                l = l(b)
                                j = l and j + -0x32 or 0x14f - j
                            elseif j <= 0xc4 then
                                a, n = 0, #c
                                j, m = 0x5374 / j, n == a
                            else
                                o = false
                                h[2][1][h[2][2]] = o
                                return o
                            end
                        elseif j >= 0xb9 then
                            if j > 187 then
                                n = h[4][1][h[4][2]]
                                k, n, m, a = d, "Hop", n["notify"], e._["tostring"]
                                j = k and 0x5efe / j or j + -0xb6
                            elseif j > 0xb9 then
                                c = false
                                return c
                            else
                                j = k > f and 0x165 - j or 0xa06e / j
                            end
                        elseif j <= 176 then
                            j = _ ~= _ and j + -4 or 0x3f
                        else
                            j = m and 0x1b1 - j or 0x46
                        end
                    elseif j < 153 then
                        if j >= 139 then
                            if j <= 0x8c then
                                if j <= 0x8b then
                                    n = h[4][1][h[4][2]]
                                    j, m = 319 - j, n["sendSummary"]
                                else
                                    j, b = 0x53ac / j, e._["task"]
                                    b, l = 0.5, b["wait"]
                                end
                            else
                                l = false
                                h[2][1][h[2][2]], l = l, true
                                return l
                            end
                        elseif j <= 129 then
                            o, b = c[k], h[4][1][h[4][2]]
                            j, l, b = 224, b["rememberVisited"], o["id"]
                        else
                            o = o(l, b)
                            _, f = 1, o
                            j = f ~= f and 0x5804 / j or 0x7e65 / j
                        end
                    elseif j < 0x9e then
                        if j > 0x99 then
                            j = _ <= 0 and 118 or 0xb0
                        else
                            j = j + -0x7f
                            l(b)
                        end
                    elseif j <= 164 then
                        if j <= 158 then
                            k = 1
                            j = m > k and 72 or 0xe1
                        else
                            c = h[2][1][h[2][2]]
                            j = c and 23 or 53
                        end
                    else
                        m = m + a
                        j = a > 0 and 0xdc - j or 236
                    end
                elseif j <= 0xe4 then
                    if j > 0xde then
                        if j >= 227 then
                            if j > 0xe3 then
                                n = n()
                                a = 30
                                m = n + a
                                m, h[1][1][h[1][2]] = false, m
                                h[2][1][h[2][2]], n = m, h[4][1][h[4][2]]
                                f, j, a, n, k, m = 4, 0x3c90 / j, "No candidates, retrying in 30s", "Hop", "Warning", n["notify"]
                            else
                                c = c()
                                j, n, a = 0x5a72 / j, e._["typeof"], c
                            end
                        elseif j > 224 then
                            j, l, k = 131, e._["math"], 1
                            b, l, o = 10, #c, l["min"]
                        else
                            j = 195
                            l(b)
                            b = h[4][1][h[4][2]]
                            b, l = o["id"], b["tryTeleportTo"]
                        end
                    elseif j <= 0xd0 then
                        if j < 0xcd then
                            m(n, a, k, f)
                            m = false
                            return m
                        elseif j > 0xcd then
                            j = m < n and 245 or j + -50
                        else
                            j = a > 0 and 0x41 or 0x148 - j
                        end
                    elseif j <= 215 then
                        j = j + -145
                        m(n)
                    else
                        j = _ ~= _ and 85 or 0x45
                    end
                elseif j <= 245 then
                    if j > 0xec then
                        j, a = 0x89d / j, e._["os"]
                        n = a["clock"]
                    elseif j < 0xeb then
                        j = a ~= a and 0xdff2 / j or 0x9e
                    elseif j <= 0xeb then
                        m(n, a, k, f)
                        j, n = 0x4b, h[4][1][h[4][2]]
                        n, m = "WebhookEnabled", n["isOn"]
                    else
                        j = a <= 0 and 0x5034 / j or 234
                    end
                elseif j < 249 then
                    j = _ > 0 and 185 or 222
                elseif j > 249 then
                    j, n = 0x27, h[4][1][h[4][2]]
                    m = n["sendSummary"]
                else
                    _ = e._["os"]
                    j, f = 0x146 - j, _["clock"]
                end
            elseif j <= 0x44 then
                if j < 0x30 then
                    if j < 24 then
                        if j >= 0x15 then
                            if j > 0x15 then
                                j = c and 0xbb or 0x15
                            else
                                c = true
                                h[2][1][h[2][2]], m = c, h[4][1][h[4][2]]
                                j, c = 0xf8 - j, m["pickHopTargets"]
                            end
                        elseif j > 9 then
                            j, k = 0x56a / j, "requested"
                        else
                            n = n()
                            a = 10
                            m = n + a
                            j, m, h[1][1][h[1][2]] = j + 0xc3, false, m
                            n, h[2][1][h[2][2]] = h[4][1][h[4][2]], m
                            m, k, f, a, n = n["notify"], "Warning", 4, "Failed, retrying in 10s", "Hop"
                        end
                    elseif j < 0x27 then
                        if j > 24 then
                            k = k + _
                            j = _ > 0 and j + 0x47 or 155
                        else
                            j = a <= 0 and 0x1380 / j or 158
                        end
                    elseif j <= 39 then
                        m()
                        n = e._["task"]
                        m, j, n = n["wait"], 0x20c1 / j, 0.6
                    else
                        m = m()
                        n = h[1][1][h[1][2]]
                        j, c = 0x17, m < n
                    end
                elseif j <= 0x3f then
                    if j >= 55 then
                        if j >= 57 then
                            if j > 0x39 then
                                l = h[3][1][h[3][2]]
                                o = not l
                                j = o and 0xc6 or j + 0x42
                            else
                                k(f, _, o, l)
                                k = false
                                return k
                            end
                        else
                            f = f(_)
                            _ = "table"
                            k = f ~= _
                            j = k and 0x43 or j + 0x38
                        end
                    elseif j > 48 then
                        j, n = 0x9bb / j, e._["os"]
                        m = n["clock"]
                    else
                        j = m > n and j + 197 or 236
                    end
                elseif j <= 67 then
                    if j <= 0x42 then
                        if j <= 65 then
                            j = m > n and 0xf5 or 123
                        else
                            a = a(k)
                            k, j, f = "Info", 301 - j, 3
                        end
                    else
                        j = k and 249 or 0xe1
                    end
                else
                    m(n, a, k, f)
                    m = false
                    return m
                end
            elseif j <= 0x66 then
                if j <= 0x4d then
                    if j > 72 then
                        if j <= 75 then
                            m = m(n)
                            j = m and j + 64 or j + 105
                        else
                            f = f()
                            _ = 10
                            k = f + _
                            k, j, h[1][1][h[1][2]] = false, 0x39, k
                            f, h[2][1][h[2][2]] = h[4][1][h[4][2]], k
                            l, _, o, k, f = 4, "Failed, retrying in 10s", "Warning", f["notify"], "Hop"
                        end
                    elseif j < 70 then
                        j = _ <= 0 and 0x55 or 0x3f
                    elseif j > 70 then
                        j, f = 0xbd - j, h[4][1][h[4][2]]
                        k = f["pickHopTargets"]
                    else
                        n, m = 3, 1
                        a = m
                        j = n ~= n and 245 or 275 - j
                    end
                elseif j <= 97 then
                    if j >= 87 then
                        if j > 0x57 then
                            j = k > f and 0x412c / j or 155
                        else
                            j = m < n and 245 or 0x4f86 / j
                        end
                    else
                        j = k < f and 172 or 0x3f
                    end
                else
                    n = n(a)
                    a = "table"
                    m = n ~= a
                    j = m and 0x6d or 0xc4
                end
            elseif j <= 117 then
                if j < 0x70 then
                    if j <= 109 then
                        j = m and 0x70 or 193
                    else
                        _, f = 0, #c
                        j, k = j + -0x2c, f == _
                    end
                elseif j > 0x70 then
                    k = k()
                    f, c = e._["typeof"], k
                    j, _ = 172 - j, c
                else
                    j, a = 0x154 - j, e._["os"]
                    n = a["clock"]
                end
            elseif j > 0x7b then
                j = 0xc0 - j
            elseif j <= 118 then
                j = k < f and 172 or 294 - j
            else
                j = a ~= a and 0x63f0 / j or j + -0x63
            end
        until false
    end
end,
F = function (e, h)
    return function ()
        local _, b, f, i, k, d, c, a, j
        j = 191
        repeat
            if j <= 0x4f then
                if j < 62 then
                    if j <= 0x17 then
                        if j < 1 then
                            j = k and j + 0xd6 or 23 - j
                        elseif j <= 1 then
                            f = h[1][1][h[1][2]]
                            k = not f
                            j = k and 0 / j or j + 48
                        else
                            j, k = 214, h[3][1][h[3][2]]
                        end
                    else
                        _ = h[2][1][h[2][2]]
                        j, _, f = 0x46, "AutoSellPets", _["isOn"]
                    end
                elseif j >= 70 then
                    if j > 0x46 then
                        j = j + -17
                        k(f)
                    else
                        j, f = 70 - j, f(_)
                        k = not f
                    end
                elseif j > 62 then
                    j, c = 0xd0, e.c(c())
                else
                    i, a = d(c, b)
                    b = i
                    j = b == nil and 0xfe or 1
                end
            elseif j >= 0xd0 then
                if j < 0xea then
                    if j > 0xd0 then
                        j = k and 0xc39c / j or j + -0x2d
                    else
                        d, c, b = d(e.d(c))
                        d, c, b = e.b(d, c, b)
                        i, a = d(c, b)
                        b = i
                        j = b == nil and 254 or 209 - j
                    end
                elseif j > 234 then
                    return
                else
                    return
                end
            elseif j > 0xb7 then
                d, j, b = e._["ipairs"], 0x43, h[2][1][h[2][2]]
                c = b["getSellablePets"]
            elseif j > 0xa9 then
                k(f)
                f = e._["task"]
                k, j, f = f["wait"], 0x4f, 0.15
            else
                j, f = 0xb7, h[2][1][h[2][2]]
                k, f = f["sellUid"], a
            end
        until false
    end
end,
df = function (e, a)
    return function ()
        local d, _, b, c
        _ = 40
        repeat
            if _ >= 40 then
                c = a[2][1][a[2][2]]
                _, d, b = 18, c["State"], a[1][1][a[1][2]]
                d, c = d.Get, d
            else
                d = e.c(d(c, b))
                return e.d(d)
            end
        until false
    end
end,
Ee = function (e, g)
    return function ()
        local d, _, c, b
        _ = 149
        while true do
            if _ <= 0x95 then
                _, c = 199, e._["settings"]
            else
                c = c()
                b, d = g[1][1][g[1][2]], c["Rendering"]
                c = b["QualityLevel"]
                d["QualityLevel"] = c
                return
            end
        end
    end
end,
Mc = function (e, h)
    return function (d, c)
        local i, b, k, j, f, a
        j = 229
        repeat
            if j >= 0xb7 then
                if j < 229 then
                    if j > 183 then
                        j, a = 0x48bc / j, h[1][1][h[1][2]]
                        i = a["webhookPing"]
                    else
                        i = i(a)
                        b = not i
                        j = b and 238 or j + -0x3b
                    end
                elseif j <= 0xe5 then
                    j, a = 0xb7, h[1][1][h[1][2]]
                    i, a = a["isOn"], "WebhookEnabled"
                else
                    b = false
                    return b
                end
            elseif j >= 124 then
                if j <= 0x7c then
                    a, i = "MMB HUB", {}
                    i["username"] = a
                    f, k = d, {}
                    k[1] = f
                    a = k
                    i["embeds"] = a
                    b = i
                    j = c and 314 - j or 0xa1 - j
                else
                    i = e.c(i(a))
                    return e.d(i)
                end
            elseif j > 37 then
                i = i()
                j, b["content"] = j + -61, i
            else
                a = h[1][1][h[1][2]]
                a, j, i = b, 0x1926 / j, a["httpPost"]
            end
        until false
    end
end,
ve = function (e, a)
    return function ()
        local d, c, _
        _ = 0x6a
        repeat
            if _ <= 0x6a then
                _, d = 0xae, a[1][1][a[1][2]]
                c, d = d, d.Disable
            else
                d(c)
                return
            end
        until false
    end
end,
od = function (e, a)
    return function ()
        local _, c, d
        _ = 187
        while true do
            if _ < 187 then
                d(c)
                return
            else
                c = a[1][1][a[1][2]]
                d = c["_moveTween"]
                _, d, c = 0x60, d.Cancel, d
            end
        end
    end
end,
Lc = function (e)
    return function ()
        local d
        d = 0x320
        return d
    end
end,
Le = function (e, a)
    return function ()
        local d, c
        d, c = a[1][1][a[1][2]], true
        d["Disabled"] = c
        return
    end
end,
cf = function (e, a)
    return function ()
        local d, c, b, _
        _ = 0x40
        while true do
            if _ < 0x5a then
                if _ > 16 then
                    _, b, d = 229, a[1][1][a[1][2]], a[2][1][a[2][2]]
                    d, c = d.SetValue, d
                else
                    return
                end
            elseif _ >= 225 then
                if _ <= 225 then
                    b, d = a[3][1][a[3][2]], a[2][1][a[2][2]]
                    _, d, c = _ + -0x87, d.SetStatus, d
                else
                    d(c, b)
                    d = a[3][1][a[3][2]]
                    _ = d and 0xc945 / _ or 0xf5 - _
                end
            else
                _ = 0x5a0 / _
                d(c, b)
            end
        end
    end
end,
mc = function (e, h)
    return function (d)
        local _, m, c, l, j, o, a, n, f, k, b
        j = 0x5b
        while true do
            if j < 166 then
                if j < 86 then
                    if j >= 33 then
                        if j <= 0x40 then
                            if j <= 0x21 then
                                j, m = 0xa6, e._["http"]
                                c = m["request"]
                            else
                                j = c and 166 or 0xca
                            end
                        else
                            k = false
                            return k
                        end
                    elseif j <= 22 then
                        j, n = 0xce, ""
                    else
                        n = n(a, k)
                        j = n and j + 0xb3 or 22
                    end
                elseif j < 0x87 then
                    if j <= 0x5b then
                        if j <= 86 then
                            n = nil
                            n = {[2] = 3, [3] = n}
                            j, n[1] = 0x35c0 / j, n
                            k, a = e:Xe{h[1], n, d}, e._["pcall"]
                        else
                            d = {[2] = 3, [3] = d}
                            d[1] = d
                            c = e._["syn"]
                            j = c and 0x81 or 64
                        end
                    else
                        j, m = 0x2040 / j, e._["syn"]
                        c = m["request"]
                    end
                elseif j >= 144 then
                    if j > 0x90 then
                        a = a(k)
                        k = not a
                        j = k and j + -90 or 0x19e - j
                    else
                        m = m(n)
                        n = ""
                        j = m == n and 0xe4 or 0x3060 / j
                    end
                else
                    j, c = 310 - j, e._["request"]
                end
            elseif j <= 0xd3 then
                if j < 175 then
                    if j >= 0xa9 then
                        if j <= 169 then
                            j = c and 0x7387 / j or 135
                        else
                            k = e.c(k(f, _))
                            return e.d(k)
                        end
                    else
                        j = c and 0xa9 or 385 - j
                    end
                elseif j > 0xce then
                    m = false
                    return m
                elseif j < 0xca then
                    n, j, m = c, 252, e._["typeof"]
                elseif j > 0xca then
                    j = j + -0x3e
                else
                    c = e._["http"]
                    j = c and 0x1a0a / j or 0xa6
                end
            elseif j > 235 then
                if j <= 252 then
                    m = m(n)
                    n = "function"
                    j = m ~= n and 0xd3 or 0xeb
                else
                    f, _, k = c, {}, e._["pcall"]
                    _["Url"] = m
                    o = "POST"
                    _["Method"] = o
                    b, l = "application/json", {}
                    l["Content-Type"] = b
                    o = l
                    _["Headers"] = o
                    j, _["Body"] = 0xaba6 / j, n[1][n[2]]
                end
            elseif j < 0xe4 then
                j, c = 0xa9, e._["http_request"]
            elseif j <= 0xe4 then
                n = false
                return n
            else
                j, a, m = 0x1b, h[2][1][h[2][2]], e._["tostring"]
                a, n, k = "WebhookUrl", a["optionValue"], ""
            end
        end
    end
end,
Be = function (e)
    return function (d, c)
        local a, i, b
        a, i = c["scale"], d["scale"]
        b = i < a
        return b
    end
end,
R = function (e, h)
    return function (d)
        local b, f, c, a, _
        _ = 179
        while true do
            if _ > 179 then
                c = e.c(c(b, f, a))
                return e.d(c)
            else
                _, b = 231, h[1][1][h[1][2]]
                c, b, f, a = b["glideTo"], d, nil, true
            end
        end
    end
end,
g = function (e)
    return function (d, c, ...)
        local j, m, p, n, i, k, o, l, g, a, b, _, f
        j = 177
        repeat
            if j <= 0x70 then
                if j <= 0x4c then
                    if j > 53 then
                        if j > 0x49 then
                            _, o = a(p, f)
                            f = _
                            j = f == nil and 39 or j + 40
                        else
                            g, k = o, c
                            j = k and 0x8e or 81
                        end
                    elseif j > 52 then
                        l = nil
                        return l
                    elseif j <= 39 then
                        if j <= 0x1e then
                            j, f = j + 100, nil
                        else
                            a = not m
                            j = a and j + 152 or j + 0x7b
                        end
                    else
                        b = b(i, g, k)
                        j, l = 0x33cc / j, b
                    end
                elseif j > 82 then
                    if j <= 103 then
                        j, f = 188, p
                    else
                        l = l(b, i)
                        b = not l
                        j = b and 73 or 0x16f - j
                    end
                elseif j >= 81 then
                    if j > 0x51 then
                        j, b, i, l = j + 0x1e, m, o, m.FindFirstChild
                    else
                        j, k = 0x8e, 4
                    end
                else
                    a, p = a(p, f)
                    f = a
                    j = f and 103 or 0x3a04 / j
                end
            elseif j < 177 then
                if j > 0x8e then
                    j, p, f, a = 0xf1 - j, e._["require"], m, e._["pcall"]
                elseif j <= 130 then
                    if j > 116 then
                        return f
                    else
                        l = not m
                        j = l and 0x35 or 82
                    end
                else
                    j, i, b = 52, m, m.WaitForChild
                end
            elseif j <= 191 then
                if j <= 188 then
                    if j <= 177 then
                        p, a, m = e.c(...), {}, d
                        j = 0xdf
                        e.e(a, 1, e.d(p))
                        n, a = a, e._["ipairs"]
                        p = n
                    else
                        j = f and 0x13e - j or 0x1608 / j
                    end
                else
                    a = nil
                    return a
                end
            elseif j > 0xdf then
                j, m = 0x4bb4 / j, l
            else
                a, p, f = a(p)
                a, p, f = e.b(a, p, f)
                _, o = a(p, f)
                f = _
                j = f == nil and 39 or 116
            end
        until false
    end
end,
Hd = function (e, a)
    return function ()
        local c, _, d
        _ = 119
        while true do
            if _ >= 0x77 then
                c = e._["task"]
                d, _, c = c["spawn"], 0x22, e:_e{a[1]}
            else
                d(c)
                return
            end
        end
    end
end,
je = function (e, h)
    return function ()
        local i, b, a, _, c, d, g
        _ = 241
        repeat
            if _ >= 0xae then
                if _ <= 241 then
                    if _ >= 187 then
                        if _ <= 0xbb then
                            d = d()
                            c = not d
                            _ = c and _ + 0x3b or 0x47
                        else
                            _, c = 187, h[1][1][h[1][2]]
                            d = c["getBasePosition"]
                        end
                    else
                        return
                    end
                else
                    _ = c and 31 or 174
                end
            elseif _ <= 0x1f then
                if _ <= 22 then
                    if _ <= 9 then
                        _, b = 0xf6, b(i, a)
                        c = not b
                    else
                        _ = 0xae
                        c(b, i, a, g)
                    end
                else
                    b = h[1][1][h[1][2]]
                    c, i, g, a, _, b = b["notify"], "Base is not available right now", 3, "Warning", 0x16, "Return"
                end
            else
                _, i = 9, h[1][1][h[1][2]]
                b, i, a = i["travelTo"], d, true
            end
        until false
    end
end,
ma = function (e)
    return function (d, c, m)
        local g, k, _, j, i, f, a
        j = 57
        repeat
            if j > 137 then
                if j > 0xbf then
                    if j > 0xcc then
                        if j <= 217 then
                            a = a(k)
                            j = a and j + 17 or 0x7421 / j
                        else
                            j, k = 0x2be0 / j, false
                        end
                    elseif j < 195 then
                        return k
                    elseif j <= 0xc3 then
                        j, _ = 0x8241 / j, e._["running"]
                        f = not _
                    else
                        j, _ = 0x27, e._["task"]
                        _, f = a, _["wait"]
                    end
                elseif j < 178 then
                    if j <= 0xab then
                        if j <= 138 then
                            f = e._["running"]
                            j = f and 0x148 - j or j + -25
                        else
                            j = f and 0x738f / j or 5
                        end
                    else
                        j = f and 0x826d / j or 0x30
                    end
                elseif j > 0xbe then
                    j, k = j + -173, true
                elseif j >= 0xb3 then
                    if j <= 179 then
                        _ = _()
                        j, f = 352 - j, _ >= i
                    else
                        g = e._["os"]
                        j, _ = 0x13a - j, g["clock"]
                    end
                else
                    j, k = 0x11b - j, 1
                end
            elseif j < 0x57 then
                if j > 39 then
                    if j >= 57 then
                        if j > 57 then
                            a = a()
                            k, j, f = e._["tonumber"], 0x18cf / j, d
                        else
                            j, k = 73, e._["os"]
                            a = k["clock"]
                        end
                    else
                        f = m
                        j = f and j + 48 or j + -0x22
                    end
                elseif j <= 18 then
                    if j >= 14 then
                        if j <= 14 then
                            j = f and 0xa72 / j or j + 124
                        else
                            f = k
                            j = f and j + 153 or j + 177
                        end
                    else
                        j, g = 0xb3, e._["os"]
                        _ = g["clock"]
                    end
                else
                    j = 0x12
                    f(_)
                end
            elseif j > 105 then
                if j < 124 then
                    j = f and 0xcc or 0x12
                elseif j <= 0x7c then
                    _ = _()
                    j, f = 0x71, _ < i
                else
                    j, a = 371 - j, 0.05
                end
            elseif j <= 0x66 then
                if j <= 96 then
                    if j <= 0x57 then
                        k = k(f)
                        j = k and 105 or 178
                    else
                        j, _ = 102, m
                    end
                else
                    _ = _()
                    g = true
                    j, f = 14, _ == g
                end
            else
                i, j, a, k = a + k, j + 112, e._["tonumber"], c
            end
        until false
    end
end,
V = function (e, h)
    return function ()
        local _, p, g, j, i, m, b, c, l, o, a, f, d, k, n
        j = 118
        repeat
            if j >= 79 then
                if j < 0x71 then
                    if j >= 0x55 then
                        if j < 0x5c then
                            if j > 0x55 then
                                j = l and j + -0x47 or 0x5c
                            else
                                n = n(a)
                                j = n and 132 - j or 165 - j
                            end
                        elseif j <= 92 then
                            j = l and 0xe6 - j or 0x8a0 / j
                        else
                            j, i, b = j + -0x12, _, e._["typeof"]
                        end
                    elseif j <= 0x50 then
                        if j > 0x4f then
                            p, j, a = c, 49, e._["pairs"]
                        else
                            b = b(i)
                            i = "string"
                            l = b == i
                            j = l and 0x4c or 0x59
                        end
                    else
                        return m
                    end
                elseif j < 157 then
                    if j > 0x76 then
                        l = n
                        j = l and 24 or 0x1842 / j
                    elseif j <= 0x71 then
                        n = {}
                        j, a, n, m = 157, c, e._["typeof"], n
                    else
                        c = h[1][1][h[1][2]]
                        j, d = 54, c["getSave"]
                    end
                elseif j >= 0xc5 then
                    if j > 197 then
                        j, l = 24, l(b, i, g, k)
                    else
                        a = h[1][1][h[1][2]]
                        j, a, n = 0x4169 / j, "AutoPlaceAll", a["isOn"]
                    end
                elseif j > 0x9d then
                    j, b = 0x59, b(i)
                    i = "table"
                    l = b == i
                else
                    n = n(a)
                    a = "table"
                    j = n ~= a and 4 or 0x78d1 / j
                end
            elseif j > 29 then
                if j < 54 then
                    if j >= 0x2f then
                        if j <= 47 then
                            j, p = 29, h[1][1][h[1][2]]
                            p, a = "AutoPlaceSelected", p["isOn"]
                        else
                            a, p, f = a(p)
                            a, p, f = e.b(a, p, f)
                            _, o = a(p, f)
                            f = _
                            j = f == nil and 0x51 or 0x61
                        end
                    else
                        j, b = 223, h[1][1][h[1][2]]
                        b, i, g, l, k = o, nil, "LifecycleRarities", b["matchesEggFilters"], "LifecycleMutations"
                    end
                elseif j >= 75 then
                    if j > 0x4b then
                        j, b, i = 0x394c / j, e._["typeof"], o
                    else
                        _, o = a(p, f)
                        f = _
                        j = f == nil and j + 6 or 0x1c6b / j
                    end
                else
                    d = d()
                    c = d
                    j = c and 27 or 113
                end
            elseif j < 20 then
                if j > 14 then
                    j, b, i = 0x678 / j, o["Placement"], nil
                    l = b == i
                elseif j > 4 then
                    j = j + 0x3d
                    l(b, i)
                else
                    return m
                end
            elseif j >= 0x1b then
                if j <= 0x1b then
                    j, c = 140 - j, d["EggInventory"]
                else
                    a = a(p)
                    j, n = j + 51, not a
                end
            elseif j <= 0x14 then
                b = e._["table"]
                b, i, j, l = m, _, 14, b["insert"]
            else
                j = l and j + -4 or 0x4b
            end
        until false
    end
end,
_e = function (e, h)
    return function ()
        local b, a, g, d, _, i, c
        _ = 11
        while true do
            if _ <= 0x58 then
                if _ < 0x41 then
                    if _ < 18 then
                        _, c = 0xd4, h[1][1][h[1][2]]
                        d = c["sendSummary"]
                    elseif _ <= 0x12 then
                        _ = i and 0x6a - _ or 0x34 - _
                    else
                        _, i = 0x58, "Send failed"
                    end
                elseif _ >= 82 then
                    if _ > 0x52 then
                        a = d
                        _ = a and 0x14e - _ or 0xac
                    else
                        _, a = 159, "Error"
                    end
                else
                    c(b, i, a, g)
                    return
                end
            elseif _ >= 0xac then
                if _ >= 0xd4 then
                    if _ <= 212 then
                        d = d()
                        b = c
                        i, b, c = d, "Webhook", b["notify"]
                        _ = i and 0x52d0 / _ or 0x12
                    else
                        _, a = 0xac, "Success"
                    end
                else
                    _ = a and 159 or 82
                end
            elseif _ <= 0x64 then
                _, i = 18, "Summary sent"
            else
                _, g = 0xe0 - _, 3
            end
        end
    end
end,
Ue = function (e, g)
    return function ()
        local c, _, b, d
        _ = 168
        repeat
            if _ >= 168 then
                _, b = 11, g[1][1][g[1][2]]
                c, b = b["IsLocalEggReady"], g[3][1][g[3][2]]
            else
                c = c(b)
                b = true
                d = c == b
                g[2][1][g[2][2]] = d
                return
            end
        until false
    end
end,
j = function (e, h)
    return function (d, ...)
        local j, f, _, k, c, b, a, i
        j = 133
        while true do
            if j >= 0x85 then
                if j <= 0xaf then
                    if j <= 0x92 then
                        if j >= 141 then
                            if j > 141 then
                                a(k)
                                j, k = 0x275a / j, h[1][1][h[1][2]]
                                _, k, a, f = e:Tc{i}, 8, k["waitFor"], 0.05
                            else
                                k, a = b[1][b[2]][3], b[1][b[2]][2]
                                return a, k
                            end
                        else
                            d = {[2] = 3, [3] = d}
                            j, d[1] = 175, d
                            b, c = d[1][d[2]], e._["typeof"]
                        end
                    else
                        c = c(b)
                        b = "Instance"
                        j = c ~= b and 0xf8 - j or j + -171
                    end
                elseif j <= 199 then
                    j = a and 0x50d8 / j or 0x6d9b / j
                else
                    c = c(e.d(b))
                    c = {[2] = 3, [3] = c}
                    j, c[1] = 0x8e02 / j, c
                    b = nil
                    b = {[2] = 3, [3] = b}
                    b[1] = b
                    i = false
                    i = {[2] = 3, [3] = i}
                    i[1] = i
                    k = e._["task"]
                    k, a = e:Uc{b, d, i, c}, k["spawn"]
                end
            elseif j > 69 then
                if j <= 0x49 then
                    c = nil
                    return c
                else
                    a = nil
                    return a
                end
            elseif j >= 0x1e then
                if j <= 30 then
                    k, f = b[1][b[2]][1], true
                    j, a = j + 169, k ~= f
                else
                    a(k, f, _)
                    a = not i[1][i[2]]
                    j = a and 268 - j or 30
                end
            else
                b = e._["table"]
                j, c, b = 0x3e4 / j, b["pack"], e.c(...)
            end
        end
    end
end,
zd = function (e, h)
    return function ()
        local c, _, a, i, d, b
        _ = 160
        while true do
            if _ < 0xa0 then
                d(c, b, i, a)
                return
            else
                i, d = e._["game"], h[2][1][h[2][2]]
                a, b = i, i["PlaceId"]
                i, _, a, d, c = a["JobId"], 0x16, h[1][1][h[1][2]], d.TeleportToPlaceInstance, d
            end
        end
    end
end,
Fb = function (e)
    return function (d)
        local f, c, b, a, _
        _ = 2
        repeat
            if _ <= 0x75 then
                if _ < 0x51 then
                    if _ >= 6 then
                        if _ <= 6 then
                            _, c = 0x2be / _, c(b, f)
                        else
                            _, f, a = 0x1b50 / _, d.GetPivot, d
                        end
                    else
                        c, _, f, b = d.FindFirstChild, 168, "Hitbox", d
                    end
                elseif _ <= 0x6a then
                    if _ > 0x51 then
                        _ = c and 0x4bc6 / _ or 0x26
                    else
                        c, b, _, f = d.FindFirstChild, d, 87 - _, "CustomBoundingBox"
                    end
                else
                    _ = c and 0x3072 / _ or 136
                end
            elseif _ < 0xb7 then
                if _ <= 0x88 then
                    _, b, f, c = 388 - _, d, "BasePart", d.FindFirstChildOfClass
                else
                    c = c(b, f)
                    _ = c and _ + -51 or 249 - _
                end
            elseif _ > 184 then
                _, c = 0x6a, c(b, f)
            elseif _ <= 183 then
                b = c["Position"]
                return b
            else
                f = f(a)
                b = f["Position"]
                return b
            end
        until false
    end
end,
G = function (e, a)
    return function ()
        local d, c
        c, d = e:dd(), a[1][1][a[1][2]]
        d["protect_gui"] = c
        return
    end
end,
ee = function (e, a)
    return function ()
        local d, _, c
        _ = 77
        repeat
            if _ > 0x4d then
                d(c)
                return
            else
                c = a[1][1][a[1][2]]
                _, d, c = 157, c["applyRendering"], false
            end
        until false
    end
end,
Sa = function (e, h)
    return function (d, c)
        local _, b, a, f
        _ = 0x9e
        while true do
            if _ < 136 then
                if _ >= 29 then
                    if _ <= 29 then
                        return
                    else
                        _, b = 11, not c
                    end
                else
                    _ = b and 0x13f / _ or _ + 0x7e
                end
            elseif _ > 0x89 then
                b = not d
                _ = b and 11 or 0x86
            elseif _ <= 0x88 then
                b(f, a)
                return
            else
                f = h[1][1][h[1][2]]
                _, f, a, b = 136, d, c, f["placeRoot"]
            end
        end
    end
end,
Bf = {}, W = function (e, h)
    return function (d)
        local i, b, j, c, a, g
        j = 9
        while true do
            if j < 97 then
                if j > 23 then
                    if j < 0x35 then
                        j, b = 0x35, d["Uid"]
                        h[2][1][h[2][2]] = b
                    elseif j <= 0x35 then
                        b = c
                        j = b and 6 or j + -33
                    else
                        i = i(a)
                        a = "table"
                        b = i == a
                        j = b and 0xcc or 23
                    end
                elseif j >= 9 then
                    if j < 0x14 then
                        j, i, b = 5, d, e._["typeof"]
                    elseif j > 20 then
                        j = b and 0x21 or 0x4c3 / j
                    else
                        j = b and 112 or 0xe6
                    end
                elseif j > 5 then
                    i = h[1][1][h[1][2]]
                    j, b = 20, not i
                else
                    b = b(i)
                    i = "table"
                    c = b == i
                    j = c and 0x6a or 0x3d9 / j
                end
            elseif j >= 0xc5 then
                if j >= 0xd9 then
                    if j >= 230 then
                        if j <= 0xe6 then
                            h[1][1][h[1][2]] = c
                            return
                        else
                            i()
                            i = h[4][1][h[4][2]]
                            j = i and 0x5bb2 / j or j + -12
                        end
                    else
                        j = 447 - j
                        i(a)
                    end
                elseif j > 0xc5 then
                    a, j, i = d["Uid"], 381 - j, e._["typeof"]
                else
                    j, a, i = j + -101, d, e._["typeof"]
                end
            elseif j > 112 then
                i = i(a)
                j, a = 0x17, "string"
                b = i == a
            elseif j <= 106 then
                if j > 0x61 then
                    i, b = true, d["IsCarrying"]
                    j, c = 197, b == i
                else
                    j, a, i = j + 120, d, h[4][1][h[4][2]]
                end
            else
                j, a, g = 0xf2, h[5][1][h[5][2]], 1
                i = a + g
                h[5][1][h[5][2]], a = i, h[3][1][h[3][2]]
                i = a["setStolen"]
            end
        end
    end
end,
Bc = function (e, h)
    return function (d)
        local c, f, _, a, b
        _ = 30
        repeat
            if _ >= 0x60 then
                if _ > 0x9c then
                    if _ <= 0xd1 then
                        f, c, a = d, h[1][1][h[1][2]], true
                        _, b, c = _ + -0xa5, c, c.FindFirstChild
                    else
                        b = b(f)
                        f = "string"
                        c = b ~= f
                        _ = c and 156 or 136
                    end
                elseif _ < 0x88 then
                    if _ > 0x60 then
                        c, f = h[2][1][h[2][2]], d
                        c, _, b = c.FindFirstChild, 96, c
                    else
                        c = c(b, f)
                        _ = c and _ + -81 or 0xd1
                    end
                elseif _ <= 0x88 then
                    _, b = 0x52e0 / _, ""
                    c = d == b
                else
                    _ = c and 0x25 or 185 - _
                end
            elseif _ <= 0x1e then
                if _ > 29 then
                    _, f, b = 0xdf, d, e._["typeof"]
                elseif _ > 15 then
                    c = h[2][1][h[2][2]]
                    _ = c and 108 or _ + 180
                else
                    return c
                end
            elseif _ <= 37 then
                c = nil
                return c
            else
                c = e.c(c(b, f, a))
                return e.d(c)
            end
        until false
    end
end,
Sd = function (e, a)
    return function ()
        local c, _, d
        _ = 227
        repeat
            if _ < 227 then
                d(c)
                return
            else
                c = e._["task"]
                d, _, c = c["spawn"], 0x4a, e:ke{a[1]}
            end
        until false
    end
end,
Wc = function (e, h)
    return function ()
        local i, b, j, d, c, g, a
        j = 151
        while true do
            if j >= 0x97 then
                if j > 151 then
                    d(c, e.d(b))
                    d = true
                    return d
                else
                    d, i = h[2][1][h[2][2]], e._["table"]
                    i, a, j, b = h[1][1][h[1][2]], 1, 0x63, i["unpack"]
                    g = i
                    g = g.n
                end
            else
                b = e.c(b(i, a, g))
                c, j, d = d, 282 - j, d.FireServer
            end
        end
    end
end,
_b = function (e, a)
    return function ()
        local b, c, d, _
        _ = 105
        repeat
            if _ > 151 then
                if _ > 0xd6 then
                    _, d = 0x6f, a[1][1][a[1][2]]
                    d, c = d.InvokeServer, d
                else
                    d = d(c, b)
                    _ = d and 0xf6 or 151
                end
            elseif _ <= 0x87 then
                if _ <= 0x6f then
                    if _ > 105 then
                        d = e.c(d(c))
                        return e.d(d)
                    else
                        d, b = a[1][1][a[1][2]], "RemoteFunction"
                        c, _, d = d, 214, d.IsA
                    end
                else
                    d(c)
                    return
                end
            else
                d = a[1][1][a[1][2]]
                c, _, d = d, 0x4fa1 / _, d.FireServer
            end
        until false
    end
end,
Md = function (e, g)
    return function (d)
        local b, c, _
        _ = 0
        repeat
            if _ <= 175 then
                if _ < 108 then
                    if _ <= 0 then
                        _ = d and 0xdc or 0x62
                    else
                        b = g[1][1][g[1][2]]
                        _, c = 0x6c, b["disableFpsBoost"]
                    end
                elseif _ > 0x6c then
                    return
                else
                    _ = 0xaf
                    c()
                end
            elseif _ > 220 then
                _ = 0xaf
                c()
            else
                b = g[1][1][g[1][2]]
                _, c = 453 - _, b["enableFpsBoost"]
            end
        until false
    end
end,
ia = function (e)
    return function (d)
        local n, c, m, k, f, _, o, b, j, l, a
        j = 0xde
        while true do
            if j > 118 then
                if j <= 0xb5 then
                    if j <= 174 then
                        if j > 0xa6 then
                            a = 0x3e8
                            j = c >= a and 217 or j + -85
                        elseif j > 0x7f then
                            l, n, f, o, a, k, b, _ = "Qa", {}, "M", "T", "", "K", "Qi", "B"
                            n[1], n[2], n[3], n[4], n[5], n[6], n[7] = a, k, f, _, o, l, b
                            m, a, n = n, 0x3e8, 1
                            j = c >= a and j + -148 or 179
                        else
                            a = e.c(a(k, f, _))
                            return e.d(a)
                        end
                    elseif j > 179 then
                        c = c(m)
                        j = c and 166 or 27
                    else
                        a = 0x3e8
                        j = c >= a and 226 or 174
                    end
                elseif j >= 0xde then
                    if j <= 0xde then
                        m, j, c = d, 181, e._["tonumber"]
                    else
                        j, a = j + -52, 0x3e8
                        c, n = c / a, 3
                    end
                elseif j > 0xc8 then
                    j, a = 0x4b71 / j, 0x3e8
                    c, n = c / a, 4
                else
                    a = 0x3e8
                    j = c >= a and 0x3e80 / j or j + -0xb1
                end
            elseif j >= 55 then
                if j >= 0x59 then
                    if j > 94 then
                        k = e._["string"]
                        k, f, j, a, _ = "%.2f%s", c, 127, k["format"], m[n]
                    elseif j > 0x59 then
                        j, k = 22, e._["string"]
                        a, k, f = k["format"], "%d", c
                    else
                        a = 0x3e8
                        j = c >= a and 0x45 or 200
                    end
                elseif j >= 69 then
                    if j <= 69 then
                        j, a = 0xc8, 0x3e8
                        c, n = c / a, 5
                    else
                        j, a = 23, 0x3e8
                        n, c = 6, c / a
                    end
                else
                    j, a = 0x1f, 0x3e8
                    c, n = c / a, 7
                end
            elseif j > 0x17 then
                if j > 0x1b then
                    a = 1
                    j = n == a and 94 or 0x95 - j
                else
                    j, c = 0x1182 / j, 0
                end
            elseif j > 0x16 then
                a = 0x3e8
                j = c >= a and 78 - j or 31
            elseif j > 18 then
                a = e.c(a(k, f))
                return e.d(a)
            else
                a = 0x3e8
                n, j, c = 2, 179, c / a
            end
        end
    end
end,
Kc = function (e, h)
    return function (d)
        local g, i, _, a, j, f, c, b, k
        j = 4
        repeat
            if j >= 0x92 then
                if j <= 197 then
                    if j <= 0xa3 then
                        if j >= 0x9e then
                            if j > 158 then
                                b = h[1][1][h[1][2]]
                                b, c = not d, b["Character"]
                                j = b and 85 or 0x649a / j
                            else
                                j, b = 0x55, not c
                            end
                        else
                            j, a, b, i = 197, c, e._["ipairs"], c.GetDescendants
                        end
                    elseif j <= 0xae then
                        b(i)
                        return
                    else
                        j, i = 0x8b, e.c(i(a))
                    end
                elseif j <= 0xd8 then
                    if j <= 0xd2 then
                        return
                    else
                        a, j, b = h[4][1][h[4][2]], j + -0xa5, c["DescendantAdded"]
                        i, b = b, b.Connect
                    end
                else
                    g, j, _ = f, 97, h[4][1][h[4][2]]
                end
            elseif j <= 0x5a then
                if j >= 73 then
                    if j < 0x55 then
                        c, j, b = e._["pcall"], 207 - j, e:ff{h[2]}
                    elseif j > 85 then
                        k, f = b(i, a)
                        a = k
                        j = a == nil and 306 - j or j + 151
                    else
                        j = b and 0xd2 or 146
                    end
                elseif j > 4 then
                    b = b(i, a)
                    h[2][1][h[2][2]], i = b, h[3][1][h[3][2]]
                    i, j, b = h[2][1][h[2][2]], 0xae, i["track"]
                else
                    c = h[2][1][h[2][2]]
                    j = c and 0x49 or 163
                end
            elseif j >= 134 then
                if j <= 134 then
                    c(b)
                    j, c = 0x5552 / j, nil
                    h[2][1][h[2][2]] = c
                else
                    b, i, a = b(e.d(i))
                    b, i, a = e.b(b, i, a)
                    k, f = b(i, a)
                    a = k
                    j = a == nil and 216 or 380 - j
                end
            else
                j = 0x221a / j
                _(g)
            end
        until false
    end
end,
Gd = function (e, g)
    return function ()
        local c, b, _, d
        _ = 127
        while true do
            if _ > 127 then
                d(c)
                return
            else
                _, c = 0xb1, g[2][1][g[2][2]]
                d, b = c["netInvoke"], g[1][1][g[1][2]]
                c = b["Treadmills"]
                c = c["REQUEST_UNEQUIP"]
            end
        end
    end
end,
ge = function (e, a)
    return function ()
        local d, _, c
        _ = 64
        repeat
            if _ <= 64 then
                c = a[1][1][a[1][2]]
                d, _, c = c["applyAntiGameplayPause"], 186, false
            else
                d(c)
                return
            end
        until false
    end
end,
fc = function (e, h)
    return function (d)
        local g, a, j, c, i, b
        j = 247
        repeat
            if j > 197 then
                if j < 246 then
                    if j > 198 then
                        return b
                    else
                        i = nil
                        return i
                    end
                elseif j > 246 then
                    i = h[1][1][h[1][2]]
                    b = i["Deserialize"]
                    c = not b
                    j = c and 5 or 0x58
                else
                    j = i and j + -48 or 0xdfe6 / j
                end
            elseif j >= 88 then
                if j >= 0x70 then
                    if j <= 112 then
                        a = a(g)
                        j, g = 0xf6, "table"
                        i = a ~= g
                    else
                        c, b = c(b, i)
                        i = not c
                        j = i and j + 0x31 or 9
                    end
                else
                    c, j, i = e._["pcall"], 0xc5, h[1][1][h[1][2]]
                    i, b = d, i["Deserialize"]
                end
            elseif j > 5 then
                a, j, g = e._["typeof"], 0x3f0 / j, b
            else
                c = nil
                return c
            end
        until false
    end
end,
Gf = function (a, b, c, d)
    a.Ff[d] = a.gf(b, c)
    return a.Ff[d]
end,
Ba = function (s, h)
    return function (d)
        local b, q, g, k, _, l, f, j, m, i, p, c, a, n, r, o
        j = 72
        while true do
            if j <= 0x96 then
                if j > 0x48 then
                    if j < 0x7e then
                        if j > 0x59 then
                            return i
                        else
                            j = g and 0x29b8 / j or 0x3426 / j
                        end
                    elseif j <= 0x7e then
                        g = g(k, q)
                        j = g and 232 or j + -37
                    else
                        b, i = _(r, l)
                        l = b
                        j = l == nil and 0x3e or 0x9f6 / j
                    end
                elseif j <= 0x27 then
                    if j < 17 then
                        _, r, l = _(s.d(r))
                        _, r, l = s.b(_, r, l)
                        b, i = _(r, l)
                        l = b
                        j = l == nil and 310 / j or j + 12
                    elseif j > 0x11 then
                        a = s.c(a(p, f))
                        m[1] = n
                        j = 178
                        s.e(m, 2, s.d(a))
                        m, c = s._["ipairs"], m
                        n = c
                    else
                        g, j, k, q = i.IsA, j + 109, i, "Tool"
                    end
                elseif j <= 0x3e then
                    p, f = m(n, a)
                    a = p
                    j = a == nil and 0xdb or 0x109 - j
                else
                    m, a = {}, h[1][1][h[1][2]]
                    n, j, p, a, f = a["Character"], 0x27, a, a.FindFirstChildOfClass, "Backpack"
                end
            elseif j < 203 then
                if j <= 178 then
                    if j <= 0xa8 then
                        j, k = j + -79, k(q, o)
                        g = k == d
                    else
                        m, n, a = m(n)
                        m, n, a = s.b(m, n, a)
                        p, f = m(n, a)
                        a = p
                        j = a == nil and 219 or 381 - j
                    end
                else
                    _, j, r, l = s._["ipairs"], j + 0x16, f.GetChildren, f
                end
            elseif j > 0xdb then
                o, k, j, q = "UID", i.GetAttribute, 0xa8, i
            elseif j >= 204 then
                if j <= 204 then
                    j, r = j + -0xc7, s.c(r(l))
                else
                    m = nil
                    return m
                end
            else
                j = f and 0xb6 or 0x312a / j
            end
        end
    end
end,
De = function (e, g)
    return function ()
        local _, c, d, b
        _ = 0x89
        while true do
            if _ <= 0x89 then
                b, d = g[1][1][g[1][2]], g[2][1][g[2][2]]
                _, d, b, c = 0xa7, d.Set3dRenderingEnabled, not b, d
            else
                d(c, b)
                return
            end
        end
    end
end,
Nc = function (e, h)
    return function (d)
        local c, f, b, _
        _ = 0x32
        repeat
            if _ > 0x93 then
                if _ < 173 then
                    if _ <= 157 then
                        _, b = 0x5a27 / _, c["highlight"]
                        f, b = b, b.Destroy
                    else
                        _ = 103
                        b(f)
                    end
                elseif _ <= 0xb8 then
                    if _ <= 173 then
                        b = c["highlight"]
                        _ = b and 0x9d or 0x73
                    else
                        _, b = 121, c["anchor"]
                        b, f = b.Destroy, b
                    end
                else
                    b, f = h[1][1][h[1][2]], nil
                    b[d] = f
                    return
                end
            elseif _ < 114 then
                if _ <= 0x3f then
                    if _ <= 50 then
                        b = h[1][1][h[1][2]]
                        c = b[d]
                        b = not c
                        _ = b and 114 or 173
                    else
                        _, b = 168, c["billboard"]
                        b, f = b.Destroy, b
                    end
                else
                    b = c["anchor"]
                    _ = b and 0xb8 or 253
                end
            elseif _ > 121 then
                _ = _ + -32
                b(f)
            elseif _ >= 0x73 then
                if _ > 115 then
                    _ = 0xfd
                    b(f)
                else
                    b = c["billboard"]
                    _ = b and 0x3f or 0x2e45 / _
                end
            else
                return
            end
        until false
    end
end,
pe = function (e, g)
    return function ()
        local d, c, _, b
        _ = 0x5b
        repeat
            if _ < 172 then
                if _ <= 0x5b then
                    b, c = true, g[2][1][g[2][2]]
                    d = c == b
                    _ = d and 0xc9 or 0xac
                else
                    _, d = 0xc9, d(c)
                end
            elseif _ <= 0xac then
                _, c = 268 - _, g[1][1][g[1][2]]
                d, c = c["isOn"], "AutoFusePets"
            else
                return d
            end
        until false
    end
end,
ac = function (e, h)
    return function ()
        local k, _, m, j, c, i, d, g, a, f
        j = 0xdf
        while true do
            if j >= 174 then
                if j > 193 then
                    if j > 0xc7 then
                        d, m = h[2][1][h[2][2]], "ClientRenderedAssets"
                        d, j, c = d.FindFirstChild, 0x28, d
                    else
                        j, m, i, c = 192, d.GetChildren, d, e._["ipairs"]
                    end
                elseif j <= 192 then
                    if j >= 177 then
                        if j <= 0xb1 then
                            c, m, i = c(e.d(m))
                            c, m, i = e.b(c, m, i)
                            a, k = c(m, i)
                            i = a
                            j = i == nil and j + 0x10 or 0xa1
                        else
                            j, m = 0x171 - j, e.c(m(i))
                        end
                    else
                        return
                    end
                else
                    return
                end
            elseif j <= 151 then
                if j >= 137 then
                    if j <= 0x89 then
                        j = 164
                        f(_)
                    else
                        j, _, f = 288 - j, e:Oe{k}, e._["pcall"]
                    end
                elseif j <= 15 then
                    f = f(_, g)
                    g = h[1][1][h[1][2]]
                    _ = g["UserId"]
                    j = f == _ and 0x97 or j + 149
                else
                    d = d(c, m)
                    c = not d
                    j = c and 0x1b30 / j or 0x1f18 / j
                end
            elseif j <= 0xa1 then
                k = {[2] = 3, [3] = k}
                j, k[1] = 0x96f / j, k
                f, g, _ = k[1][k[2]].GetAttribute, "OwnerUserId", k[1][k[2]]
            else
                a, k = c(m, i)
                i = a
                j = i == nil and j + 0x1d or 0xa1
            end
        end
    end
end,
rc = function (e, g)
    return function (d)
        local c, f, _, b
        _ = 15
        repeat
            if _ > 0x7e then
                f, _, c = d, _ + -5, g[1][1][g[1][2]]
                b, c = c, c.FindFirstChild
            elseif _ <= 0x34 then
                if _ > 15 then
                    return c
                else
                    c = g[1][1][g[1][2]]
                    _ = c and 0x83 or 52
                end
            else
                _, c = 0x1998 / _, c(b, f)
            end
        until false
    end
end,
Ne = function (e, a)
    return function ()
        local c, d, b, _
        _ = 0xee
        while true do
            if _ < 238 then
                d(c, b)
                return
            else
                _, d, b = 180, a[2][1][a[2][2]], a[1][1][a[1][2]]
                c, d = d, d.PivotTo
            end
        end
    end
end,
qe = function (e, g)
    return function ()
        local b, c, d, _
        _ = 148
        while true do
            if _ > 0x94 then
                if _ <= 0xd0 then
                    _, d = _ + -0x5b, d(e.d(c))
                    g[1][1][g[1][2]] = d
                else
                    _, c = 0xd0, e.c(c(b))
                end
            elseif _ > 0x75 then
                c = g[2][1][g[2][2]]
                d = c["GetSlotOwner"]
                _ = d and 17 or 117
            elseif _ > 0x11 then
                return
            else
                c = g[2][1][g[2][2]]
                b, _, c, d = g[3][1][g[3][2]], 0xec, e._["tonumber"], c["GetSlotOwner"]
                b = b["Name"]
            end
        end
    end
end,
va = function (s, h)
    return function ()
        local _, n, a, r, t, e, b, d, l, k, g, i, j, m, c, p, f, u, v
        j = 116
        repeat
            if j < 0x83 then
                if j > 49 then
                    if j <= 103 then
                        if j >= 0x55 then
                            if j <= 95 then
                                if j <= 0x55 then
                                    e = s.c(e(b))
                                    v, j, u = u, 0xd6, u.ToObjectSpace
                                else
                                    j = r < l and 7 or j + 67
                                end
                            else
                                c = h[1][1][h[1][2]]
                                j, d = j + 0x94, c["GetPlotData"]
                            end
                        elseif j <= 0x39 then
                            j, k = 0x16, s.c(k(u, v, e))
                            i, g = i.PointToWorldSpace, i
                        else
                            j = 221 - j
                            g(k, s.d(u))
                        end
                    elseif j >= 0x77 then
                        if j > 119 then
                            j = _ ~= _ and j + 115 or 10
                        else
                            c = {}
                            d = c
                            return d
                        end
                    elseif j > 106 then
                        m = h[1][1][h[1][2]]
                        c = m["GetPlotData"]
                        d = not c
                        j = d and 119 or 0x67
                    else
                        j = p < f and 0xeb or 139
                    end
                elseif j < 33 then
                    if j <= 20 then
                        if j <= 10 then
                            if j <= 7 then
                                p = p + _
                                j = _ > 0 and 138 - j or 227 - j
                            else
                                j = _ <= 0 and j + 0xe2 or 265 - j
                            end
                        else
                            j = t <= 0 and j + 75 or 0xb6 - j
                        end
                    elseif j > 0x16 then
                        j = _ > 0 and 0x31 or 0x79
                    else
                        j, i = 0x74e / j, i(g, s.d(k))
                        k = s._["table"]
                        u, g, b, k = m["CFrame"], k["insert"], s._["CFrame"], a
                        b, e = i, b["new"]
                    end
                elseif j <= 0x2e then
                    if j < 42 then
                        j, m = j + 0xb9, d["PetArea"]
                        c = not m
                    elseif j > 0x2a then
                        j = t > 0 and 153 or j + 86
                    else
                        m = {}
                        c = m
                        return c
                    end
                elseif j <= 0x2f then
                    j = t ~= t and 0x149 / j or 0xd1 - j
                else
                    j = p > f and j + 0xba or 121
                end
            elseif j <= 0xb9 then
                if j < 0x99 then
                    if j > 0x8b then
                        if j <= 0x8c then
                            j = c and 0xb6 - j or j + 2
                        else
                            m, c = d["CenterPoint"], d["PetArea"]
                            p, n = {}, c["Size"]
                            a, t = p, n.X
                            t, l = 0.5, -t
                            l, r = 5, l * t
                            l, p = n.X, r + l
                            l, r = 5, l * t
                            _, f = 7, r - l
                            j = f ~= f and 235 or 29
                        end
                    elseif j > 0x84 then
                        j = _ ~= _ and 235 or 0xff
                    elseif j <= 0x83 then
                        j = p > f and 0xeb or 0x7094 / j
                    else
                        j = t ~= t and 95 or j + -112
                    end
                elseif j < 163 then
                    if j <= 0x99 then
                        j = r > l and 160 - j or 0x11d - j
                    else
                        i, j, u = c["CFrame"], 0x39, s._["Vector3"]
                        e, u, v, k = r, p, 1, u["new"]
                    end
                elseif j >= 179 then
                    if j <= 0xb3 then
                        j = r < l and 7 or 0x20dd / j
                    else
                        j = t <= 0 and 0xb3 or 0xe8 - j
                    end
                else
                    r = r + t
                    j = t > 0 and 0xde or 185
                end
            elseif j < 0xde then
                if j > 0xda then
                    j = _ <= 0 and 106 or 139
                elseif j >= 214 then
                    if j > 214 then
                        j = c and 0x166 - j or 421 - j
                    else
                        j, u = 58, s.c(u(v, s.d(e)))
                    end
                else
                    j, m = 0x8c, d["CenterPoint"]
                    c = not m
                end
            elseif j > 236 then
                if j > 251 then
                    k = n.Z
                    g, k = -k, 0.5
                    i, g = g * k, 5
                    r, g = i + g, n.Z
                    g, i = 5, g * k
                    l, t = i - g, 7
                    j = l ~= l and 262 - j or 46
                else
                    d = d()
                    c = not d
                    j = c and 0x1d5 - j or 284 - j
                end
            elseif j > 235 then
                j = p < f and 0xeb or 255
            elseif j <= 0xde then
                j = r > l and 0x612 / j or 0xa06e / j
            else
                return a
            end
        until false
    end
end,
gc = function (e, h)
    return function (d, c)
        local n, m, f, _, o, l, b, i, p, j, a
        j = 138
        repeat
            if j < 138 then
                if j > 0x44 then
                    if j >= 0x6f then
                        if j < 0x76 then
                            j, p, a = 0x15f - j, m, e._["typeof"]
                        elseif j > 118 then
                            j, f = 0xc3, f(_)
                        else
                            _, o = a(p, f)
                            f = _
                            j = f == nil and 0x161 - j or 206
                        end
                    elseif j <= 77 then
                        f, j, _ = e._["tonumber"], 0x24b2 / j, p
                    else
                        i = nil
                        return i
                    end
                elseif j < 53 then
                    if j <= 19 then
                        if j <= 7 then
                            p = h[2][1][h[2][2]]
                            j, a = 0xa3, p["CalculateFusePrice"]
                            n = not a
                        else
                            j, f = 0xc9, nil
                        end
                    else
                        a, p = a(p, f)
                        f = a
                        j = f and 0x4d or 230 - j
                    end
                elseif j <= 0x3a then
                    if j <= 0x35 then
                        i = not b
                        j = i and 97 or j + 196
                    else
                        j, m = 0x1926 / j, d["Inventory"]
                    end
                else
                    n = nil
                    return n
                end
            elseif j > 218 then
                if j < 239 then
                    if j > 219 then
                        j, a, f = 0x10e - j, e._["pcall"], h[2][1][h[2][2]]
                        f, p = n, f["CalculateFusePrice"]
                    else
                        j, a = 0xda, {}
                        a, n, p = e._["ipairs"], a, c
                    end
                elseif j <= 0xf0 then
                    if j <= 239 then
                        j, b = 0x124 - j, b(i)
                    else
                        a = a(p)
                        p = "table"
                        n = a ~= p
                        j = n and 163 or 7
                    end
                else
                    j, n[_] = 118, b
                end
            elseif j >= 0xc3 then
                if j < 0xce then
                    if j > 195 then
                        return f
                    else
                        j = f and 0xc9 or 214 - j
                    end
                elseif j <= 0xce then
                    l = m[o]
                    b = l
                    j = b and 0x90d8 / j or 53
                else
                    a, p, f = a(p)
                    a, p, f = e.b(a, p, f)
                    _, o = a(p, f)
                    f = _
                    j = f == nil and 235 or 424 - j
                end
            elseif j > 0xa3 then
                i = h[1][1][h[1][2]]
                j, b, i = 0xef, i["getPetItemData"], l
            elseif j <= 0x8a then
                m = d
                j = m and 0x3a or 0x6f
            else
                j = n and 0x2b4c / j or 0xdb
            end
        until false
    end
end,
Vc = function (e, h)
    return function ()
        local a, d, i, g, b, c, j
        j = 10
        repeat
            if j <= 107 then
                if j > 10 then
                    b = e.c(b(i, a, g))
                    j, d, c = 0x12c - j, d.InvokeServer, d
                else
                    d, i = h[2][1][h[2][2]], e._["table"]
                    a, i, b = 1, h[1][1][h[1][2]], i["unpack"]
                    j, g = 107, i
                    g = g.n
                end
            else
                d = e.c(d(c, e.d(b)))
                return e.d(d)
            end
        until false
    end
end,
Jd = function (e, a)
    return function ()
        local c, _, d
        _ = 6
        repeat
            if _ <= 6 then
                c = e._["task"]
                _, c, d = 239, e:be{a[2], a[1]}, c["spawn"]
            else
                d(c)
                return
            end
        until false
    end
end,
U = function (e, h)
    return function ()
        local c, a, j, i, f, d, k, _, b
        j = 0x65
        while true do
            if j <= 84 then
                if j <= 0x30 then
                    if j < 0x25 then
                        if j < 0x18 then
                            _, j, k = h[3][1][h[3][2]], 141 - j, e._["pcall"]
                            _, f = a, _["RequestEquipTool"]
                        elseif j <= 24 then
                            d, c, b = d(e.d(c))
                            d, c, b = e.b(d, c, b)
                            i, a = d(c, b)
                            b = i
                            j = b == nil and 0x780 / j or 0x54
                        else
                            j = k and 202 or 0x196e / j
                        end
                    elseif j <= 45 then
                        if j > 0x25 then
                            j, f = 0x286e / j, e._["task"]
                            f, k = 0.15, f["wait"]
                        else
                            j, c = 24, e.c(c())
                        end
                    else
                        j = k and j + -18 or 181
                    end
                elseif j < 80 then
                    if j <= 0x41 then
                        f = f(_)
                        j, k = 0xc30 / j, not f
                    else
                        i, a = d(c, b)
                        b = i
                        j = b == nil and 0x1680 / j or 0x17a0 / j
                    end
                elseif j > 80 then
                    f = h[1][1][h[1][2]]
                    k = not f
                    j = k and j + -0x24 or 0x112 - j
                else
                    return
                end
            elseif j >= 0xb5 then
                if j <= 202 then
                    if j < 190 then
                        j, k = 0x1e, h[4][1][h[4][2]]
                    elseif j <= 190 then
                        _ = h[2][1][h[2][2]]
                        j, _, f = 0x41, "AutoSellEggs", _["isOn"]
                    else
                        return
                    end
                elseif j > 0xd9 then
                    k(f)
                    f = h[2][1][h[2][2]]
                    j, f, k = 144, a, f["sellUid"]
                else
                    f = h[3][1][h[3][2]]
                    k = f["RequestEquipTool"]
                    j = k and 18 or 0x2625 / j
                end
            elseif j <= 144 then
                if j <= 123 then
                    if j <= 0x65 then
                        b, j, d = h[2][1][h[2][2]], 37, e._["ipairs"]
                        c = b["getSellableEggUids"]
                    else
                        j = j + -78
                        k(f, _)
                    end
                else
                    j = j + 19
                    k(f)
                    f = e._["task"]
                    f, k = 0.15, f["wait"]
                end
            else
                j = 0x48
                k(f)
            end
        end
    end
end,
Ia = function (e, h)
    return function (d)
        local g, b, j, i, a, c
        j = 0x5a
        while true do
            if j >= 139 then
                if j <= 240 then
                    if j > 0x8b then
                        j, b = 132, b()
                        h[1][1][h[1][2]] = b
                    else
                        j, b = j + 101, e._["tick"]
                    end
                else
                    j = b and j + -0x6a or 0x179 - j
                end
            elseif j <= 0x5a then
                if j > 0x52 then
                    g, c = e._["Enum"], d["UserInputType"]
                    a = g["UserInputType"]
                    i = a["MouseMovement"]
                    b = c == i
                    j = b and 0xf5 or 0x52
                else
                    g = e._["Enum"]
                    a = g["UserInputType"]
                    i = a["Gamepad1"]
                    j, b = 0x147 - j, c == i
                end
            else
                return
            end
        end
    end
end,
qc = function (s)
    return function ()
        local p, f, r, i, g, e, n, j, u, d, t, l, c, a, m, _, o, k
        j = 0x8d
        repeat
            if j < 124 then
                if j < 0x3e then
                    if j < 0x11 then
                        if j <= 14 then
                            if j < 13 then
                                j, _ = j + 168, true
                            elseif j > 13 then
                                j, d = 0x7c, d(c)
                                m, c = d, s._["type"]
                            else
                                _, j, f = p, j + 0x40, s._["typeof"]
                            end
                        else
                            d = d(c)
                            c = "function"
                            j = d ~= c and 136 or 21
                        end
                    elseif j > 0x15 then
                        if j <= 0x23 then
                            return
                        else
                            j = 0x3e
                            k(u, o)
                        end
                    elseif j > 0x12 then
                        j, c, d = 35 - j, true, s._["getgc"]
                    elseif j > 17 then
                        u, k, j, e, o = p, s._["setmetatable"], 0x2a, s:Ye(), {}
                        o["__newindex"] = e
                    else
                        j, f = 0xf02 / j, true
                    end
                elseif j > 87 then
                    if j > 99 then
                        o, j, u = g, 205, s._["typeof"]
                    elseif j < 92 then
                        i, g = r(l, t)
                        t = i
                        j = t == nil and 0x3e94 / j or 237
                    elseif j > 0x5c then
                        r, l, t = r(l)
                        r, l, t = s.b(r, l, t)
                        i, g = r(l, t)
                        t = i
                        j = t == nil and 0x3e or 0x70
                    else
                        j = k and 0x12 or 0x41
                    end
                elseif j <= 77 then
                    if j > 0x4a then
                        f = f(_)
                        _ = "table"
                        j = f == _ and 0xcb or 62
                    elseif j <= 0x41 then
                        if j <= 62 then
                            a, p = c(m, n)
                            n = a
                            j = n == nil and 35 or 13
                        else
                            i, g = r(l, t)
                            t = i
                            j = t == nil and 0x3e or 112
                        end
                    else
                        j = k and j + 0x75 or j + 0x12
                    end
                elseif j <= 78 then
                    r, j, l = s._["pairs"], 0xb1 - j, p
                else
                    r, l, t = r(l)
                    r, l, t = s.b(r, l, t)
                    i, g = r(l, t)
                    t = i
                    j = t == nil and 0x3d2c / j or j + 150
                end
            elseif j >= 0xbf then
                if j >= 0xe2 then
                    if j <= 0xef then
                        if j > 0xed then
                            return
                        elseif j <= 0xe2 then
                            _ = not f
                            j = _ and 0x188 - j or 0x3e
                        else
                            j = g == p and 0xf9 - j or 89
                        end
                    elseif j <= 0xf5 then
                        u = 3
                        j, k = 74, g <= u
                    else
                        r, j, _ = p, 0x95, s._["getrawmetatable"]
                    end
                elseif j >= 203 then
                    if j <= 205 then
                        if j <= 203 then
                            f, j, l, r = false, 210, s._["getrawmetatable"], s._["type"]
                        else
                            u = u(o)
                            o = "number"
                            k = u == o
                            j = k and 0x7c1f / j or 0x9a
                        end
                    else
                        r = r(l)
                        l = "function"
                        _ = r == l
                        j = _ and 0xfd or 0x76f2 / j
                    end
                elseif j > 191 then
                    c, j, m = s._["pairs"], 0x98, d
                else
                    j, o, u = 92, nil, p[g]
                    k = u == o
                end
            elseif j < 152 then
                if j < 141 then
                    if j > 124 then
                        return
                    else
                        c = c(m)
                        m = "table"
                        j = c ~= m and 0xef or 195
                    end
                elseif j >= 0x91 then
                    if j > 145 then
                        j, _ = 0x5465 / j, _(r)
                    else
                        j = _ and 0x11 or 371 - j
                    end
                else
                    d, j, c = s._["type"], 16, s._["getgc"]
                end
            elseif j < 0x9b then
                if j > 0x98 then
                    j = k and j + 0x5b or 0x4a
                else
                    c, m, n = c(m)
                    c, m, n = s.b(c, m, n)
                    a, p = c(m, n)
                    n = a
                    j = n == nil and 0x23 or 0x7b8 / j
                end
            elseif j <= 0xa6 then
                if j > 155 then
                    l, r, j, _ = p, s._["pairs"], 0x386a / j, false
                else
                    u = 1
                    j, k = 154, g >= u
                end
            else
                j = _ and 0x4e or 0x2b98 / j
            end
        until false
    end
end,
be = function (e, a)
    return function ()
        local c, d, _
        _ = 0x54
        repeat
            if _ <= 84 then
                _, d = 213, 0
                c, a[2][1][a[2][2]] = a[1][1][a[1][2]], d
                c, d = "Manual hop", c["serverHop"]
            else
                d(c)
                return
            end
        until false
    end
end,
gd = function (e, a)
    return function ()
        local b, d, c, _
        _ = 7
        repeat
            if _ > 7 then
                d(c, b)
                return
            else
                b, d = a[1][1][a[1][2]], a[2][1][a[2][2]]
                _, d, c = 0xb6, d.SetValue, d
            end
        until false
    end
end,
ze = function (e, a)
    return function ()
        local c, d, _
        _ = 62
        repeat
            if _ > 62 then
                return
            elseif _ <= 11 then
                _, c, d = 0xad, a[3][1][a[3][2]], a[2][1][a[2][2]]
                d["CFrame"] = c
            else
                c, d = a[1][1][a[1][2]], a[2][1][a[2][2]]
                d["CameraSubject"] = c
                d = a[3][1][a[3][2]]
                _ = d and 11 or 173
            end
        until false
    end
end,
vc = function (e)
    return function (d)
        local b, i, _, k, a, c, j
        j = 232
        while true do
            if j <= 201 then
                if j >= 0x8a then
                    if j >= 0x9f then
                        if j <= 0x9f then
                            return c
                        else
                            k = b(i, a)
                            a = k
                            j = a == nil and 360 - j or 0xfa
                        end
                    else
                        c = c(b)
                        b = "table"
                        j = c ~= b and 0x79d4 / j or 85
                    end
                elseif j > 0x23 then
                    j, c, b, i = 0xb9f / j, 0, e._["pairs"], d
                else
                    b, i, a = b(i)
                    b, i, a = e.b(b, i, a)
                    k = b(i, a)
                    a = k
                    j = a == nil and 194 - j or 0x222e / j
                end
            elseif j <= 0xe8 then
                if j <= 226 then
                    c = 0
                    return c
                else
                    b, j, c = d, 138, e._["typeof"]
                end
            else
                _ = 1
                j, c = 0xc9, c + _
            end
        end
    end
end,
N = function (s, h)
    return function ()
        local d, g, m, y, u, a, c, f, t, A, n, k, e, z, i, _, l, v, b, o, p, j, q, r, x
        j = 0x49
        repeat
            if j >= 123 then
                if j >= 180 then
                    if j >= 0xe1 then
                        if j <= 0xea then
                            if j < 0xe7 then
                                if j <= 225 then
                                    e = e(b)
                                    b = "table"
                                    j = e == b and j + -15 or 32
                                else
                                    j, g = 250, g(k)
                                end
                            elseif j > 231 then
                                j = e and 350 - j or 0x9240 / j
                            else
                                j, g = 359 - j, i
                            end
                        elseif j < 0xf3 then
                            a, z, f = a(s.d(z))
                            a, z, f = s.b(a, z, f)
                            _, r = a(z, f)
                            f = _
                            j = f == nil and j + -0xdf or j + -0x5e
                        elseif j <= 243 then
                            j = g and 231 or 371 - j
                        else
                            j = g and 123 or 16
                        end
                    elseif j >= 210 then
                        if j > 215 then
                            j = 16
                            q(o, x, m, u, p)
                        elseif j > 0xd2 then
                            A, d = "ClientRenderedAssets", h[1][1][h[1][2]]
                            d, j, c = d.FindFirstChild, 0xb9, d
                        else
                            e = not g
                            j = e and 0xd2 / j or 234
                        end
                    elseif j >= 185 then
                        if j <= 0xb9 then
                            d = d(c, A)
                            c = not d
                            j = c and 155 or 0x5037 / j
                        else
                            j = 0x1f
                            a(z)
                            f, a, z = d, s._["ipairs"], d.GetChildren
                        end
                    else
                        j, m = 174, s.c(m(u))
                    end
                elseif j > 149 then
                    if j < 170 then
                        if j > 0xa0 then
                            b = b(q, o, s.d(x))
                            j = k and 0x46ae / j or 0x68
                        elseif j <= 155 then
                            return
                        else
                            e, j, b = s._["tonumber"], 0xd4 - j, v["MoneyPerSecond"]
                        end
                    elseif j >= 174 then
                        if j <= 174 then
                            q = q(o, x, s.d(m))
                            j, b = 0x68, q
                        else
                            j, l = 0x4fb6 / j, l(t, i)
                            i, t = s:hd{r}, s._["pcall"]
                        end
                    else
                        k = k(y)
                        y = "string"
                        g = k == y
                        j = g and j + -140 or j + 0x49
                    end
                elseif j > 0x87 then
                    if j <= 0x92 then
                        if j > 0x91 then
                            r = {[2] = 3, [3] = r}
                            j, r[1] = 0x6616 / j, r
                            i, t, l = "UID", r[1][r[2]], r[1][r[2]].GetAttribute
                        else
                            j, m = 0x87, "?"
                        end
                    else
                        u = u(p)
                        j, p = 0xd8, r[1][r[2]]
                    end
                elseif j > 0x84 then
                    j = 0x6b
                elseif j <= 0x80 then
                    if j > 0x7b then
                        j = g and 0x9c - j or 0xfa
                    else
                        g, k, v, y = nil, nil, s._["typeof"], A[l]
                        j, e = j + -47, y
                    end
                else
                    c = c(A)
                    d = not c
                    j = d and 0x1ef0 / j or 0x6edc / j
                end
            elseif j > 50 then
                if j <= 104 then
                    if j < 73 then
                        if j > 0x38 then
                            return
                        elseif j <= 0x34 then
                            e = e(b)
                            j, k = j + -0x14, e
                        else
                            j, g = 78, y["Category"]
                        end
                    elseif j >= 0x4e then
                        if j <= 0x4e then
                            v, e = n[1][n[2]][l], s._["typeof"]
                            j, b = 303 - j, v
                        else
                            o = h[2][1][h[2][2]]
                            q, m, x = o["drawEspAt"], r[1][r[2]]["Name"], "pet_"
                            o, j, x, m, p = x .. m, 0xfd - j, i["Position"], b, h[2][1][h[2][2]]
                            p, u = e, p["espColorFor"]
                        end
                    elseif j <= 73 then
                        A = h[2][1][h[2][2]]
                        A, j, c = "EspPets", 0x84, A["isOn"]
                    else
                        v = v(e)
                        e = "table"
                        j = v == e and 0x10a0 / j or 78
                    end
                elseif j >= 0x6f then
                    if j <= 114 then
                        if j <= 111 then
                            A = h[2][1][h[2][2]]
                            j, c = 0x2d, A["getSave"]
                        else
                            t, i = t(i)
                            j, k, y = 170, s._["typeof"], l
                        end
                    else
                        e = v["ItemData"]
                        j, g = 0xa0, e["Category"]
                    end
                elseif j > 0x6b then
                    o = s._["string"]
                    x, o, q, u = b, "%s\n%s/s", o["format"], h[2][1][h[2][2]]
                    j, m, u = 0x4ca4 / j, u["formatNumber"], k
                else
                    j, x = j + 0x3b, s.c(x(m))
                end
            elseif j >= 0x1e then
                if j <= 44 then
                    if j > 0x20 then
                        j, A = j + -15, c["Inventory"]
                    elseif j > 31 then
                        j, b = 0x32, h[2][1][h[2][2]]
                        e, b = b["resolveRarity"], g
                    elseif j <= 30 then
                        j, g = 243, t
                    else
                        j, z = 0xf0, s.c(z(f))
                    end
                elseif j < 0x30 then
                    c = c()
                    A = c
                    j = A and 0x2c or 0x4a - j
                elseif j <= 0x30 then
                    j, a = 205, {}
                    n = a
                    n = {[2] = 3, [3] = n}
                    n[1] = n
                    z, a = s:id{n, h[3]}, s._["pcall"]
                else
                    e = e(b)
                    q = s._["string"]
                    x, q, b = h[2][1][h[2][2]], "%s [%s]", q["format"]
                    x, j, o = g, 6, x["assetName"]
                end
            elseif j > 17 then
                if j < 28 then
                    j, n = 48, {}
                    A = n
                elseif j > 0x1c then
                    j = A and 48 or 0x1b
                else
                    k = h[2][1][h[2][2]]
                    g, j, k = k["withinEspRange"], j + 202, i["Position"]
                end
            elseif j < 16 then
                if j > 1 then
                    o = o(x)
                    x, m = s._["tostring"], e
                    j = m and 135 or 145
                else
                    j, e = 235 - j, v["ItemData"]
                end
            elseif j > 16 then
                return
            else
                _, r = a(z, f)
                f = _
                j = f == nil and 0x110 / j or 146
            end
        until false
    end
end,
k = function (e)
    return function (d)
        local j, m, i, _, a, k, g, f, c
        j = 185
        while true do
            if j >= 161 then
                if j > 0xbd then
                    if j >= 226 then
                        if j > 227 then
                            g = "BodyGyro"
                            j, _ = 189, f == g
                        elseif j > 0xe2 then
                            g, j, _ = e:Xc{k}, 262 - j, e._["pcall"]
                        else
                            c, i, j, m = e._["ipairs"], d, 0xb2, d.GetChildren
                        end
                    elseif j <= 0xc1 then
                        j = _ and 0x17e - j or 246
                    else
                        j = _ and 39 or 63
                    end
                elseif j <= 0xb9 then
                    if j > 178 then
                        c = not d
                        j = c and 0xa6 or 226
                    elseif j < 0xa6 then
                        k = {[2] = 3, [3] = k}
                        k[1] = k
                        g, f = "BodyVelocity", k[1][k[2]]["ClassName"]
                        _ = f == g
                        j = _ and 0xc1 or 287 - j
                    elseif j <= 0xa6 then
                        return
                    else
                        j, m = 0x37a0 / j, e.c(m(i))
                    end
                elseif j <= 188 then
                    return
                else
                    j = _ and 0xa0f2 / j or j + -0x97
                end
            elseif j >= 0x50 then
                if j > 126 then
                    if j <= 158 then
                        g = "AlignOrientation"
                        j, _ = 0x42a8 / j, f == g
                    else
                        a, k = c(m, i)
                        i = a
                        j = i == nil and 188 or j + 2
                    end
                elseif j >= 110 then
                    if j <= 0x6e then
                        j = _ and 0x6c or 0x9e
                    else
                        g = "BodyPosition"
                        j, _ = 193, f == g
                    end
                elseif j > 0x50 then
                    j = _ and 227 or j + 0x33
                else
                    c, m, i = c(e.d(m))
                    c, m, i = e.b(c, m, i)
                    a, k = c(m, i)
                    i = a
                    j = i == nil and 188 or 0xa1
                end
            elseif j > 38 then
                if j > 0x27 then
                    g = "LinearVelocity"
                    j, _ = 39, f == g
                else
                    j = _ and 149 - j or 11
                end
            elseif j <= 35 then
                if j > 11 then
                    j = 0x9f
                    _(g)
                else
                    j, g = 110, "VectorForce"
                    _ = f == g
                end
            else
                g = "BodyAngularVelocity"
                j, _ = 218, f == g
            end
        end
    end
end,
ye = function (e, a)
    return function ()
        local c, d, _
        _ = 50
        repeat
            if _ > 0x32 then
                d = e.c(d(c))
                return e.d(d)
            else
                d, _, c = a[1][1][a[1][2]], 0xa1, true
                d["Archivable"] = c
                d, c = d.Clone, d
            end
        until false
    end
end,
Kb = function (e, a)
    return function ()
        local d, _, c
        _ = 0x5d
        repeat
            if _ > 0x91 then
                c = a[1][1][a[1][2]]
                _, d = 40, not c
            elseif _ > 0x5d then
                d = d(c)
                _ = d and 0x8f4d / _ or _ + -0x69
            elseif _ <= 40 then
                return d
            else
                _, c = 0x91, a[2][1][a[2][2]]
                c, d = "AutoOpenReadyEggs", c["isOn"]
            end
        until false
    end
end,
Xb = function (e, h)
    return function ()
        local j, _, d, a, n, f, m, c, k, l, g
        j = 0x27
        repeat
            if j <= 152 then
                if j <= 0x3d then
                    if j < 0x30 then
                        if j < 21 then
                            if j <= 3 then
                                j = j + 200
                                f(_)
                            else
                                j, g = 105, g()
                                g, _ = a["Interval"], g - f
                                k = _ >= g
                            end
                        elseif j <= 0x15 then
                            f, g = h[3][1][h[3][2]], e._["os"]
                            j, _ = 0x5b, g["clock"]
                        else
                            d = h[2][1][h[2][2]]
                            j = d and 154 or 167
                        end
                    elseif j >= 53 then
                        if j < 60 then
                            _ = h[1][1][h[1][2]]
                            j, f = 0xab, _["isDoubleSpeedVisible"]
                        elseif j > 0x3c then
                            j = g and 213 - j or 0xa3
                        else
                            j, k = 296 - j, a["Ready"]
                        end
                    elseif j > 0x30 then
                        j = m > c and 0x30 or 101
                    else
                        return
                    end
                elseif j < 105 then
                    if j >= 0x63 then
                        if j > 0x63 then
                            k, n = h[5][1][h[5][2]], d[m]
                            a = k[n]
                            k = a
                            j = k and 0x3c or 0xe6
                        else
                            return
                        end
                    else
                        _ = _()
                        f[n] = _
                        _ = "Auto Treadmill"
                        f = n ~= _
                        j = f and 0xc8 - j or 325 - j
                    end
                elseif j >= 135 then
                    if j > 135 then
                        return
                    else
                        l = e._["os"]
                        j, g = j + -119, l["clock"]
                    end
                elseif j <= 105 then
                    j = k and 0x89d / j or j + 58
                else
                    f = h[4][1][h[4][2]]
                    j = f and 0x63a2 / j or 0x1691 / j
                end
            elseif j >= 0xcb then
                if j < 0xe9 then
                    if j <= 223 then
                        if j <= 0xcb then
                            j, f = 0xf2, true
                            h[2][1][h[2][2]], _, f = f, a["Run"], e._["pcall"]
                        else
                            j, g = 0x3d, _
                        end
                    else
                        j = k and 0xe9 or j + -0x7d
                    end
                elseif j <= 236 then
                    if j > 234 then
                        j, k = 230, k()
                    elseif j > 0xe9 then
                        j = f and 0xa572 / j or 0xb98e / j
                    else
                        _ = h[3][1][h[3][2]]
                        f = _[n]
                        j = f and 0x87 or 180
                    end
                else
                    f, _ = f(_)
                    g = false
                    h[2][1][h[2][2]], g = g, f
                    j = g and 465 - j or 0x39aa / j
                end
            elseif j <= 171 then
                if j < 167 then
                    if j <= 0x9a then
                        return
                    else
                        j, f = 0x34, 1
                        m = m + f
                    end
                elseif j <= 0xa7 then
                    c = h[1][1][h[1][2]]
                    j, d = 0x158 - j, c["priorityOrder"]
                else
                    j, f = 0xea, f()
                end
            elseif j <= 0xb4 then
                if j > 0xb1 then
                    j, f = 135, 0
                else
                    d = d()
                    m, c = 1, #d
                    n = m
                    j = c < n and 0x114 - j or 278 - j
                end
            else
                f, _ = e._["pcall"], h[1][1][h[1][2]]
                j, _ = j + -0xb2, _["stopTreadmillTraining"]
            end
        until false
    end
end,
Uc = function (e, a)
    return function ()
        local d, _, c, b
        _ = 102
        repeat
            if _ > 74 then
                if _ <= 0x85 then
                    if _ >= 112 then
                        if _ <= 0x70 then
                            _, c = 0x15, e.c(c(b))
                        else
                            c = e._["table"]
                            c, _, b, d = e._["pcall"], 140, e:Wc{a[4], a[2]}, c["pack"]
                        end
                    elseif _ <= 79 then
                        d = true
                        a[3][1][a[3][2]] = d
                        return
                    else
                        d, b = a[2][1][a[2][2]], "RemoteFunction"
                        c, _, d = d, 3, d.IsA
                    end
                elseif _ <= 140 then
                    _, c = 0x40, e.c(c(b))
                else
                    d, _, b = a[2][1][a[2][2]], 0x98 / _, "RemoteEvent"
                    c, d = d, d.IsA
                end
            elseif _ > 0x16 then
                if _ > 0x40 then
                    c = e._["table"]
                    _, c, d = 0x63 - _, false, c["pack"]
                elseif _ > 0x19 then
                    d = d(e.d(c))
                    _, a[1][1][a[1][2]] = 79, d
                else
                    _, d = _ + 54, d(c)
                    a[1][1][a[1][2]] = d
                end
            elseif _ >= 0x15 then
                if _ > 21 then
                    _, c = 0x86 - _, e._["table"]
                    c, d, b = e._["pcall"], c["pack"], e:Vc{a[4], a[2]}
                else
                    _, d = 0x4f, d(e.d(c))
                    a[1][1][a[1][2]] = d
                end
            elseif _ <= 1 then
                d = d(c, b)
                _ = d and 134 - _ or 0x4a
            else
                d = d(c, b)
                _ = d and 0x19 - _ or 0x1c8 / _
            end
        until false
    end
end,
X = function (e, h)
    return function ()
        local g, b, _, c, k, j, f, n, l, a, m, d
        j = 82
        repeat
            if j < 0x69 then
                if j < 82 then
                    if j < 0x38 then
                        if j <= 0x15 then
                            _ = _(g, l, b)
                            k = f + _
                            return k
                        else
                            j, n, m, c = 0x13a7 / j, "Machines", d, d.FindFirstChild
                        end
                    elseif j > 0x38 then
                        k = nil
                        return k
                    else
                        n = nil
                        return n
                    end
                elseif j > 0x59 then
                    g, f = e._["Vector3"], a["Position"]
                    g, l, _ = 0, 4, g["new"]
                    j, b = 21, g
                elseif j <= 84 then
                    if j <= 0x52 then
                        m, d = "__OBJECTS", h[1][1][h[1][2]]
                        j, c, d = 0x73, d, d.FindFirstChild
                    else
                        m = {[2] = 3, [3] = m}
                        m[1] = m
                        n = not m[1][m[2]]
                        j = n and 0x38 or 171
                    end
                else
                    m = c
                    j = m and j + 145 or j + -5
                end
            elseif j < 0xc7 then
                if j < 129 then
                    if j <= 0x69 then
                        n, a = n(a)
                        k = not n
                        j = k and 0x596a / j or 199
                    else
                        d = d(c, m)
                        c = d
                        j = c and 39 or 89
                    end
                elseif j <= 0x81 then
                    j, c = j + -0x28, c(m, n)
                else
                    a, j, n = e:ld{m}, 0x4623 / j, e._["pcall"]
                end
            elseif j > 218 then
                j, a, m, n = 213, "FuseMachine", c.FindFirstChild, c
            elseif j >= 0xd5 then
                if j > 0xd5 then
                    j = k and 0x3b9c / j or 0x5d
                else
                    j, m = j + -129, m(n, a)
                end
            else
                j, k = 0x1a1 - j, not a
            end
        until false
    end
end,
Xd = function (e, g)
    return function (d)
        local c, f, b, _
        _ = 0x2b
        repeat
            if _ < 0xbd then
                if _ > 0x4c then
                    if _ > 143 then
                        c(b, f)
                        f, c = "Minutes between server hops", g[1][1][g[1][2]]
                        _, b, c = 0xf5, c, c.SetDescription
                    else
                        return
                    end
                elseif _ >= 61 then
                    if _ <= 0x3d then
                        _, f, c = 174, "Hop Every", g[1][1][g[1][2]]
                        c, b = c.SetTitle, c
                    else
                        c = "After Steal Count"
                        _ = d == c and 219 or 14
                    end
                elseif _ <= 14 then
                    f, c = "Wait Before Hop", g[1][1][g[1][2]]
                    _, c, b = 194, c.SetTitle, c
                else
                    c = "Timed Interval"
                    _ = d == c and 61 or 0x4c
                end
            elseif _ <= 0xdb then
                if _ > 0xce then
                    _, f, c = 254, "Hop After", g[1][1][g[1][2]]
                    b, c = c, c.SetTitle
                elseif _ < 194 then
                    _ = 332 - _
                    c(b, f)
                elseif _ <= 194 then
                    _ = _ + -5
                    c(b, f)
                    c, f = g[1][1][g[1][2]], "Seconds without a matching egg"
                    b, c = c, c.SetDescription
                else
                    _ = 0x15d - _
                    c(b, f)
                end
            elseif _ <= 0xf5 then
                _ = 0x184 - _
                c(b, f)
            else
                c(b, f)
                c, f = g[1][1][g[1][2]], "Number of stolen eggs before hopping"
                _, b, c = 0xce, c, c.SetDescription
            end
        until false
    end
end,
cd = function (e, a)
    return function ()
        local c, d, _
        _ = 174
        while true do
            if _ <= 174 then
                c = a[1][1][a[1][2]]
                _, c, d = 227, "PlayerRequest", c["RequestDropHeldAreaEgg"]
            else
                d(c)
                return
            end
        end
    end
end,
Aa = function (e, h)
    return function (d, c)
        local i, a, _, f, j, k, g, m
        j = 0x76
        repeat
            if j < 101 then
                if j > 0x3b then
                    if j > 0x42 then
                        f = f(_, g)
                        k["Size"] = f
                        g = e._["Enum"]
                        _ = g["Font"]
                        f = _["GothamBold"]
                        k["Font"] = f
                        f = 13
                        k["TextSize"] = f
                        f = 0.4
                        k["TextStrokeTransparency"] = f
                        k["TextColor3"] = c
                        k["Parent"] = a
                        _ = {}
                        _["anchor"] = i
                        _["billboard"] = a
                        _["label"] = k
                        g = nil
                        _["highlight"] = g
                        _, f = h[2][1][h[2][2]], _
                        _[d] = f
                        return f
                    else
                        k = k(f)
                        f = "Text"
                        k["Name"] = f
                        f = 1
                        k["BackgroundTransparency"] = f
                        j, _ = 92, e._["UDim2"]
                        _, f = 1, _["fromScale"]
                        g = _
                    end
                elseif j > 47 then
                    j, k = 141, k(f, _)
                    a["Size"] = k
                    f = e._["Vector3"]
                    f, k, _ = 0, f["new"], 2.5
                    g = f
                elseif j > 37 then
                    a = e._["Instance"]
                    j, a, i = 237, "Part", a["new"]
                else
                    return m
                end
            elseif j > 141 then
                if j > 0xea then
                    i = i(a)
                    j, a = 0xea, "EspAnchor"
                    i["Name"] = a
                    a = true
                    i["Anchored"] = a
                    a = false
                    i["CanCollide"] = a
                    i["CanQuery"] = a
                    i["CanTouch"] = a
                    a = 1
                    i["Transparency"] = a
                    k = e._["Vector3"]
                    k, a = 0.2, k["new"]
                    _, f = k, k
                else
                    a = a(k, f, _)
                    i["Size"] = a
                    a = h[1][1][h[1][2]]
                    i["Parent"] = a
                    k = e._["Instance"]
                    j, a, k = j + -0x85, k["new"], "BillboardGui"
                end
            elseif j < 0x76 then
                a = a(k)
                k = "EspLabel"
                j, a["Name"] = 0x1747 / j, k
                k = true
                a["AlwaysOnTop"] = k
                f = e._["UDim2"]
                _, k, f = 34, f["fromOffset"], 0xdc
            elseif j > 0x76 then
                k = k(f, _, g)
                a["StudsOffset"] = k
                j, a["Adornee"] = 0x42, i
                a["Parent"] = i
                f = e._["Instance"]
                k, f = f["new"], "TextLabel"
            else
                i = h[2][1][h[2][2]]
                m = i[d]
                j = m and 0x25 or 47
            end
        until false
    end
end,
_f = function (e, h)
    return function ()
        local b, c, i, g, j, d, a
        j = 0x52
        repeat
            if j <= 0x73 then
                if j >= 83 then
                    if j >= 84 then
                        if j > 0x54 then
                            d = d()
                            c = not d
                            j = c and 0xc7 - j or 0x82 - j
                        else
                            c = false
                            return c
                        end
                    else
                        i = {}
                        j, b = 0xbb, i
                    end
                elseif j <= 0x3a then
                    if j > 15 then
                        return i
                    else
                        c = d["Inventory"]
                        j = c and 169 - j or 0xb3
                    end
                else
                    c = h[2][1][h[2][2]]
                    j, d = 115, c["getSave"]
                end
            elseif j < 179 then
                if j > 0x96 then
                    b = d["EggInventory"]
                    j = b and 0xbb or 0x53
                else
                    g = h[1][1][h[1][2]]
                    a, g = b[g], nil
                    j, i = 0x21fc / j, a == g
                end
            elseif j <= 179 then
                b = {}
                j, c = 0x9a, b
            else
                g = h[1][1][h[1][2]]
                g, a = nil, c[g]
                i = a == g
                j = i and 0x96 or 0x3a
            end
        until false
    end
end,
Qd = function (e, a)
    return function ()
        local _, c, d
        _ = 0xe6
        repeat
            if _ < 230 then
                d(c)
                return
            else
                _, c = 0x4c, e._["task"]
                c, d = e:je{a[1]}, c["spawn"]
            end
        until false
    end
end,
Ud = function (e, a)
    return function ()
        local _, c, d
        _ = 0x4e
        repeat
            if _ >= 0x4e then
                _, c = 67, a[1][1][a[1][2]]
                d = c["rejoinServer"]
            else
                d()
                return
            end
        until false
    end
end,
Hb = function (e, g)
    return function ()
        local b, c, f, _, d
        _ = 220
        repeat
            if _ <= 0x70 then
                if _ >= 27 then
                    if _ >= 0x5a then
                        if _ <= 90 then
                            _ = d and 112 or 0x1b
                        else
                            d = false
                            return d
                        end
                    elseif _ <= 0x1b then
                        _, c = 0x2b - _, g[1][1][g[1][2]]
                        d = c["pickStealTarget"]
                    else
                        c = false
                        return c
                    end
                elseif _ >= 0x10 then
                    if _ <= 16 then
                        d = d()
                        c = not d
                        _ = c and 52 - _ or 24
                    else
                        b = g[1][1][g[1][2]]
                        f, b, _, c = "Warning", "Stealing", 261 - _, b["setStatus"]
                    end
                else
                    c = g[1][1][g[1][2]]
                    _, d = _ + 0xc0, c["eggInventoryFull"]
                end
            elseif _ >= 215 then
                if _ < 0xdc then
                    _ = 0x78
                    c(b)
                    b = g[1][1][g[1][2]]
                    b, c = d, b["stealEgg"]
                elseif _ <= 0xdc then
                    d = g[2][1][g[2][2]]
                    _ = d and 90 or 1
                else
                    _ = 0xd7
                    c(b, f)
                    b = g[1][1][g[1][2]]
                    b, c = "Auto Steal Egg", b["setJob"]
                end
            elseif _ > 0x78 then
                _, d = 283 - _, d()
            else
                c = e.c(c(b))
                return e.d(c)
            end
        until false
    end
end,
rb = function (e, h)
    return function (d, c)
        local k, b, a, i, f, j, _
        j = 0xb9
        while true do
            if j < 136 then
                if j > 0x4a then
                    if j <= 109 then
                        i(a, k, f, _)
                        return
                    else
                        a = h[1][1][h[1][2]]
                        i, a, k = a["notify"], "Copied", c
                        j = k and 0xe46 / j or j + 0x77
                    end
                elseif j >= 39 then
                    if j > 0x27 then
                        j = 126
                        i(a, k)
                    else
                        j, i, k, a = 0xb46 / j, e._["pcall"], d, b
                    end
                else
                    _, j, f = 3, j + 0x50, "Success"
                end
            elseif j > 0xc8 then
                if j <= 0xf5 then
                    j, k = 0x1bc1 / j, "Copied to clipboard"
                else
                    i = i(a)
                    a = "function"
                    j = i == a and 39 or 126
                end
            elseif j < 0xb9 then
                j, b = 0xc8, e._["toclipboard"]
            elseif j > 0xb9 then
                i, j, a = e._["typeof"], j + 0x30, b
            else
                b = e._["setclipboard"]
                j = b and 200 or 136
            end
        end
    end
end,
pa = function (e)
    return function (d)
        local i, g, f, k, c, l, j, a, _, m
        j = 0x56
        repeat
            if j < 0xac then
                if j > 83 then
                    if j < 123 then
                        m = {}
                        c, j, i, m = m, 9, d, e._["typeof"]
                    elseif j <= 123 then
                        j, g = 306 - j, e._["table"]
                        _, g, l = g["insert"], c, f
                    else
                        return c
                    end
                elseif j < 38 then
                    if j > 9 then
                        j = 198
                        m(i, a)
                    else
                        m = m(i)
                        i = "table"
                        j = m ~= i and 161 or 259 - j
                    end
                elseif j >= 0x33 then
                    if j > 0x33 then
                        k, f = m(i, a)
                        a = k
                        j = a == nil and j + 0x7d or 0x11c - j
                    else
                        j, i = j + -14, e._["table"]
                        a, i, m = d["BaseMutation"], c, i["insert"]
                    end
                else
                    m = m(i)
                    i = "table"
                    j = m == i and 0xc8 or j + 170
                end
            elseif j >= 198 then
                if j > 201 then
                    if j <= 0xd0 then
                        j, m, i = 0xbc, e._["typeof"], d["BaseMutation"]
                    else
                        i, j, m = d["Mutations"], 0x251c / j, e._["typeof"]
                    end
                elseif j <= 200 then
                    if j > 0xc6 then
                        j, m, i = 174, e._["pairs"], d["Mutations"]
                    else
                        return c
                    end
                else
                    _, j, g = e._["typeof"], 373 - j, f
                end
            elseif j <= 183 then
                if j <= 174 then
                    if j > 172 then
                        m, i, a = m(i)
                        m, i, a = e.b(m, i, a)
                        k, f = m(i, a)
                        a = k
                        j = a == nil and 208 or 375 - j
                    else
                        _ = _(g)
                        g = "string"
                        j = _ == g and 0x52a4 / j or 0xff - j
                    end
                else
                    j = 0x10a - j
                    _(g, l)
                end
            else
                m = m(i)
                i = "string"
                j = m == i and 0x2574 / j or j + 10
            end
        until false
    end
end,
mf = function (e, h)
    return function (d)
        local n, g, j, b, a, m, l, _, c, i, o, p, f
        j = 6
        while true do
            if j > 184 then
                m = m + a
                j = (a > 0 and m > n or a <= 0 and m < n or a ~= a) and 0x4a or j + -0x38
            elseif j <= 74 then
                if j <= 6 then
                    c, n, m = 0, 5, 1
                    a = m
                    j = (n ~= n or a > 0 and m > n or (a <= 0 or a ~= a) and m < n) and 74 or 184
                else
                    n, a, m, p = h[1][1][h[1][2]], c, h[2][1][h[2][2]], 24
                    n = n(a, p)
                    f, p, a, _ = c, h[1][1][h[1][2]], h[3][1][h[3][2]], 16
                    p = p(f, _)
                    f = 0xff
                    a = a(p, f)
                    p, _, f, o = h[3][1][h[3][2]], c, h[1][1][h[1][2]], 8
                    f = f(_, o)
                    _ = 255
                    p = p(f, _)
                    o, f, _ = 255, h[3][1][h[3][2]], c
                    f = e.c(f(_, o))
                    m = e.c(m(n, a, p, e.d(f)))
                    return e.d(m)
                end
            else
                _ = 85
                _, j, f, b, i, l, g = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~", 240, c * _, d, m, d.sub, m
                l = l(b, i, g)
                o, i, b, _ = _, true, 1, _.find
                _ = _(o, l, b, i)
                f, p = 1, f + _
                c = p - f
            end
        end
    end
end,
ua = function (e, h)
    return function (d)
        local g, i, k, j, a, b, c, f, _
        j = 94
        while true do
            if j >= 0x9e then
                if j < 0xf4 then
                    if j < 169 then
                        c = nil
                        return c
                    elseif j > 0xa9 then
                        return _
                    else
                        f = f(_, g)
                        j = f and 250 or 0x119 - j
                    end
                elseif j <= 0xfa then
                    if j > 0xf4 then
                        _ = k["Name"]
                        j, f = 112, _ == d
                    else
                        c, b, i = c(e.d(b))
                        c, b, i = e.b(c, b, i)
                        a, k = c(b, i)
                        i = a
                        j = i == nil and 158 or 284 - j
                    end
                else
                    f, _ = f(_, g)
                    j = f and 200 or 90
                end
            elseif j < 90 then
                if j > 0x28 then
                    j, b = 0x3a24 / j, e.c(b(i))
                elseif j > 0x1a then
                    f, g, j, _ = k.IsA, "ModuleScript", 209 - j, k
                else
                    j, f, _, g = 0xfe, e._["pcall"], e._["require"], k
                end
            elseif j > 0x5e then
                j = f and 0x1a or 90
            elseif j > 90 then
                c, j, b = e._["ipairs"], 0x3d, h[1][1][h[1][2]]
                b, i = b.GetDescendants, b
            else
                a, k = c(b, i)
                i = a
                j = i == nil and j + 0x44 or 40
            end
        end
    end
end,
jc = function (e, h)
    return function ()
        local m, g, _, d, f, j, a, n, p, l, o, b, c, i
        j = 0xf0
        while true do
            if j < 0x8c then
                if j >= 0x34 then
                    if j < 0x79 then
                        if j < 56 then
                            if j > 52 then
                                n, a, p = n(a)
                                n, a, p = e.b(n, a, p)
                                f, _ = n(a, p)
                                p = f
                                j = p == nil and j + 0xa1 or 0x25d0 / j
                            else
                                f, _ = n(a, p)
                                p = f
                                j = p == nil and 216 or j + 124
                            end
                        elseif j > 61 then
                            j = 0xfd - j
                            b(i, g)
                        elseif j <= 0x38 then
                            j, l, b = 0x9f, e._["typeof"], _
                        else
                            j = o and 82 - j or 0x12a - j
                        end
                    elseif j <= 126 then
                        if j <= 0x7c then
                            if j <= 121 then
                                l = l(b)
                                j, o = 24, not l
                            else
                                d = d()
                                c = d
                                j = c and 4 or 0x7e
                            end
                        else
                            m, j, n = e._["typeof"], j + 51, c
                        end
                    elseif j <= 0x7f then
                        m(n)
                        m, j, a, n = false, 0xb6 - j, c, e._["pairs"]
                    else
                        return m
                    end
                elseif j <= 22 then
                    if j > 17 then
                        if j <= 0x15 then
                            j, b, l = 237, nil, _["Placement"]
                            o = l ~= b
                        else
                            g, b = h[3][1][h[3][2]], e._["pcall"]
                            j, g, i = 0x5d8 / j, f[1][f[2]], g["RequestCompleteHatchEgg"]
                        end
                    elseif j < 13 then
                        if j > 4 then
                            b = h[2][1][h[2][2]]
                            b, j, l = "AutoOpenReadyEggs", 0x79, b["isOn"]
                        else
                            j, c = 504 / j, d["EggInventory"]
                        end
                    elseif j > 13 then
                        j = j + 0x23
                    else
                        j = 30 - j
                    end
                elseif j <= 0x26 then
                    if j > 0x18 then
                        l = h[2][1][h[2][2]]
                        l, o, j, g, i, b = _, l["matchesEggFilters"], 0x36a / j, "LifecycleMutations", "LifecycleRarities", nil
                    elseif j > 23 then
                        j = o and 136 or 40
                    else
                        j, o = 0xa6 - j, o(l, b, i, g)
                    end
                else
                    j, b, l = 0xd1, f[1][f[2]], e._["typeof"]
                end
            elseif j < 0xb1 then
                if j > 0x9f then
                    if j <= 172 then
                        if j <= 166 then
                            if j > 162 then
                                l = o[1][o[2]]
                                j = l and j + 72 or 381 - j
                            else
                                j, b, l = j + -0x11, e:Ue{h[3], o, f}, e._["pcall"]
                            end
                        else
                            m, i = true, h[3][1][h[3][2]]
                            b = i["RequestCompleteHatchEgg"]
                            j = b and 22 or 357 - j
                        end
                    else
                        f = {[2] = 3, [3] = f}
                        f[1] = f
                        l = h[1][1][h[1][2]]
                        o = not l
                        j = o and 0xc8 - j or 9
                    end
                elseif j > 151 then
                    if j <= 0x9d then
                        o = false
                        o = {[2] = 3, [3] = o}
                        o[1] = o
                        b = h[3][1][h[3][2]]
                        l = b["IsLocalEggReady"]
                        j = l and j + 5 or 0xa6
                    else
                        j, l = 0x25e3 / j, l(b)
                        b = "table"
                        o = l == b
                    end
                elseif j >= 145 then
                    if j <= 0x91 then
                        j = 0xa6
                        l(b)
                    else
                        return
                    end
                elseif j <= 140 then
                    n = h[2][1][h[2][2]]
                    j, n, m = 0x4574 / j, "Auto Hatch", n["setJob"]
                else
                    j = o and j + 14 or 0x34
                end
            elseif j > 0xd7 then
                if j < 237 then
                    if j <= 216 then
                        return m
                    else
                        j = 0xb05 / j
                        b(i)
                    end
                elseif j < 0xee then
                    j = o and j + -199 or j + -94
                elseif j > 238 then
                    c = h[2][1][h[2][2]]
                    j, d = 124, c["getSave"]
                else
                    b = h[3][1][h[3][2]]
                    j, l = j + -0x17, b["RequestHatchEgg"]
                end
            elseif j < 207 then
                if j < 180 then
                    m = m(n)
                    n = "table"
                    j = m ~= n and 0x6867 / j or 140
                elseif j <= 0xb4 then
                    l = false
                    j, l = 0x183 - j, {[2] = 3, [3] = l}
                    l[1] = l
                    b, i = e._["pcall"], e:Te{h[3], l, f}
                else
                    i = e._["task"]
                    j, b, i = 217, i["wait"], 0.35
                end
            elseif j <= 209 then
                if j <= 207 then
                    b(i)
                    j = l[1][l[2]] and 172 or 13
                else
                    l = l(b)
                    b = "string"
                    o = l == b
                    j = o and 56 or 61
                end
            else
                j = l and 0x18b - j or 0x11
            end
        end
    end
end,
te = function (e, g)
    return function ()
        local _, d, c, b
        _ = 220
        while true do
            if _ < 0xdc then
                d(c, b)
                return
            else
                b, _, d = g[1][1][g[1][2]], 0x17, g[2][1][g[2][2]]
                c, b, d = d, not b, d.SetGameplayPausedNotificationEnabled
            end
        end
    end
end,
bb = function (s, h)
    return function ()
        local f, b, p, i, x, l, r, c, _, j, t, k, d, v, o, a, n, e, g, u, q, w
        j = 0x43
        while true do
            if j <= 150 then
                if j <= 0x4b then
                    if j <= 0x26 then
                        if j <= 19 then
                            if j > 16 then
                                if j <= 18 then
                                    j, q = 66, 0
                                else
                                    j, q = 138, q(o)
                                end
                            elseif j <= 8 then
                                if j > 5 then
                                    j, d = 0xb3, h[2][1][h[2][2]]
                                    d, c = d.GetChildren, d
                                else
                                    c = {}
                                    j, d = 0x96, c
                                end
                            else
                                j, a = 0xbb0 / j, h[1][1][h[1][2]]
                                n = a["getRoot"]
                            end
                        elseif j <= 0x1d then
                            if j <= 0x17 then
                                if j > 0x16 then
                                    n = n(a)
                                    j, w = 16, not n
                                else
                                    j, n = 0x9e2 / j, h[1][1][h[1][2]]
                                    w, n = n["isOn"], "AutoStealAll"
                                end
                            else
                                u = nil
                                k = g == u
                                j = k and 243 or 146
                            end
                        else
                            b = "Furthest"
                            j = a == b and 0xcc4 / j or 0x49
                        end
                    elseif j <= 67 then
                        if j >= 66 then
                            if j <= 66 then
                                o = 0x186a0
                                o, j, b = s._["math"], 114, q * o
                                o, x, q = v, 0x1869f, o["min"]
                            else
                                d = h[2][1][h[2][2]]
                                j = d and 8 or 104
                            end
                        elseif j <= 47 then
                            _, j, r = s._["typeof"], 0x4d, f["Uid"]
                        else
                            b = b(q)
                            j = b and 0x2cc4 / j or 133
                        end
                    elseif j <= 0x49 then
                        if j > 0x45 then
                            b = "Biggest Size"
                            j = a == b and 300 - j or j + 109
                        else
                            j = e > f and 0xbc or j + 0xaa
                        end
                    else
                        v = h[1][1][h[1][2]]
                        j, u, v = 155, v["getSlotEggPosition"], i
                    end
                elseif j >= 115 then
                    if j <= 0x85 then
                        if j <= 0x84 then
                            if j >= 118 then
                                if j > 118 then
                                    j, o = 0x13, h[1][1][h[1][2]]
                                    o, q = g, o["eggScore"]
                                else
                                    a = h[1][1][h[1][2]]
                                    j, a, n = 0x17, "AutoStealSelected", a["isOn"]
                                end
                            else
                                w = w(n)
                                j = w and 0x76 or 0x10
                            end
                        else
                            j, b = 0x144 - j, 0
                        end
                    elseif j >= 146 then
                        if j <= 146 then
                            j = k and 0x2ac6 / j or 0xef
                        else
                            w, c = 0, #d
                            j = c == w and 0x9150 / j or 192
                        end
                    else
                        j = q and 66 or j + -0x78
                    end
                elseif j > 0x5d then
                    if j < 105 then
                        j = d and 0x96 or 5
                    elseif j > 105 then
                        j, q = 0x45, q(o, x)
                        e = b - q
                    else
                        j = k and 251 - j or 134 - j
                    end
                elseif j <= 86 then
                    if j > 80 then
                        j, e = j + -0x11, v
                    elseif j <= 77 then
                        _ = _(r)
                        r = "string"
                        j = _ == r and 247 or 228
                    else
                        j, v = 0x114 - j, u
                    end
                else
                    w, n, a = w(s.d(n))
                    w, n, a = s.b(w, n, a)
                    p, f = w(n, a)
                    a = p
                    j = a == nil and 0x73 - j or 140 - j
                end
            elseif j >= 0xd0 then
                if j < 0xf0 then
                    if j <= 228 then
                        if j <= 0xe3 then
                            if j >= 214 then
                                if j <= 0xd6 then
                                    j, b = 0xa5, n["Position"]
                                    e = b - u
                                    v = e["Magnitude"]
                                else
                                    b, q = s._["tonumber"], g
                                    j = q and 0xfa or j + -32
                                end
                            else
                                u = h[1][1][h[1][2]]
                                j, v, u, k = 457 - j, w, g, u["isStealCandidate"]
                            end
                        else
                            p, f = w(n, a)
                            a = p
                            j = a == nil and 22 or 0x2f
                        end
                    elseif j > 232 then
                        t, i = _(r, l)
                        l = t
                        j = l == nil and 0xec33 / j or 0x98
                    elseif j > 0xe7 then
                        j, n = 0x5448 / j, s.c(n())
                    else
                        e, b = nil, "Nearest"
                        j = a == b and j + -0x29 or 38
                    end
                elseif j <= 248 then
                    if j < 247 then
                        if j <= 240 then
                            j, e = 0x1d7 - j, s._["math"]
                            v = e["huge"]
                        else
                            j, k = 389 - j, w
                        end
                    elseif j <= 247 then
                        j, _ = 0xe4, f["Uid"]
                        c[_] = f
                    else
                        c = nil
                        return c
                    end
                elseif j > 0xfa then
                    return p
                elseif j > 0xf9 then
                    j, q = 0xc3, g["AssetScale"]
                else
                    j, k = 105, k(u, v)
                end
            elseif j >= 188 then
                if j < 192 then
                    if j > 190 then
                        j, e = 0x45, b
                    elseif j <= 188 then
                        p, j, f = i, 239, e
                    else
                        j, e = 0x3336 / j, -v
                    end
                elseif j <= 196 then
                    if j >= 195 then
                        if j <= 0xc3 then
                            j = 60
                        else
                            j = v and 214 or 0x7e54 / j
                        end
                    else
                        w = {}
                        j, w, c, a = 232, s._["ipairs"], w, h[1][1][h[1][2]]
                        n = a["getAreaEggs"]
                    end
                else
                    j, a = 171, a(p, f)
                    r, p = s._["math"], nil
                    _ = r["huge"]
                    f, r, _ = -_, d, s._["ipairs"]
                end
            elseif j > 171 then
                if j > 0xb6 then
                    j, n = 0x18a - j, n()
                    p = a
                    a, p, f = p["optionValue"], "StealPriority", "Rarest"
                elseif j > 179 then
                    q = g
                    j = q and 0x5dd8 / j or 0x140 - j
                else
                    j, d = 283 - j, d(c)
                end
            elseif j >= 0xa5 then
                if j > 165 then
                    _, r, l = _(r)
                    _, r, l = s.b(_, r, l)
                    t, i = _(r, l)
                    l = t
                    j = l == nil and j + 0x52 or 0x6588 / j
                else
                    j = v and 231 or j + 75
                end
            elseif j <= 152 then
                k = i["Name"]
                g = c[k]
                k = g
                j = k and 0x168 - j or 105
            else
                u = u(v)
                v = n
                j = v and 80 or j + 41
            end
        end
    end
end,
Qe = function (e, g)
    return function ()
        local c, _, b, d
        _ = 0x80
        while true do
            if _ >= 96 then
                if _ < 128 then
                    _, b = 0xfe, g[2][1][g[2][2]]
                    c, b = b["_regrabBusy"], true
                    d = c == b
                elseif _ <= 128 then
                    _, c = 0x2f, g[2][1][g[2][2]]
                    c, d = "AutoReturn", c["isOn"]
                else
                    return d
                end
            elseif _ <= 9 then
                d = g[1][1][g[1][2]]
                _ = d and _ + 245 or 0x60
            else
                d = d(c)
                _ = d and 9 or _ + 207
            end
        end
    end
end,
Ac = function (e, g)
    return function (d, c)
        local b, _, f
        _ = 0xb5
        repeat
            if _ >= 0x2c then
                if _ <= 0x2c then
                    _, b, f = 44 - _, e._["pcall"], e:cf{d, g[1], c}
                else
                    d = {[2] = 3, [3] = d}
                    d[1] = d
                    c = {[2] = 3, [3] = c}
                    c[1] = c
                    b = g[1][1][g[1][2]]
                    _ = b and 0x2c or 6
                end
            elseif _ <= 0 then
                _ = 6
                b(f)
            else
                return
            end
        until false
    end
end,
Mb = function (e, h)
    return function ()
        local l, c, m, a, g, j, _, n, k, d, f
        j = 73
        repeat
            if j <= 0x8b then
                if j >= 0x49 then
                    if j < 127 then
                        if j < 0x66 then
                            if j > 0x49 then
                                n = n(a)
                                j = n and 42 or 63
                            else
                                j, c = 0xaf, h[2][1][h[2][2]]
                                d, c = c["multiSelected"], "UpgradeTypes"
                            end
                        elseif j >= 104 then
                            if j > 104 then
                                k = h[3][1][h[3][2]]
                                a, j, k = k["GetByUpgradeLevel"], j + 27, 1
                                k = n + k
                            else
                                m = m(n)
                                c = not m
                                j = c and 0x80 or 0x1d
                            end
                        else
                            c = c()
                            m = not c
                            j = m and 0x5742 / j or 60
                        end
                    elseif j >= 0x87 then
                        if j < 138 then
                            a = a(k)
                            j = a and j + -0x70 or 0x42f9 / j
                        elseif j > 0x8a then
                            n(a)
                            m, j, a = true, j + 0x15, e._["task"]
                            a, n = 0.35, a["wait"]
                        else
                            j, n = 246 - j, 0
                        end
                    elseif j > 0x7f then
                        c, m = {}, true
                        c["Base"] = m
                        j, c["Treadmill"] = 0x1d, m
                        d = c
                    else
                        return m
                    end
                elseif j <= 0x2b then
                    if j < 0x1d then
                        if j <= 0x16 then
                            j, a = 93, h[1][1][h[1][2]]
                            a, n = c, a["IsNextTierAffordable"]
                        else
                            j, f, k = 66 - j, a["Price"], e._["tonumber"]
                        end
                    elseif j < 0x2a then
                        m = h[2][1][h[2][2]]
                        j, c = j + 73, m["getSave"]
                    elseif j > 0x2a then
                        k = k(f)
                        j = k and 51 or 222
                    else
                        j, a = 181 - j, h[2][1][h[2][2]]
                        n, k = a["netCall"], h[4][1][h[4][2]]
                        a = k["Plots"]
                        a = a["REQUEST_BASE_UPGRADE"]
                    end
                elseif j > 0x3d then
                    n = d["Treadmill"]
                    j = n and 204 or 223
                elseif j < 0x3c then
                    f = c["Money"]
                    j = f >= k and j + 0x9c or 0x7f
                elseif j > 0x3c then
                    j = n and j + 113 or 0x2bd8 / j
                else
                    n, m = d["Base"], false
                    j = n and j + 185 or 0x3d
                end
            elseif j >= 0xcf then
                if j <= 223 then
                    if j < 0xdb then
                        if j <= 207 then
                            _ = h[2][1][h[2][2]]
                            j, f, l = 0xc2df / j, _["netCall"], h[4][1][h[4][2]]
                            g = l["Treadmills"]
                            _, g = g["REQUEST_UPGRADE"], a["_id"]
                        else
                            a, j, n = c["TreadmillUpgradeLevel"], 0xba, e._["tonumber"]
                        end
                    elseif j <= 0xde then
                        if j <= 0xdb then
                            m = false
                            return m
                        else
                            j, f = 51, e._["math"]
                            k = f["huge"]
                        end
                    else
                        j = n and 180 or 390 - j
                    end
                elseif j >= 245 then
                    if j <= 245 then
                        j, n = 0x3a61 / j, h[1][1][h[1][2]]
                    else
                        j = 0x7a0a / j
                        f(_)
                    end
                elseif j <= 0xef then
                    a = a(k)
                    k = "function"
                    j, n = 0x196 - j, a == k
                else
                    j = 246
                    f(_, g)
                    _, m = e._["task"], true
                    _, f = 0.35, _["wait"]
                end
            elseif j < 0xaf then
                if j > 168 then
                    j, a, k = 342 - j, e._["typeof"], h[1][1][h[1][2]]
                    k = k["IsNextTierAffordable"]
                elseif j <= 167 then
                    if j <= 0xa0 then
                        j = 0x3f
                        n(a)
                    else
                        j = n and j + 0x30 or 0x7f
                    end
                else
                    j, a = 0xb8, a(k)
                    k = "function"
                    n = a == k
                end
            elseif j > 184 then
                if j <= 186 then
                    n = n(a)
                    j = n and 108 or 324 - j
                else
                    j, n = 223, h[3][1][h[3][2]]
                end
            elseif j > 180 then
                j = n and 22 or 0x2d48 / j
            elseif j > 0xaf then
                k, j, a = h[3][1][h[3][2]], 239, e._["typeof"]
                k = k["GetByUpgradeLevel"]
            else
                d = d(c)
                n = h[2][1][h[2][2]]
                j, m, n = j + -0x47, n["multiHasAny"], "UpgradeTypes"
            end
        until false
    end
end,
Ma = function (e, h)
    return function (d)
        local f, _, i, g, k, j, m, a, c
        j = 167
        while true do
            if j >= 111 then
                if j >= 0xb6 then
                    if j > 0xc2 then
                        if j > 219 then
                            m, i = m(i)
                            i = {[2] = 3, [3] = i}
                            i[1] = i
                            a = not m
                            j = a and 0x4dd6 / j or 0xcfe1 / j
                        else
                            j, f, k = 0xc2, i[1][i[2]], e._["typeof"]
                        end
                    elseif j > 0xc0 then
                        k = k(f)
                        f = "string"
                        j, a = 0x52, k ~= f
                    elseif j > 0xb6 then
                        _ = _(g)
                        g = "table"
                        j, f = j + -0xb5, _ ~= g
                    else
                        m, j, i = e._["pcall"], 0xf3, e:Ed{c}
                    end
                elseif j > 0x7f then
                    if j > 140 then
                        j, m = 115, e._["string"]
                        c, i, m = m["format"], e._["game"], "https://games.roblox.com/v1/games/%d/servers/Public?sortOrder=Asc&excludeFullGames=true&limit=100"
                        i = i["PlaceId"]
                    else
                        a = nil
                        return a
                    end
                elseif j > 115 then
                    g, j, _ = k, 73, e._["typeof"]
                elseif j > 0x6f then
                    c = c(m, i)
                    c = {[2] = 3, [3] = c}
                    c[1] = c
                    j = d and 0x32 or 182
                else
                    f = nil
                    return f
                end
            elseif j < 50 then
                if j >= 26 then
                    if j <= 0x1a then
                        _, j, g = e._["typeof"], 192, k["data"]
                    else
                        return k
                    end
                elseif j > 11 then
                    j = f and 32 - j or 26
                else
                    j = f and j + 100 or 29
                end
            elseif j < 0x4d then
                if j <= 0x32 then
                    j, i = 0xb6, "&cursor="
                    m = i .. d
                    c[1][c[2]] = c[1][c[2]] .. m
                else
                    j, _ = 21, _(g)
                    g = "table"
                    f = _ ~= g
                end
            elseif j > 82 then
                a, k = a(k)
                f = not a
                j = f and 0x82 - j or j + 0x12
            elseif j <= 0x4d then
                a, j, k = e._["pcall"], j + 0x20, e:Dd{i, h[1]}
            else
                j = a and 0x8c or 159 - j
            end
        end
    end
end,
T = function (e, h)
    return function (d)
        local c, g, j, f, b, a, i
        j = 106
        repeat
            if j <= 0xa9 then
                if j <= 101 then
                    if j <= 0x1b then
                        if j < 14 then
                            g = g(f)
                            return g
                        elseif j > 14 then
                            c = c(b)
                            b = "Vector3"
                            j = c ~= b and 0xae or 214 - j
                        else
                            j, b = 101, b(i, a, g)
                            a = e._["CFrame"]
                            f, a, i, g = d.Z, d.X, a["new"], b
                        end
                    else
                        i = i(a, g, f)
                        j, i = 2, {[2] = 3, [3] = i}
                        i[1] = i
                        g = h[1][1][h[1][2]]
                        a = g["Character"]
                        a = {[2] = 3, [3] = a}
                        a[1] = a
                        f, g = e:kd{i, a, c}, e._["pcall"]
                    end
                elseif j <= 106 then
                    c, j, b = e._["typeof"], 27, d
                else
                    c = c()
                    c = {[2] = 3, [3] = c}
                    c[1] = c
                    b = not c[1][c[2]]
                    j = b and 0x18a - j or 371 - j
                end
            elseif j < 0xca then
                if j > 174 then
                    j, b = 169, h[2][1][h[2][2]]
                    c = b["getRoot"]
                else
                    c = false
                    return c
                end
            elseif j > 0xca then
                b = false
                return b
            else
                j, i = j + -188, h[2][1][h[2][2]]
                b, g, a, i = i["groundedY"], d.Y, d.Z, d.X
            end
        until false
    end
end,
Ja = function (e, a)
    return function ()
        local c, d, _, b
        _ = 0xd5
        while true do
            if _ >= 0x5e then
                if _ <= 94 then
                    d(c, b)
                    return
                else
                    c = a[2][1][a[2][2]]
                    d = not c
                    _ = d and 0x14 or 48
                end
            elseif _ > 0x14 then
                _, c = _ + 0x2e, e._["task"]
                d, c, b = c["delay"], 0.35, e:Cd{a[1], a[3]}
            else
                return
            end
        end
    end
end,
ub = function (e, h)
    return function ()
        local c, b, k, a, f, g, j, _, d, i
        j = 0xc7
        repeat
            if j >= 0x67 then
                if j <= 173 then
                    if j > 0xa4 then
                        c = false
                        return c
                    elseif j > 0xa2 then
                        j = 36
                        f(_)
                    elseif j <= 103 then
                        c, b, i = c(e.d(b))
                        c, b, i = e.b(c, b, i)
                        a, k = c(b, i)
                        i = a
                        j = i == nil and 0x58eb / j or 0xc3
                    else
                        j = f and 3 or 0x16c8 / j
                    end
                elseif j >= 0xc7 then
                    if j <= 0xc7 then
                        c = h[1][1][h[1][2]]
                        d = c["Character"]
                        c = not d
                        j = c and 173 or 0x31
                    else
                        c = true
                        return c
                    end
                else
                    k = {[2] = 3, [3] = k}
                    j, k[1] = 0x3921 / j, k
                    _, f, g = k[1][k[2]], k[1][k[2]].IsA, "LocalScript"
                end
            elseif j < 70 then
                if j >= 36 then
                    if j <= 0x24 then
                        a, k = c(b, i)
                        i = a
                        j = i == nil and j + 185 or 195
                    else
                        c, b, j, i = e._["ipairs"], d.GetDescendants, 119 - j, d
                    end
                else
                    j, f, _ = 0x1ec / j, e._["pcall"], e:we{k}
                end
            elseif j >= 0x5e then
                if j > 0x5e then
                    j, _ = 94, e._["string"]
                    g, _, f = "PushBack", k[1][k[2]]["Name"], _["find"]
                else
                    j, f = 0x3b7c / j, f(_, g)
                end
            elseif j <= 70 then
                j, b = 0x1c2a / j, e.c(b(i))
            else
                f = f(_, g)
                j = f and 0x61 or 0xa2
            end
        until false
    end
end,
fd = function (e, a)
    return function ()
        local c, d, _
        _ = 0x33
        repeat
            if _ >= 0x33 then
                if _ <= 0x95 then
                    if _ >= 0x4b then
                        if _ <= 0x4b then
                            _ = _ + -0x43
                            d()
                        else
                            _, c = 1, a[2][1][a[2][2]]
                            d = c["swapStealHumanoid"]
                        end
                    else
                        _, c = 0xf8, a[2][1][a[2][2]]
                        d = c["stealingEnabled"]
                    end
                else
                    d = d()
                    _ = d and 149 or 8
                end
            elseif _ > 0x18 then
                d()
                return
            elseif _ >= 8 then
                if _ <= 8 then
                    _, d = 24, a[1][1][a[1][2]]
                else
                    _ = 43
                    d()
                    d = a[3][1][a[3][2]]
                end
            else
                d()
                _, d = 76 - _, c["stabilizeStealRoot"]
            end
        until false
    end
end,
la = function (e, a)
    return function ()
        local d, _
        _ = 33
        while true do
            if _ > 0x21 then
                d = d()
                a[1][1][a[1][2]] = d
                return
            else
                _, d = 0xde, e._["tick"]
            end
        end
    end
end,
Sb = function (e, h)
    return function ()
        local i, d, b, a, c, j, f, k
        j = 252
        while true do
            if j >= 107 then
                if j >= 0xc1 then
                    if j < 0xe9 then
                        if j >= 0xd4 then
                            if j > 212 then
                                i = i()
                                k = a
                                j, a = 0x3700 / j, k["getLaneZ"]
                            else
                                j, c = 0x3d48 / j, c(b, i)
                            end
                        else
                            j, b = j + -0x42, b(i, a)
                        end
                    elseif j >= 235 then
                        if j <= 235 then
                            b = e._["Vector3"]
                            i, c = d["Position"], b["new"]
                            b, a = i.X, h[1][1][h[1][2]]
                            j, i = 0x1c7 - j, a["getLaneY"]
                        else
                            d = h[2][1][h[2][2]]
                            j = d and 100 or 129
                        end
                    else
                        j, i = 0x72ae / j, e._["Vector3"]
                        b, a = i["new"], c["Position"]
                        k, i = h[1][1][h[1][2]], a.X
                        a = k["getLaneY"]
                    end
                elseif j < 127 then
                    if j <= 118 then
                        if j <= 107 then
                            i, j, c, b = "BasePart", 319 - j, d.IsA, d
                        else
                            c = e.c(c(b, i, e.d(a)))
                            return e.d(c)
                        end
                    else
                        a = a()
                        j, f = 0x2c, k
                        k = f["getLaneZ"]
                    end
                elseif j <= 0x81 then
                    if j > 0x7f then
                        c = e._["Vector3"]
                        d, c, i = c["new"], 543.5, h[1][1][h[1][2]]
                        j, b = 34, i["getLaneY"]
                    else
                        j = b and j + 106 or j + 2
                    end
                else
                    c = c(b, i)
                    b = c
                    j = b and 0x31 or 0x120 - j
                end
            elseif j < 0x2c then
                if j <= 32 then
                    if j < 28 then
                        b = e.c(b(i, a, e.d(k)))
                        return e.d(b)
                    elseif j > 28 then
                        c, j, i = h[2][1][h[2][2]], j + 129, "SeparationLine"
                        b, c = c, c.FindFirstChild
                    else
                        d = d(c, b)
                        c = d
                        j = c and 0x6b or 0x818 / j
                    end
                elseif j <= 34 then
                    j, b = 76 - j, b()
                    a = i
                    i = a["getLaneZ"]
                else
                    j, i = 0xdf2 / j, e.c(i())
                end
            elseif j < 74 then
                if j >= 49 then
                    if j <= 49 then
                        i, b, j, a = c, c.IsA, 242 - j, "BasePart"
                    else
                        j, a = 0x76, e.c(a())
                    end
                else
                    j, k = 0x2c0 / j, e.c(k())
                end
            elseif j > 85 then
                b, j, d = "StartArea", 0x1c, h[2][1][h[2][2]]
                d, c = d.FindFirstChild, d
            elseif j > 0x4a then
                d = e.c(d(c, b, e.d(i)))
                return e.d(d)
            else
                j = c and 235 or 0x940 / j
            end
        end
    end
end,
Na = function (e, h)
    return function (d)
        local g, _, f, a, m, k, n, c, j, l
        j = 0xf2
        while true do
            if j < 150 then
                if j <= 0x43 then
                    if j >= 50 then
                        if j <= 0x36 then
                            if j > 50 then
                                j, n, a = 0x27de / j, e._["pcall"], e:Fd{c}
                            else
                                m, n, j, a = c[1][c[2]].FindFirstChild, c[1][c[2]], 171 - j, "Bounds"
                            end
                        else
                            j, k = 0xdc, a
                        end
                    elseif j >= 0x19 then
                        if j <= 0x19 then
                            _ = _()
                            l = g
                            j, g = 0x83, l["getLaneZ"]
                        else
                            k = e.c(k(f, _, e.d(g)))
                            return e.d(k)
                        end
                    else
                        j, a = 0xc7, e._["Vector3"]
                        k, n = m["Position"], a["new"]
                        f, a = h[1][1][h[1][2]], k.X
                        k = f["getLaneY"]
                    end
                elseif j > 0x7d then
                    j, g = 34, e.c(g())
                elseif j >= 0x79 then
                    if j > 0x79 then
                        n, a, j, k = m.IsA, m, 239 - j, "BasePart"
                    else
                        m = m(n, a)
                        n = m
                        j = n and 246 - j or 271 - j
                    end
                else
                    j, n = 150, n(a, k)
                end
            elseif j > 0xc7 then
                if j >= 224 then
                    if j >= 242 then
                        if j > 242 then
                            m = nil
                            return m
                        else
                            m = h[1][1][h[1][2]]
                            m, j, c = d, 0xa4, m["getZoneModel"]
                        end
                    else
                        j, f = 0x1a6 - j, e.c(f())
                    end
                elseif j > 207 then
                    j = k and j + -13 or 0xbc
                else
                    j, f = 0xe8 - j, e._["Vector3"]
                    k, _ = f["new"], a["Position"]
                    g, f = h[1][1][h[1][2]], _.X
                    _ = g["getLaneY"]
                end
            elseif j >= 0xbd then
                if j < 0xc6 then
                    n, a = n(a)
                    k = n
                    j = k and 0x3177 / j or 0xdc
                elseif j <= 0xc6 then
                    n = e.c(n(a, k, e.d(f)))
                    return e.d(n)
                else
                    k = k()
                    j, _ = 0xae20 / j, f
                    f = _["getLaneZ"]
                end
            elseif j < 164 then
                j = n and 23 or 54
            elseif j <= 0xa4 then
                c = c(m)
                c = {[2] = 3, [3] = c}
                c[1] = c
                m = not c[1][c[2]]
                j = m and j + 0x56 or 0x32
            else
                k = nil
                return k
            end
        end
    end
end,
D = function (s, h)
    return function (...)
        local c, p, _, u, m, t, r, n, l, o, g, d, j, e, b, a, f, i, k
        j = 136
        while true do
            if j >= 118 then
                if j > 0xbd then
                    if j >= 0xe1 then
                        if j > 0xe1 then
                            j, f = 144, f(_, r)
                        else
                            f = f(_, r)
                            j = f and 0x171 - j or 0xb1
                        end
                    elseif j <= 192 then
                        return p
                    else
                        f, _, j, r = p.IsA, p, 225, "RemoteEvent"
                    end
                elseif j <= 0x90 then
                    if j <= 0x88 then
                        if j > 0x76 then
                            m, c = s.c(...), {}
                            s.e(c, 1, s.d(m))
                            j, c, m, d = 0x4d, s._["ipairs"], h[1][1][h[1][2]], c
                            n, m = m, m.GetDescendants
                        else
                            r, j, f, _ = d, j + -0x3d, true, s._["ipairs"]
                        end
                    else
                        j = f and 118 or j + -64
                    end
                elseif j > 177 then
                    c = nil
                    return c
                else
                    j, f, _, r = 427 - j, p.IsA, p, "RemoteFunction"
                end
            elseif j < 0x4c then
                if j <= 57 then
                    if j >= 39 then
                        if j <= 39 then
                            k = k(u, o, e, b)
                            g = not k
                            j = g and 0xc09 / j or j + 37
                        else
                            _, r, l = _(r)
                            _, r, l = s.b(_, r, l)
                            t, i = _(r, l)
                            l = t
                            j = l == nil and 0x1209 / j or 0x51 - j
                        end
                    else
                        j, u = 0x3a8 / j, s._["string"]
                        k, o, e, u, b = u["find"], i, 1, p["Name"], true
                    end
                else
                    c, m, n = c(s.d(m))
                    c, m, n = s.b(c, m, n)
                    a, p = c(m, n)
                    n = a
                    j = n == nil and 0x107 - j or 223
                end
            elseif j <= 0x4f then
                if j > 0x4d then
                    j, f = 0xa0 - j, false
                elseif j > 76 then
                    j, m = 0x97 - j, s.c(m(n))
                else
                    t, i = _(r, l)
                    l = t
                    j = l == nil and j + 5 or 100 - j
                end
            elseif j > 0x50 then
                j = f and j + 0x6f or 0x1950 / j
            else
                a, p = c(m, n)
                n = a
                j = n == nil and 0x3b10 / j or 0xdf
            end
        end
    end
end,
wb = function (e, h)
    return function ()
        local a, k, c, i, d, j, m, g, l, f, _
        j = 21
        while true do
            if j < 95 then
                if j <= 42 then
                    if j > 0x1a then
                        if j >= 0x26 then
                            if j <= 38 then
                                return a[1][a[2]]
                            else
                                j, _ = 0xb2, a[1][a[2]]
                            end
                        else
                            j, _ = 0x46, f
                        end
                    elseif j < 0x15 then
                        if j > 0x10 then
                            i = {[2] = 3, [3] = i}
                            j, i[1] = 0x98, i
                            a = nil
                            a = {[2] = 3, [3] = a}
                            a[1] = a
                            f, k = e:ye{c}, e._["pcall"]
                        else
                            j, _ = j + 0x68, _()
                            a[1][a[2]]["WalkSpeed"] = _
                            _ = true
                            a[1][a[2]]["AutoRotate"] = _
                        end
                    elseif j < 0x19 then
                        c = h[2][1][h[2][2]]
                        d = c["Character"]
                        c = not d
                        j = c and 122 or 0x41
                    elseif j <= 0x19 then
                        _(g)
                        j, l, g, _ = 71, "Humanoid", d, d.FindFirstChildOfClass
                    else
                        j = i and j + -7 or 182
                    end
                elseif j < 70 then
                    if j <= 65 then
                        if j <= 0x34 then
                            j = j + 153
                            _(g)
                        else
                            m, i, j, c = d, "Humanoid", 98, d.FindFirstChildOfClass
                        end
                    else
                        a[1][a[2]] = _
                        j = a[1][a[2]] and 0x9b - j or 0x78
                    end
                elseif j >= 71 then
                    if j > 71 then
                        _ = false
                        a[1][a[2]]["Sit"] = _
                        a[1][a[2]]["PlatformStand"] = _
                        g = h[3][1][h[3][2]]
                        j, _ = 16, g["stealSpeed"]
                    else
                        _ = _(g, l)
                        j = _ and 0x8a - j or 0xcd - j
                    end
                else
                    j = _ and 0x73 or j + 0x19
                end
            elseif j > 0x7f then
                if j >= 0xb6 then
                    if j <= 0xd0 then
                        if j > 205 then
                            i = h[1][1][h[1][2]]
                            m = i["CurrentCamera"]
                            m = {[2] = 3, [3] = m}
                            m[1] = m
                            i = m[1][m[2]]
                            j = i and 127 or 0x1520 / j
                        elseif j <= 182 then
                            j, i = 0x13, nil
                        else
                            j, g = 0x19, e._["task"]
                            _, g = g["wait"], 0.1
                        end
                    else
                        j = 274 - j
                        _(g)
                    end
                elseif j < 152 then
                    j, _ = 67, a[1][a[2]]
                elseif j <= 152 then
                    k, f = k(f)
                    _ = k
                    j = _ and 0x25 or j + -82
                else
                    j = _ and 0x11a - j or j + -0x8c
                end
            elseif j <= 115 then
                if j > 104 then
                    if j > 109 then
                        a[1][a[2]] = f
                        a[1][a[2]]["Parent"] = d
                        j, g, _ = 52, e:Ae{c}, e._["pcall"]
                    else
                        m = nil
                        return m
                    end
                elseif j <= 0x62 then
                    if j <= 95 then
                        j, a[1][a[2]] = 0x12c - j, c[1][c[2]]
                    else
                        c = c(m, i)
                        c = {[2] = 3, [3] = c}
                        c[1] = c
                        m = not c[1][c[2]]
                        j = m and 0x29ba / j or 0x4fa0 / j
                    end
                else
                    j, g, _ = 236, e:ze{a, m, i}, e._["pcall"]
                end
            elseif j < 122 then
                _ = m[1][m[2]]
                j = _ and 42 or 0x5370 / j
            elseif j <= 0x7a then
                c = nil
                return c
            else
                j, i = 26, m[1][m[2]]["CFrame"]
            end
        end
    end
end,
Ce = function (e)
    return function (d, c)
        local a, b, i
        i, a = d["playing"], c["playing"]
        b = i < a
        return b
    end
end,
Hf = {}, y = function (e, h)
    return function ()
        local j, i, g, d, a, b, c
        j = 0x25
        while true do
            if j <= 0x78 then
                if j > 43 then
                    if j > 91 then
                        c = false
                        return c
                    elseif j > 0x48 then
                        b = h[1][1][h[1][2]]
                        c = b["IsWorldPositionWithinLocalPlotBounds"]
                        j = c and 72 or 0x3552 / j
                    else
                        b = h[1][1][h[1][2]]
                        c, j, b = b["IsWorldPositionWithinLocalPlotBounds"], 0x29, d["Position"]
                    end
                elseif j <= 41 then
                    if j < 0x25 then
                        b = h[2][1][h[2][2]]
                        j, c = j + 0xe0, b["getPetAreaStandPosition"]
                    elseif j <= 37 then
                        j, c = 225, h[2][1][h[2][2]]
                        d = c["getRoot"]
                    else
                        j, c = 0x96, c(b)
                    end
                else
                    return b
                end
            elseif j <= 204 then
                if j > 0x96 then
                    g = d["Position"]
                    j, a = 0x2b, g - c
                    a, i = 0x1e, a["Magnitude"]
                    b = i <= a
                elseif j > 126 then
                    j = c and 126 or j + -143
                else
                    c = true
                    return c
                end
            elseif j > 0xe1 then
                c = c()
                i = nil
                b = c ~= i
                j = b and j + -27 or j + -0xbc
            else
                d = d()
                c = not d
                j = c and 0x6978 / j or 0x13c - j
            end
        end
    end
end,
id = function (e, h)
    return function ()
        local m, _, c, n, p, o, f, l, b, i, j, a, d
        j = 0x61
        repeat
            if j < 0xa7 then
                if j >= 0x3d then
                    if j > 102 then
                        j, _ = 301 - j, _(o)
                        o = "table"
                        f = _ == o
                    elseif j <= 97 then
                        if j <= 0x3d then
                            c = h[2][1][h[2][2]]
                            j, d = 190, c["GetRuntimeSnapshot"]
                        else
                            c = h[2][1][h[2][2]]
                            d = c["GetRuntimeSnapshot"]
                            j = d and 0x3d or 0x66
                        end
                    else
                        return
                    end
                elseif j > 17 then
                    j, i = 0x23e1 / j, h[1][1][h[1][2]]
                    i[l] = b
                elseif j <= 13 then
                    if j <= 5 then
                        c = {}
                        j, d = 0x389 / j, c
                    else
                        j, o, _ = 172, p, e._["typeof"]
                    end
                else
                    o, j, _ = p["Records"], 0x83, e._["typeof"]
                end
            elseif j < 181 then
                if j >= 0xac then
                    if j <= 172 then
                        _ = _(o)
                        o = "table"
                        f = _ == o
                        j = f and 0x11 or 0xaa
                    else
                        f, j, _ = e._["pairs"], 411 - j, p["Records"]
                    end
                elseif j <= 167 then
                    l, b = f(_, o)
                    o = l
                    j = o == nil and 373 - j or 0x37
                else
                    j = f and 0xb2 or 0x178 - j
                end
            elseif j <= 0xce then
                if j < 0xbe then
                    m, j, c = d, j + 0x1c, e._["pairs"]
                elseif j > 0xbe then
                    a, p = c(m, n)
                    n = a
                    j = n == nil and 102 or 13
                else
                    d = d()
                    j = d and 181 or 5
                end
            elseif j <= 209 then
                c, m, n = c(m)
                c, m, n = e.b(c, m, n)
                a, p = c(m, n)
                n = a
                j = n == nil and 0x5346 / j or j + -196
            else
                f, _, o = f(_)
                f, _, o = e.b(f, _, o)
                l, b = f(_, o)
                o = l
                j = o == nil and j + -0x1b or 0x320f / j
            end
        until false
    end
end,
Wb = function (e, h)
    return function (d, c)
        local b, f, a, _
        _ = 0xad
        while true do
            if _ > 0xad then
                if _ <= 219 then
                    if _ > 0xda then
                        _ = 226
                        f(a)
                    elseif _ >= 214 then
                        if _ <= 0xd6 then
                            _, b = 0x121 - _, not c[1][c[2]]
                        else
                            _, a, f = 219, e:Ne{c, b}, e._["pcall"]
                        end
                    else
                        _, d["CFrame"] = 226, c[1][c[2]]
                    end
                elseif _ <= 0xe2 then
                    return
                else
                    f = h[2][1][h[2][2]]
                    _, f, b = 159, d, f["stopSoftMove"]
                end
            elseif _ >= 0x84 then
                if _ > 0x9f then
                    c = {[2] = 3, [3] = c}
                    c[1] = c
                    b = not d
                    _ = b and 75 or 0xd6
                elseif _ <= 0x99 then
                    if _ > 132 then
                        return
                    else
                        b(f)
                        f = h[1][1][h[1][2]]
                        b = f["Character"]
                        b = {[2] = 3, [3] = b}
                        b[1] = b
                        f = b[1][b[2]]
                        _ = f and 41 or 0x57
                    end
                else
                    b(f)
                    _, f = 132, h[2][1][h[2][2]]
                    b, f = f["stripCheatMovers"], d
                end
            elseif _ > 75 then
                _ = f and 218 or 0xcc
            elseif _ <= 41 then
                _, f = 128 - _, b[1][b[2]]["Parent"]
            else
                _ = b and _ + 78 or 323 - _
            end
        end
    end
end,
Va = function (e, h)
    return function ()
        local b, c, _, d, f, a
        _ = 158
        while true do
            if _ > 0x8d then
                if _ < 0xd9 then
                    if _ <= 158 then
                        if _ <= 149 then
                            d, _, b = h[1][1][h[1][2]], 0x1b5b / _, "GameplayZ"
                            d, c = d.FindFirstChild, d
                        else
                            d = h[1][1][h[1][2]]
                            _ = d and 0x95 or 248
                        end
                    else
                        _, c = _ + -107, c(b, f)
                    end
                elseif _ > 0xee then
                    d = -365.5
                    return d
                elseif _ <= 217 then
                    f, _, b, a = c, 0x71, c.IsA, "BasePart"
                else
                    f = c["Position"]
                    b = f.Z
                    return b
                end
            elseif _ > 97 then
                if _ < 0x71 then
                    c, b, _, f = d.IsA, d, 0xb7, "BasePart"
                elseif _ > 113 then
                    b = d["Position"]
                    c = b.Z
                    return c
                else
                    _, b = 0x2ad1 / _, b(f, a)
                end
            elseif _ > 0x2f then
                if _ <= 76 then
                    _ = c and 217 - _ or 12
                else
                    _ = b and 238 or 248
                end
            elseif _ > 23 then
                d = d(c, b)
                c = d
                _ = c and 0x97 - _ or 76
            elseif _ <= 12 then
                _, f, c = 276 / _, "SeparationLine", h[1][1][h[1][2]]
                c, b = c.FindFirstChild, c
            else
                c = c(b, f)
                b = c
                _ = b and 0xd9 or 0x8b7 / _
            end
        end
    end
end,
ld = function (e, a)
    return function ()
        local c, d, _
        _ = 0x6d
        repeat
            if _ <= 0x6d then
                _, d = 0xe9, a[1][1][a[1][2]]
                d, c = d.GetPivot, d
            else
                d = e.c(d(c))
                return e.d(d)
            end
        until false
    end
end,
Nb = function (e, h)
    return function ()
        local m, f, k, c, a, d, n, g, j, b, l, _
        j = 0x33
        while true do
            if j < 0x65 then
                if j < 0x28 then
                    if j > 25 then
                        j = g and 54 / j or 0x28
                    elseif j > 5 then
                        m, j, n = e._["ipairs"], 126 - j, h[3][1][h[3][2]]
                    elseif j <= 2 then
                        j, g = 0xc3, true
                        d[_] = g
                        l = e._["table"]
                        l, b, g = c, _, l["insert"]
                    else
                        return c
                    end
                elseif j <= 76 then
                    if j >= 0x33 then
                        if j <= 0x33 then
                            c = {}
                            j, m, d = 158, {}, c
                            m, n, c = e._["ipairs"], h[2][1][h[2][2]], m
                        else
                            k, f = m(n, a)
                            a = k
                            j = a == nil and 380 / j or 0xd1
                        end
                    else
                        k, f = m(n, a)
                        a = k
                        j = a == nil and 25 or 0x11d - j
                    end
                else
                    j, l = 0x1b, d[_]
                    g = not l
                end
            elseif j < 0xcc then
                if j >= 0x9e then
                    if j <= 158 then
                        m, n, a = m(n)
                        m, n, a = e.b(m, n, a)
                        k, f = m(n, a)
                        a = k
                        j = a == nil and 0x19 or 245
                    else
                        j = 0x28
                        g(l, b)
                    end
                elseif j <= 101 then
                    m, n, a = m(n)
                    m, n, a = e.b(m, n, a)
                    k, f = m(n, a)
                    a = k
                    j = a == nil and j + -0x60 or 0xd1
                else
                    _ = _(g, l)
                    l = h[4][1][h[4][2]]
                    g = l[_]
                    j = g and 88 or 0xe8e / j
                end
            elseif j < 0xe6 then
                if j <= 204 then
                    j = j + -128
                    _(g, l)
                else
                    g = d[f]
                    _ = not g
                    j = _ and 0xbbc6 / j or 76
                end
            elseif j > 230 then
                g = h[1][1][h[1][2]]
                j, l, _, g = 0x8412 / j, nil, g["optionValue"], f
            else
                _ = true
                j, d[f] = 0xcc, _
                g = e._["table"]
                g, l, _ = c, f, g["insert"]
            end
        end
    end
end,
lb = function (e, a)
    return function (d)
        local c, b, _
        _ = 79
        while true do
            if _ > 0xcf then
                if _ > 242 then
                    c(b)
                    _ = d[1][d[2]] and 450 - _ or _ + -0x87
                else
                    c(b)
                    _, b = 0xf5, e:ue{d, a[1]}
                end
            elseif _ > 0xcd then
                _ = 317 - _
                c(b)
            elseif _ <= 110 then
                if _ > 79 then
                    return
                else
                    d = {[2] = 3, [3] = d}
                    d[1] = d
                    _, b, c = 242, e:te{d, a[2]}, e._["pcall"]
                end
            else
                c, _, b = e._["pcall"], 0xa5c3 / _, e:se{a[3]}
            end
        end
    end
end,
Fa = function (s, h)
    return function ()
        local p, r, t, e, j, a, m, _, g, n, f, k, l, c, o, q, i, d
        j = 0x9d
        repeat
            if j > 157 then
                if j >= 206 then
                    if j < 0xf3 then
                        if j <= 0xd0 then
                            if j > 206 then
                                j, l = 145, r
                            else
                                j, c, m, n = 0x493a / j, d.FindFirstChild, d, "Machines"
                            end
                        else
                            m = not c
                            j = m and 0x102 - j or 245
                        end
                    elseif j < 0xf5 then
                        j = l and 48 or 0x90
                    elseif j <= 0xf5 then
                        j, a, n, m = 0xb7c0 / j, c, c.GetChildren, s._["ipairs"]
                    else
                        c = c(m)
                        d = not c
                        j = d and 114 or j + -0x61
                    end
                elseif j >= 192 then
                    if j > 202 then
                        return
                    elseif j > 0xc0 then
                        _, r = _(r)
                        l = _
                        j = l and 0xd0 or 0x15b - j
                    else
                        j, n = 44, s.c(n(a))
                    end
                elseif j <= 162 then
                    j, l = 0x195 - j, l(t)
                else
                    j, k = 0x97, k(q, o, e)
                    q = f[1][f[2]]
                end
            elseif j < 0x72 then
                if j <= 91 then
                    if j >= 48 then
                        if j <= 0x30 then
                            t = h[2][1][h[2][2]]
                            g, i, j, l = f[1][f[2]]["Name"], "machine_", 184, t["drawEspAt"]
                            q, g, t, i = s._["Color3"], f[1][f[2]]["Name"], i .. g, r["Position"]
                            q, e, k, o = 230, 120, q["fromRGB"], 200
                        else
                            j, c = j + 132, c(m, n)
                        end
                    elseif j <= 0x23 then
                        return
                    else
                        m, n, a = m(s.d(n))
                        m, n, a = s.b(m, n, a)
                        p, f = m(n, a)
                        a = p
                        j = a == nil and j + 160 or 0x12e8 / j
                    end
                elseif j > 0x64 then
                    f = {[2] = 3, [3] = f}
                    j, f[1] = 0xca, f
                    r, _ = s:yd{f}, s._["pcall"]
                else
                    j, t = 262 - j, h[2][1][h[2][2]]
                    t, l = r["Position"], t["withinEspRange"]
                end
            elseif j >= 0x95 then
                if j >= 0x9c then
                    if j > 156 then
                        m = h[2][1][h[2][2]]
                        m, j, c = "EspMachines", 0xf6, m["isOn"]
                    else
                        d = d(c, m)
                        c = d
                        j = c and 0xce or 223
                    end
                elseif j <= 149 then
                    m, d = "__OBJECTS", h[1][1][h[1][2]]
                    j, c, d = 0x9c, d, d.FindFirstChild
                else
                    j = 0x54f0 / j
                    l(t, i, g, k, q)
                end
            elseif j >= 144 then
                if j > 0x90 then
                    j = l and 100 or 243
                else
                    p, f = m(n, a)
                    a = p
                    j = a == nil and 204 or 0x6e
                end
            else
                return
            end
        until false
    end
end,
Se = function (e, h)
    return function ()
        local c, a, d, f, j, i, b, k
        j = 0x7d
        while true do
            if j <= 147 then
                if j <= 72 then
                    if j >= 0x20 then
                        if j < 0x3a then
                            if j < 33 then
                                f = h[10][1][h[10][2]]
                                j, f = 281 - j, f["MAX_INVENTORY"]
                            elseif j <= 0x21 then
                                j = 0xf8 - j
                                d(c, b)
                            else
                                c = h[5][1][h[5][2]]
                                j = c and 0xc0 - j or 234
                            end
                        elseif j >= 0x47 then
                            if j > 0x47 then
                                return
                            else
                                j, a = 188, 0
                            end
                        elseif j > 0x3a then
                            j = 141
                        else
                            j, b = 0x1ba4 / j, e.c(b(i))
                            d, c = d.SetValue, d
                        end
                    elseif j > 15 then
                        if j > 26 then
                            j, a = j + 66, e.c(a(k))
                        else
                            j, b = j + 0xba, "No"
                        end
                    elseif j >= 11 then
                        if j > 11 then
                            j, b = 0 / j, "Neutral"
                        else
                            j, i, d = 252 - j, e._["string"], h[4][1][h[4][2]]
                            i, b, k = "%d / %s", i["format"], h[3][1][h[3][2]]
                            a = k["eggInventoryCount"]
                        end
                    elseif j <= 0 then
                        d, j, c = d.SetStatus, 0x21, d
                    else
                        d = d()
                        j = d and 0x2f or 72
                    end
                elseif j <= 0x7d then
                    if j <= 0x6a then
                        if j < 98 then
                            if j > 88 then
                                j, i = 0x9a, e.c(i(e.d(a)))
                                c, b = c.SetValue, c
                            else
                                j = 0xa6
                                c(b, e.d(i))
                            end
                        elseif j <= 0x62 then
                            i, d = h[3][1][h[3][2]], h[7][1][h[7][2]]
                            b, a = i["formatElapsed"], e._["os"]
                            j, i = 0xdf, a["clock"]
                        else
                            j = j + 128
                            c(b, e.d(i))
                        end
                    elseif j < 122 then
                        j, f = 0x45, "?"
                    elseif j > 122 then
                        d = h[9][1][h[9][2]]
                        j = d and 205 or 0xd7
                    else
                        j = j + 69
                        d(c, e.d(b))
                    end
                elseif j > 0x8d then
                    if j <= 145 then
                        j, a, c = 219, h[3][1][h[3][2]], h[5][1][h[5][2]]
                        a, i = d["Money"], a["formatNumber"]
                    else
                        j = 0x708c / j
                        c(b, e.d(i))
                    end
                elseif j >= 140 then
                    if j > 0x8c then
                        j, k = 0x4d1c / j, e.c(k(f))
                    else
                        j, b = 0x9e, e.c(b(i, a, e.d(k)))
                        d, c = d.SetValue, d
                    end
                else
                    a, c, i = d["Rebirth"], h[8][1][h[8][2]], e._["tostring"]
                    j = a and j + 0x3e or 0x47
                end
            elseif j <= 203 then
                if j <= 0xb8 then
                    if j > 0xa2 then
                        if j > 167 then
                            d(c, b)
                            b, d = h[1][1][h[1][2]], h[9][1][h[9][2]]
                            j = b and 233 or 0xadf0 / j
                        elseif j <= 166 then
                            c = h[2][1][h[2][2]]
                            j = c and j + 1 or 0x48
                        else
                            j, c, k, i = j + -0x8a, h[2][1][h[2][2]], h[3][1][h[3][2]], e._["tostring"]
                            k, a = d["Inventory"], k["countTable"]
                        end
                    elseif j >= 0x9e then
                        if j > 0x9e then
                            j, i = j + -15, e.c(i(a))
                            b, c = c, c.SetValue
                        else
                            j = j + 0x29
                            d(c, e.d(b))
                        end
                    elseif j <= 151 then
                        j, b = j + 94, "Yes"
                    else
                        j = 0x48
                        c(b, e.d(i))
                    end
                elseif j <= 199 then
                    if j < 196 then
                        if j > 188 then
                            d = h[4][1][h[4][2]]
                            j = d and 11 or 390 - j
                        else
                            j = 0xcb
                        end
                    elseif j > 0xc4 then
                        c = h[3][1][h[3][2]]
                        j, d = 9, c["getSave"]
                    else
                        c = h[8][1][h[8][2]]
                        j = c and 0x7e or 0x7f18 / j
                    end
                elseif j > 0xca then
                    j, i = 0x45c8 / j, e.c(i(a))
                    b, c = c, c.SetValue
                else
                    a, j, c = h[3][1][h[3][2]], 364 - j, h[11][1][h[11][2]]
                    a, i = d["SpeedPower"], a["formatNumber"]
                end
            elseif j > 233 then
                if j > 242 then
                    if j <= 0xf5 then
                        j = b and j + -0x21 or 26
                    else
                        j = f and 69 or 109
                    end
                elseif j <= 0xf1 then
                    if j > 234 then
                        a = a()
                        k, f = e._["tostring"], h[10][1][h[10][2]]
                        j = f and 32 or 0xf9
                    else
                        c = h[11][1][h[11][2]]
                        j = c and 0xca or 430 - j
                    end
                else
                    j = b and j + -242 or 15
                end
            elseif j >= 0xdb then
                if j > 223 then
                    j, b = 0xf2, "Warning"
                elseif j > 0xdb then
                    i = i()
                    a = h[6][1][h[6][2]]
                    j, i = 0x119 - j, i - a
                else
                    i = e.c(i(a))
                    j, b, c = 325 - j, c, c.SetValue
                end
            elseif j < 0xd4 then
                b, d = h[1][1][h[1][2]], h[9][1][h[9][2]]
                j = b and 0x97 or j + 40
            elseif j > 212 then
                d = h[7][1][h[7][2]]
                j = d and 98 or j + -0x18
            else
                j, c, d = 0x9860 / j, d, d.SetValue
            end
        end
    end
end,
Jc = function (e, g)
    return function ()
        local _, b, d, c
        _ = 0x67
        repeat
            if _ <= 97 then
                if _ <= 71 then
                    if _ > 0x13 then
                        return d
                    elseif _ <= 2 then
                        c(b)
                        b = g[2][1][g[2][2]]
                        _, b, c = 19, g[4][1][g[4][2]], b["clearTable"]
                    else
                        _ = 0x47
                        c(b)
                    end
                else
                    _, c = 2, 0
                    b, g[5][1][g[5][2]], g[1][1][g[1][2]], g[3][1][g[3][2]] = g[2][1][g[2][2]], c, c, c
                    c, b = b["clearTable"], g[6][1][g[6][2]]
                end
            elseif _ <= 104 then
                if _ > 103 then
                    c = c()
                    _, b = 0xed, true
                else
                    c = g[2][1][g[2][2]]
--===== [Webhook] Discord embed helpers =====
                    b, _, d = c, 0x68, c["sendWebhookEmbed"]
                    c = b["buildSummaryEmbed"]
                end
            else
                d = d(c, b)
                _ = d and 334 - _ or 71
            end
        until false
    end
end,
Ic = function (e, a)
    return function ()
        local d, c, _
        _ = 0x3a
        while true do
            if _ < 0xac then
                if _ > 58 then
                    return
                else
                    d = a[2][1][a[2][2]]
                    _ = d and 0xac or 0xa6
                end
            elseif _ > 172 then
                _ = 166
                d(c)
            else
                d, _, c = e._["pcall"], 0xe8, e:ef{a[1], a[2]}
            end
        end
    end
end,
s = function (e, g)
    return function ()
        local b, d, c, f, _
        _ = 0x2e
        while true do
            if _ < 0x2e then
                d(c, b, f)
                return
            else
                d, _, b, f = g[1][1][g[1][2]], 38, "PlayerGui", 10
                c, d = d, d.WaitForChild
            end
        end
    end
end,
Ec = function (e, h)
    return function (d)
        local a, i, g, c, b, _
        _ = 0x6c
        repeat
            if _ >= 0x74 then
                if _ < 151 then
                    if _ > 140 then
                        i = e._["Color3"]
                        b, i, _, g, a = i["fromRGB"], 110, _ + -0x7b, 0xff, 0xc3
                    elseif _ > 133 then
                        b = e.c(b(i, a, g))
                        return e.d(b)
                    elseif _ <= 116 then
                        b = 9
                        _ = c >= b and 102 or _ + 35
                    else
                        _, i = _ + -0x44, e._["Color3"]
                        a, i, b = 0x5a, 0xff, i["fromRGB"]
                        g = a
                    end
                elseif _ > 220 then
                    if _ <= 0xea then
                        _, c = 116, 0
                    else
                        _, i = 105, e._["Color3"]
                        a, i, g, b = 0xc8, 0xbe, 215, i["fromRGB"]
                    end
                elseif _ < 0xc1 then
                    b = 7
                    _ = c >= b and 0x11c - _ or 0xdc
                elseif _ > 193 then
                    b = 5
                    _ = c >= b and 193 or 0x105 - _
                else
                    i = e._["Color3"]
                    a, i, _, b, g = 0xbe, 0xff, _ + -0x75, i["fromRGB"], 80
                end
            elseif _ >= 65 then
                if _ >= 0x66 then
                    if _ <= 0x69 then
                        if _ > 102 then
                            b = e.c(b(i, a, g))
                            return e.d(b)
                        else
                            i = e._["Color3"]
                            _, a, i, b = 0x37c8 / _, 120, 255, i["fromRGB"]
                            g = i
                        end
                    else
                        b, i = h[1][1][h[1][2]], d
                        _ = i and 48 or 55
                    end
                elseif _ <= 0x41 then
                    b = e.c(b(i, a, g))
                    return e.d(b)
                else
                    b = e.c(b(i, a, g))
                    return e.d(b)
                end
            elseif _ > 0x30 then
                _, i = 0x30, ""
            elseif _ >= 41 then
                if _ > 41 then
                    c = b[i]
                    _ = c and 0x74 or 234
                else
                    b = 3
                    _ = c >= b and 0x91 or 0x273d / _
                end
            else
                b = e.c(b(i, a, g))
                return e.d(b)
            end
        until false
    end
end,
_d = function (e, h)
    return function ()
        local c, _, f, b, d, a
        _ = 55
        while true do
            if _ < 0x37 then
                d(c, b, f, a)
                return
            else
                f, d = e._["game"], h[2][1][h[2][2]]
                b, c, a, _, d, f = f["PlaceId"], d, h[3][1][h[3][2]], 42, d.TeleportToPlaceInstance, h[1][1][h[1][2]]
            end
        end
    end
end,
E = function (e, g)
    return function ()
        local d, c, _, b
        _ = 171
        repeat
            if _ > 0x59 then
                if _ > 0xe2 then
                    if _ <= 0xf2 then
                        c = c(b)
                        _, b = 0x59, "function"
                        d = c ~= b
                    else
                        d, b = e._["pcall"], g[1][1][g[1][2]]
                        _, c = 0x203a / _, b["Get"]
                    end
                elseif _ >= 0xb8 then
                    if _ <= 0xb8 then
                        c, b = e._["typeof"], g[1][1][g[1][2]]
                        _, b = 0xadf0 / _, b["Get"]
                    else
                        _, b = _ + -0xcc, nil
                    end
                else
                    c = g[1][1][g[1][2]]
                    d = not c
                    _ = d and 0x59 or 0xb8
                end
            elseif _ < 33 then
                if _ < 0x15 then
                    _, b = 0x570 / _, c
                elseif _ <= 21 then
                    d = nil
                    return d
                else
                    return b
                end
            elseif _ <= 0x57 then
                if _ <= 0x21 then
                    d, c = d(c)
                    b = d
                    _ = b and 16 or 0xb37 / _
                else
                    _ = b and 0x77a / _ or 0xe2
                end
            else
                _ = d and 0x6e - _ or 0x153 - _
            end
        until false
    end
end,
pb = function (s, h)
    return function ()
        local _, m, f, b, j, a, d, c, t, g, k, l, u, e, n, p, r, v, i, q
        j = 206
        repeat
            if j <= 0x70 then
                if j > 64 then
                    if j <= 93 then
                        if j < 0x54 then
                            if j < 81 then
                                if j <= 66 then
                                    j, b = j + 0x17, "?"
                                else
                                    t, j, l = nil, 247 - j, h[3][1][h[3][2]]
                                    l[_] = t
                                end
                            elseif j <= 0x51 then
                                a = {}
                                j, m = 0xfc, a
                            else
                                t, l = true, r["Uid"]
                                m[l] = t
                                t, i = h[3][1][h[3][2]], r["Uid"]
                                t, l = nil, t[i]
                                j = l == t and 0x3c8a / j or j + 132
                            end
                        elseif j >= 89 then
                            if j >= 0x5c then
                                if j > 92 then
                                    _, f = true, h[7][1][h[7][2]]
                                    j, f[a] = 0x105 - j, _
                                else
                                    c = c(m)
                                    j = c and 43 or 0x5c / j
                                end
                            else
                                j = 2
                            end
                        elseif j > 0x54 then
                            a = {}
                            j, m = 95, a
                        else
                            a = c(m, n)
                            n = a
                            j = n == nil and j + 37 or 0x3480 / j
                        end
                    elseif j <= 99 then
                        if j < 0x62 then
                            if j <= 95 then
                                j = 0x1c
                            else
                                j, v = j + -0x34, ""
                            end
                        elseif j <= 98 then
                            n = n(a)
                            a, f = s._["ipairs"], h[12][1][h[12][2]]
                            j, p = 0xfa - j, f["getAreaEggs"]
                        else
                            i = h[12][1][h[12][2]]
                            i, t, g = "WebhookRarities", i["selectionAllows"], l
                            j = g and 0x75 or 332 - j
                        end
                    elseif j >= 109 then
                        if j > 109 then
                            i = s._["table"]
                            v, u, g, i, t = l, h[9][1][h[9][2]], {}, h[2][1][h[2][2]], i["insert"]
                            j = v and 156 - j or j + -16
                        else
                            j = 0x5b1e / j
                            t(i, g)
                        end
                    else
                        j, k = j + 136, 0
                    end
                elseif j >= 40 then
                    if j < 0x30 then
                        if j > 43 then
                            k = u[v]
                            j = k and 0x28bc / j or 101
                        elseif j > 0x29 then
                            c, h[6][1][h[6][2]] = h[10][1][h[10][2]], c
                            h[4][1][h[4][2]] = c
                            return
                        elseif j > 0x28 then
                            j = t and 153 - j or 0xd6
                        else
                            a, j, m = s._["math"], 248, h[5][1][h[5][2]]
                            f, a, p, n = h[4][1][h[4][2]], 0, h[10][1][h[10][2]], a["max"]
                            p = p - f
                        end
                    elseif j <= 54 then
                        if j < 53 then
                            j, c = 0xec, 0
                        elseif j <= 0x35 then
                            c = true
                            h[1][1][h[1][2]], m, c = c, d["Inventory"], s._["pairs"]
                            j = m and 0x5f or 0x11ce / j
                        else
                            l = l(t)
                            t = n
                            j = t and 0x63 or 123
                        end
                    elseif j > 56 then
                        m = h[1][1][h[1][2]]
                        c = not m
                        j = c and 0x35 or j + -24
                    else
                        j, n = 241, h[6][1][h[6][2]]
                        m = c > n
                    end
                elseif j >= 0x11 then
                    if j > 28 then
                        if j > 34 then
                            v = v(e)
                            e, b = s._["tostring"], l
                            j = b and 0x59 or 66
                        else
                            j, p, a = 196, h[3][1][h[3][2]], s._["pairs"]
                        end
                    elseif j <= 0x18 then
                        if j > 0x11 then
                            c, j, m = s._["tonumber"], 116 - j, d["Rebirth"]
                        else
                            _, r, f = p["Uid"], true, h[3][1][h[3][2]]
                            j, f[_] = 0xe6, r
                        end
                    else
                        c, m, n = c(m)
                        c, m, n = s.b(c, m, n)
                        a = c(m, n)
                        n = a
                        j = n == nil and j + 179 or 0x79 - j
                    end
                elseif j >= 5 then
                    if j <= 5 then
                        return
                    else
                        t = m[_]
                        l = not t
                        j = l and 0x48 or j + 159
                    end
                elseif j > 1 then
                    e = e(b)
                    j, b, q = 183 - j, s._["tostring"], r["AreaId"]
                else
                    j, c = 43, 0
                end
            elseif j <= 195 then
                if j <= 0xaf then
                    if j > 152 then
                        if j > 0xa8 then
                            _ = a(p, f)
                            f = _
                            j = f == nil and 5 or 191 - j
                        elseif j >= 166 then
                            if j <= 0xa6 then
                                c, m, n = c(m)
                                c, m, n = s.b(c, m, n)
                                a = c(m, n)
                                n = a
                                j = n == nil and j + -45 or 326 - j
                            else
                                a = c(m, n)
                                n = a
                                j = n == nil and j + 0x27 or 93
                            end
                        else
                            _ = h[7][1][h[7][2]]
                            _, f = nil, _[a]
                            j = f == _ and 0x8020 / j or 0x54
                        end
                    elseif j >= 123 then
                        if j <= 148 then
                            if j > 0x7b then
                                c = c(m)
                                j = c and 0x8870 / j or 0x1bc0 / j
                            else
                                j = t and j + 72 or 0x29
                            end
                        else
                            j, p = 407 - j, s.c(p())
                        end
                    elseif j <= 117 then
                        j = j + 65
                    else
                        j, c, m = 148, s._["tonumber"], d["Rebirth"]
                    end
                elseif j < 0xb9 then
                    if j > 181 then
                        j, t = j + -0x3b, t(i, g)
                    elseif j > 180 then
                        j, b = 0xb0, s.c(b(q))
                    elseif j > 0xb0 then
                        return
                    else
                        k = k(u, v, e, s.d(b))
                        j, g["text"] = 0x6d, k
                    end
                elseif j <= 189 then
                    if j >= 0xba then
                        if j <= 0xba then
                            j, m = 0x173 - j, s.c(m())
                        else
                            l, i, j, t = h[3][1][h[3][2]], true, j + -0x87, r["Uid"]
                            l[t] = i
                            t = h[12][1][h[12][2]]
                            t, l = r["AssetCategory"], t["resolveRarity"]
                        end
                    else
                        c, m, n = c(s.d(m))
                        c, m, n = s.b(c, m, n)
                        a, p = c(m, n)
                        n = a
                        j = n == nil and 209 - j or 0x11
                    end
                else
                    j, g = 0x29, h[2][1][h[2][2]]
                    g, i = 60, #g
                    t = i < g
                end
            elseif j <= 233 then
                if j < 0xd5 then
                    if j < 0xce then
                        if j > 0xc4 then
                            _, f = true, h[7][1][h[7][2]]
                            f[a] = _
                            _, r = h[11][1][h[11][2]], 1
                            j, f = 84, _ + r
                            h[11][1][h[11][2]] = f
                        else
                            a, p, f = a(p)
                            a, p, f = s.b(a, p, f)
                            _ = a(p, f)
                            f = _
                            j = f == nil and j + -191 or 0x10
                        end
                    elseif j > 206 then
                        n, c = h[12][1][h[12][2]], s._["ipairs"]
                        j, m = 186, n["getAreaEggs"]
                    else
                        c = h[12][1][h[12][2]]
                        j, d = 0xd5, c["getSave"]
                    end
                elseif j > 0xd9 then
                    if j > 0xe6 then
                        j, g = j + -116, ""
                    else
                        a, p = c(m, n)
                        n = a
                        j = n == nil and 0x1590 / j or 0xf46 / j
                    end
                elseif j >= 214 then
                    if j > 214 then
                        h[6][1][h[6][2]], n = c, {}
                        j, a, m = 98, h[12][1][h[12][2]], n
                        a, n = "WebhookEggSpawns", a["isOn"]
                    else
                        _, r = a(p, f)
                        f = _
                        j = f == nil and 0x1c6c / j or j + -132
                    end
                else
                    d = d()
                    c = not d
                    j = c and 0x189 - j or 0x40
                end
            elseif j > 241 then
                if j > 0xfc then
                    a, p, f = a(s.d(p))
                    a, p, f = s.b(a, p, f)
                    _, r = a(p, f)
                    f = _
                    j = f == nil and 0x21de / j or 0x52
                elseif j > 0xf8 then
                    j = 0xa368 / j
                else
                    n = n(a, p)
                    c = m + n
                    h[5][1][h[5][2]], c = c, h[10][1][h[10][2]]
                    c, m, h[4][1][h[4][2]] = s._["pairs"], d["Inventory"], c
                    j = m and 0xf420 / j or 329 - j
                end
            elseif j < 0xed then
                if j > 0xeb then
                    m = h[6][1][h[6][2]]
                    j = m and 56 or 241
                else
                    a = h[8][1][h[8][2]]
                    a, n = h[6][1][h[6][2]], a + c
                    j, m = 217, n - a
                    h[8][1][h[8][2]] = m
                end
            elseif j > 237 then
                j = m and 0xeb or 217
            else
                g["rank"] = k
                u = h[2][1][h[2][2]]
                k = #u
                g["order"] = k
                j, u = j + -199, s._["string"]
                u, e, k = "**%s** `%s` in %s", h[12][1][h[12][2]], u["format"]
                e, v = r["AssetCategory"], e["assetName"]
            end
        until false
    end
end,
wd = function (e, h)
    return function ()
        local _, f, d, b, c
        _ = 0xe8
        while true do
            if _ > 0xa6 then
                if _ > 0xe3 then
                    d = h[1][1][h[1][2]]
                    _ = d and 0x82 or 166
                else
                    h[2][1][h[2][2]] = d
                    return
                end
            elseif _ <= 0x88 then
                if _ > 130 then
                    c, f = h[3][1][h[3][2]], h[1][1][h[1][2]]
                    c, b, _, f = c.IsInGroupAsync, c, 0x3a, f["GROUP_ID"]
                elseif _ <= 58 then
                    c = c(b, f)
                    b = true
                    _, d = 227, c == b
                else
                    c = h[1][1][h[1][2]]
                    _, d = 166, c["GROUP_ID"]
                end
            else
                _ = d and _ + -30 or 393 - _
            end
        end
    end
end,
Bd = function (e, a)
    return function ()
        local d, c
        c, d = a[1][1][a[1][2]], a[2][1][a[2][2]]
        d["Enabled"] = c
        return
    end
end,
l = function (e, h)
    return function (d)
        local i, j, c, b, k, f, a
        j = 195
        while true do
            if j <= 110 then
                if j > 39 then
                    c, b, i = c(e.d(b))
                    c, b, i = e.b(c, b, i)
                    a, k = c(b, i)
                    i = a
                    j = i == nil and j + -0x4c or 0xf4 - j
                elseif j >= 34 then
                    if j > 34 then
                        return k
                    else
                        c = nil
                        return c
                    end
                else
                    a, k = c(b, i)
                    i = a
                    j = i == nil and 42 - j or 134
                end
            elseif j <= 195 then
                if j <= 0x86 then
                    f = k["Uid"]
                    j = f == d and 0x146a / j or 8
                else
                    i, j, c = h[1][1][h[1][2]], 0xed, e._["ipairs"]
                    b = i["getAreaEggs"]
                end
            else
                j, b = 0x6e, e.c(b())
            end
        end
    end
end,
Vb = function (e, g)
    return function ()
        local d, f, b, c, _
        _ = 116
        while true do
            if _ < 97 then
                if _ > 0x23 then
                    d(c, b, f)
                    c = g[2][1][g[2][2]]
                    d = c["SetDefaultTheme"]
                    _ = d and 0x110d / _ or 0xef
                else
                    _ = 239
                    d(c, b)
                end
            elseif _ <= 0x74 then
                if _ > 0x61 then
                    d, f, b = g[2][1][g[2][2]], g[1][1][g[1][2]], "Ember"
                    _, d, c = 45, d.SaveCustomTheme, d
                else
                    b, d = "Ember", g[2][1][g[2][2]]
                    _, c, d = 0x23, d, d.SetDefaultTheme
                end
            else
                return
            end
        end
    end
end,
qd = function (e, g)
    return function ()
        local d, _, b, c
        _ = 12
        repeat
            if _ < 157 then
                if _ < 0x51 then
                    if _ <= 12 then
                        d = g[2][1][g[2][2]]
                        _ = d and 0x57 or 0xe5
                    else
                        d(c)
                        d = true
                        return d
                    end
                elseif _ <= 0x51 then
                    _, c, d = _ + -0x2f, e:ud{g[1]}, e._["pcall"]
                else
                    _, c = 0x4c20 / _, g[2][1][g[2][2]]
                end
            elseif _ > 0xe5 then
                if _ <= 0xe6 then
                    c = g[3][1][g[3][2]]
                    _, d = _ + -0x49, not c
                else
                    b, c = true, g[4][1][g[4][2]]
                    d = c == b
                    _ = d and 157 or 0xd4ee / _
                end
            elseif _ <= 224 then
                if _ <= 0x9d then
                    return d
                else
                    _, c = 229, c()
                    d = not c
                end
            else
                _ = d and 0x51 or 0xed
            end
        until false
    end
end,
Kf = function (a, b, c, d)
    a.Jf[d] = a.gf(b, c)
    return a.Jf[d]
end,
B = function (e, a)
    return function ()
        local c, _, d
        _ = 1
        repeat
            if _ >= 0x78 then
                if _ >= 0xa3 then
                    if _ < 0xc4 then
                        if _ <= 163 then
                            _, d = 234, true
                            c, a[2][1][a[2][2]], d = a[1][1][a[1][2]], d, e._["pcall"]
                            c = c["runAutoReturn"]
                        else
                            d = d(c)
                            _ = d and 0x5eb9 / _ or 0x104 - _
                        end
                    elseif _ > 226 then
                        d(c)
                        d = false
                        _, a[2][1][a[2][2]] = 0x187 - _, d
                    elseif _ > 196 then
                        _ = d and 0x1fc8 / _ or 0x5a0c / _
                    else
                        return
                    end
                elseif _ > 156 then
                    return
                elseif _ > 137 then
                    d = d(c)
                    _ = d and 120 or 0x89b8 / _
                elseif _ > 0x78 then
                    _, d = 83, a[4][1][a[4][2]]
                else
                    _, d = _ + 0x6a, a[4][1][a[4][2]]
                end
            elseif _ >= 81 then
                if _ < 102 then
                    if _ <= 0x51 then
                        _ = d and _ + 0x52 or _ + 0x4c
                    else
                        _ = d and 0x199d / _ or 81
                    end
                elseif _ > 102 then
                    d(c)
                    d = false
                    a[2][1][a[2][2]] = d
                    return
                else
                    _, c = 177, a[1][1][a[1][2]]
                    c, d = "AutoReturn", c["isOn"]
                end
            elseif _ < 0x38 then
                if _ <= 1 then
                    d = a[2][1][a[2][2]]
                    _ = d and 0xc4 or 56
                else
                    d = true
                    a[2][1][a[2][2]], c, d = d, a[1][1][a[1][2]], e._["pcall"]
                    _, c = _ + 83, c["runAutoDropEgg"]
                end
            elseif _ > 0x38 then
                c = a[3][1][a[3][2]]
                _, d = 81, not c
            else
                _, c = 0x2220 / _, a[1][1][a[1][2]]
                c, d = "AutoDropEgg", c["isOn"]
            end
        until false
    end
end,
vb = function (s, h)
    return function (d)
        local f, y, j, n, _, b, r, p, z, k, t, q, A, l, g, o, v, u, a, c, m, x, i, e
        j = 0xf7
        repeat
            if j >= 0x78 then
                if j > 188 then
                    if j > 222 then
                        if j < 0xef then
                            if j < 0xe5 then
                                r = h[2][1][h[2][2]]
                                _, j, r = r["multiHasAny"], 0x8e, "FuseMutations"
                            elseif j <= 229 then
                                b = a
                                j = b and 0xc7 or j + -0x24
                            else
                                v = v(e)
                                e = "string"
                                y = v == e
                                j = y and 0x2d or 428 - j
                            end
                        elseif j >= 247 then
                            if j > 0xf7 then
                                a = {}
                                j, n = 0x173 - j, a
                            else
                                c = d
                                j = c and 39 or 0xb8
                            end
                        elseif j > 239 then
                            j, o = 0x41e6 / j, 0
                        else
                            return A
                        end
                    elseif j <= 204 then
                        if j > 0xc1 then
                            if j > 199 then
                                n = n(a)
                                a = "table"
                                j = n ~= a and 0xef or 145
                            else
                                o = s._["table"]
                                j, x, q, o = 0x4c2e / j, g[1][g[2]], o["find"], n
                            end
                        elseif j < 0xc0 then
                            j = y and 0x48 or j + -173
                        elseif j > 0xc0 then
                            j, e = 0x2f, not b
                        else
                            j, b = 110, h[1][1][h[1][2]]
                            e = b["CanSelectPet"]
                        end
                    elseif j <= 221 then
                        if j <= 0xd1 then
                            f = f(s.d(_))
                            j = f and 226 or 99
                        else
                            j, x = 165, x(m, u)
                        end
                    else
                        j = j + -0x40
                        e(b)
                    end
                elseif j <= 0xa5 then
                    if j <= 142 then
                        if j >= 0x82 then
                            if j < 131 then
                                g = {[2] = 3, [3] = g}
                                j, g[1] = j + 0x6c, g
                                k = {[2] = 3, [3] = k}
                                k[1] = k
                                v, e = s._["typeof"], g[1][g[2]]
                            elseif j > 131 then
                                _ = _(r)
                                l = h[2][1][h[2][2]]
                                r, j, l = l["multiSelected"], 0xa7, "FuseMutations"
                            else
                                j, A[y[1][y[2]]] = 137 - j, m
                                u = s._["table"]
                                m, u, p = u["insert"], A[y[1][y[2]]], {}
                                p["uid"] = g[1][g[2]]
                                p["scale"] = o
                            end
                        elseif j > 120 then
                            j, b = j + -0x1d, h[2][1][h[2][2]]
                            b, e = k[1][k[2]], b["recordMutations"]
                        else
                            j, z = 0x35e8 / j, h[2][1][h[2][2]]
                            z, a = "FuseKeepEquipped", z["isOn"]
                        end
                    elseif j >= 158 then
                        if j > 0x9e then
                            m = b
                            j = m and 0xd5 - j or 0x10e - j
                        else
                            e = v[1][v[2]]
                            j = e and 229 or 47
                        end
                    elseif j <= 145 then
                        n = d["EquippedAssets"]
                        j = n and 0x43f8 / j or 251
                    else
                        q, o, x = q(o)
                        q, o, x = s.b(q, o, x)
                        m, u = q(o, x)
                        x = m
                        j = x == nil and j + 25 or 331 - j
                    end
                elseif j <= 0xb6 then
                    if j >= 173 then
                        if j > 180 then
                            m = A[y[1][y[2]]]
                            j = m and 0x83 or 0x7d2 / j
                        elseif j <= 0xad then
                            j, o = 69, h[2][1][h[2][2]]
                            o, q = y[1][y[2]], o["resolveRarity"]
                        else
                            j, m = 0x15e - j, x
                        end
                    elseif j > 0xa7 then
                        j = m and 182 or 19
                    else
                        r = r(l)
                        j, t, l = j + -0x75, c, s._["pairs"]
                    end
                elseif j <= 184 then
                    if j <= 183 then
                        p = r[u]
                        j = p and 0x370b / j or 0x75
                    else
                        j, n = 0xcc, {}
                        a, A, n = c, n, s._["typeof"]
                    end
                else
                    j, q = j + -0xa6, _
                end
            elseif j <= 70 then
                if j < 43 then
                    if j <= 19 then
                        if j >= 11 then
                            if j <= 0x11 then
                                if j <= 11 then
                                    j, u = 142 - j, {}
                                    m = u
                                else
                                    g, k = l(t, i)
                                    i = g
                                    j = i == nil and 119 or j + 0x71
                                end
                            else
                                j = 0x11
                            end
                        elseif j > 3 then
                            j = 19
                            m(u, p)
                        else
                            j, q, b, o = 151 - j, s._["ipairs"], false, e
                        end
                    elseif j >= 22 then
                        if j > 22 then
                            j, c = j + 0x91, d["Inventory"]
                        else
                            j = q and 3 or 0xad
                        end
                    else
                        b = not q
                        q = b
                        j = q and 0xbc or 0x16
                    end
                elseif j > 0x30 then
                    if j <= 69 then
                        if j >= 56 then
                            if j > 56 then
                                q = q(o)
                                o, j, x = s._["tonumber"], 0xc66 / j, k[1][k[2]]["Scale"]
                            else
                                z = z(f)
                                r, f = h[2][1][h[2][2]], s._["tonumber"]
                                r, _, j, l = "FuseMaxScale", r["optionValue"], 156 - j, 10
                            end
                        else
                            l, t, i = l(t)
                            l, t, i = s.b(l, t, i)
                            g, k = l(t, i)
                            i = g
                            j = i == nil and 0x173e / j or 0x1964 / j
                        end
                    else
                        m = nil
                        x = q == m
                        j = x and 165 or 0x8d - j
                    end
                elseif j >= 46 then
                    if j < 47 then
                        o = o(x)
                        j = o and j + 0x18 or 0x11f - j
                    elseif j <= 0x2f then
                        j = e and j + 75 or 0x37d / j
                    else
                        j, m = 0x69, o <= f
                    end
                elseif j <= 0x2b then
                    b = b(q)
                    q = "string"
                    e = b == q
                    j = e and 0x2040 / j or j + 0x43
                else
                    e, j, v = k[1][k[2]], 0xfd2 / j, s._["typeof"]
                end
            elseif j <= 98 then
                if j <= 0x4f then
                    if j >= 77 then
                        if j <= 0x4e then
                            if j > 0x4d then
                                j, o, x = 0x15, #e, 0
                                q = o > x
                            else
                                j, b = 0xad, true
                            end
                        else
                            e, j, b = s._["pcall"], 0xde, s:xe{h[1], v, k, y, g}
                        end
                    elseif j > 71 then
                        j, y = 0xc18 / j, k[1][k[2]]["Category"]
                        y = {[2] = 3, [3] = y}
                        y[1] = y
                        v = false
                        v = {[2] = 3, [3] = v}
                        v[1] = v
                        q, b = y[1][y[2]], s._["typeof"]
                    else
                        j, m = 0x3d4b / j, h[2][1][h[2][2]]
                        x, m, u = m["selectionAllows"], "FuseRarities", q
                    end
                elseif j <= 0x5d then
                    if j <= 0x5a then
                        v = v(e)
                        e = "table"
                        j, y = 0xbe, v == e
                    else
                        e = e(b)
                        q = z
                        j = q and j + -15 or 21
                    end
                else
                    q = q(o, x)
                    j, o = j + 0x5f, nil
                    b = q ~= o
                end
            elseif j <= 0x6e then
                if j < 105 then
                    if j <= 99 then
                        j, f = j + 0x7f, 10
                    else
                        j, _ = j + 0x6d, s.c(_(r, l))
                    end
                elseif j > 0x69 then
                    j = e and 0x4f or 0x43e4 / j
                else
                    j = m and 0x49d4 / j or 0x45ba / j
                end
            elseif j > 117 then
                return A
            elseif j <= 115 then
                a = a(z)
                j, f = 0x38, h[2][1][h[2][2]]
                f, z = "FuseKeepMutated", f["isOn"]
            else
                m, u = q(o, x)
                x = m
                j = x == nil and 0x4f11 / j or 0xb7
            end
        until false
    end
end,
f = function (Va)
    return function (...)
        local Da, pb, F, s, vb, C, la, fb, Ca, Y, Lb, Aa, pa, Oa, w, c, q, ta, tb, t, bb, ea, m, ib, hb, mb, O, J, R, ga, L, nb, Mb, Ab, Ra, n, ab, Sa, Pb, qa, eb, Ka, U, N, gb, D, e, _b, ca, Ob, _, _a, b, Fa, ma, T, l, ob, Ea, o, Ba, Hb, ka, Xa, Wa, yb, wa, Ya, Cb, x, Bb, Na, u, I, S, Ma, r, j, ua, aa, Jb, E, d, rb, Ua, H, W, g, v, zb, X, k, h, sa, qb, ja, A, da, xa, Ha, i, B, xb, Ib, cb, za, Ja, ya, Nb, Gb, p, jb, fa, Fb, G, ra, ha, K, V, P, Q, Db, kb, ba, M, ub, ia, y, Eb, db, lb, wb, na, Ia, La, va, Pa, sb, f, oa, Qa, z, Ta, a
        Ka = 0x71
        repeat
            if Ka < 411 then
                if Ka > 198 then
                    if Ka <= 280 then
                        if Ka <= 239 then
                            if Ka <= 215 then
                                if Ka >= 207 then
                                    if Ka >= 210 then
                                        if Ka < 0xd5 then
                                            if Ka <= 0xd2 then
                                                return
                                            else
                                                Ka, Pb = 0x1e22b / Ka, {[2] = 3, [3] = Pb}
                                                Pb[1] = Pb
                                                _b, ib, Fb, O, ga, B = 4, "Globals", l[1][l[2]], "Constants", "Shared", Na[1][Na[2]]["requirePath"]
                                            end
                                        elseif Ka > 213 then
                                            Ka, tb, K = 291, Na[1][Na[2]]["findRemoteContains"], "AskPlaceEgg"
                                        else
                                            P = P(G, S, w)
                                            J["GetAreaEggSnapshot"] = P
                                            G, Ka, S, w, P = ab, 0x1f338 / Ka, "SyncFieldEggs", "RequestAreaEggSnapshot", Na[1][Na[2]]["pickFn"]
                                        end
                                    elseif Ka <= 208 then
                                        if Ka > 0xcf then
                                            ua = not q
                                            Ka = ua and 192 or Ka + 40
                                        else
                                            Ka, _ = Ka + 0x26e, {}
                                            jb, Cb, _ = Sa["Directory"], _, Va._["pairs"]
                                        end
                                    else
                                        ga, Ka, _b = "Eggs", 0x356, Na[1][Na[2]]["findModule"]
                                    end
                                elseif Ka >= 203 then
                                    if Ka > 0xcd then
                                        Gb, Ka, K = "ConfirmBriefing", 0x342, Na[1][Na[2]]["findRemoteContains"]
                                    elseif Ka > 204 then
                                        Ka, Gb, K = 0x229, "AskPurchase", Na[1][Na[2]]["findRemoteContains"]
                                    elseif Ka > 203 then
                                        Gb = kb[1][kb[2]]["RequestAreaEggSnapshot"]
                                        K = not Gb
                                        Ka = K and 0xb34c / Ka or 151
                                    else
                                        Ka, K = 68, K(Gb)
                                    end
                                elseif Ka <= 201 then
                                    if Ka > 0xc8 then
                                        Gb, Ka, K = "EQUIP_BEST", Ka + 421, Na[1][Na[2]]["findRemoteContains"]
                                    else
                                        Ka, K, Gb = 0x26f, Na[1][Na[2]]["findRemoteContains"], "AskRedeemAll"
                                    end
                                else
                                    Ka = Bb and 0xbd or 0xd0
                                end
                            elseif Ka <= 230 then
                                if Ka >= 0xdf then
                                    if Ka < 228 then
                                        if Ka <= 0xdf then
                                            Ka, ab, j, O, Sa, ib = 0x3a8, "Assets", "Data", l[1][l[2]], 4, Na[1][Na[2]]["requirePath"]
                                        else
                                            Ka, K = 0x84b7 / Ka, Wa[1][Wa[2]]
                                        end
                                    elseif Ka > 228 then
                                        Ka, Gb, K = 0x1e7 - Ka, "LoadPet", Na[1][Na[2]]["findRemoteContains"]
                                    else
                                        r, Ka, ta = Va._["pairs"], 0x3d9, ga["Directory"]
                                    end
                                elseif Ka <= 219 then
                                    if Ka <= 0xda then
                                        wb, Ka, Db = Va:qc(), 0x329, Va._["pcall"]
                                    else
                                        Ka, K = 0x1c2 - Ka, K(Gb)
                                    end
                                else
                                    Db = true
                                    ya[1][ya[2]]["__MMB_HUB_RUNNING"] = Db
                                    wb = Va._["game"]
--===== [Main] Server / game load watch loop =====
                                    Ka, wb, hb = 317, wb.IsLoaded, wb
                                end
                            elseif Ka < 235 then
                                if Ka >= 0xe8 then
                                    if Ka > 0xe8 then
                                        Ka, tb["CLAIM_REWARD"] = 0x2f3ee / Ka, K
                                        Wa = tb
                                        rb["GroupReward"] = Wa
                                        vb = rb
                                        vb = {[2] = 3, [3] = vb}
                                        vb[1] = vb
                                        Wa, rb = "RF/EggWorld/AskFieldEggCarry", Na[1][Na[2]]["findRemote"]
                                    else
                                        bb, Ka, ua = Va:nc{v, ya}, 463, Va._["pcall"]
                                    end
                                else
                                    Ka, tb["SELL_ASSET"] = 0x1f5b4 / Ka, K
                                    Wa = tb
                                    rb["AssetInventory"] = Wa
                                    X, Gb, da, tb, K = "AwayEarnings", Ib, "FetchSummary", {}, Na[1][Na[2]]["remoteFrom"]
                                end
                            elseif Ka >= 0xee then
                                if Ka <= 238 then
                                    P, G, J, Ka, kb, Ib = "Shared", "Remotes", 6, 0x41b - Ka, l[1][l[2]], Na[1][Na[2]]["requirePath"]
                                else
                                    jb = jb(aa)
                                    aa = "table"
                                    Ka = jb == aa and 0x2a3ec / Ka or Ka + 0x4a
                                end
                            else
                                ta, Ka, R = Va._["typeof"], 0x16e, ga["Directory"]
                            end
                        elseif Ka < 256 then
                            if Ka < 0xf6 then
                                if Ka <= 0xf3 then
                                    if Ka <= 0xf2 then
                                        if Ka < 0xf1 then
                                            ib, Ka, O = Na[1][Na[2]]["findModule"], 0x1ff, "Assets"
                                        elseif Ka <= 0xf1 then
                                            Ka, Bb = 329, Bb(q, o)
                                            Oa["gethui"] = Bb
                                            Bb, o, q = Va._["rawget"], "protect_gui", ya[1][ya[2]]
                                        else
                                            _b = _b(ga, ib, O, Sa, j)
                                            Ka = _b and 250 or 451 - Ka
                                        end
                                    else
                                        Ka = K and 68 or 0x4458 / Ka
                                    end
                                elseif Ka > 0xf4 then
                                    Fb = {[2] = 3, [3] = Fb}
                                    Ka, Fb[1] = 242, Fb
                                    O, _b, j, ga, ib, Sa = "Shared", Na[1][Na[2]]["requirePath"], "Eggs", l[1][l[2]], 4, "Types"
                                else
                                    Ka, Fb, B = 0x29e - Ka, "Constants", Na[1][Na[2]]["findModule"]
                                end
                            elseif Ka < 250 then
                                if Ka > 0xf7 then
                                    Na, E = "mmb-hub-steal-an-egg", {}
                                    E["Id"] = Na
                                    Na = "MMB HUB"
                                    E["Title"] = Na
                                    Na = "Made with <3 - MMB HUB"
                                    E["Subtitle"] = Na
                                    Na = "Light"
                                    E["Theme"] = Na
                                    Na = "Comfortable"
                                    E["Density"] = Na
                                    Na = false
                                    E["HighContrast"] = Na
                                    Na = ""
                                    E["FooterText"] = Na
                                    Ka, Na = 0x271, "MMBHub"
                                    E["ConfigFolder"] = Na
                                    Na = true
                                    E["AutoLoad"] = Na
                                    Na = "Show MMBHub"
                                    E["ShowText"] = Na
--===== [UI] Window creation - title / theme / config =====
                                    bb, ua = o, o.CreateWindow
                                elseif Ka > 246 then
                                    ta = {}
                                    r = ta
                                    r = {[2] = 3, [3] = r}
                                    r[1] = r
                                    R = {}
                                    ta = R
                                    ta = {[2] = 3, [3] = ta}
                                    ta[1] = ta
                                    Cb = {}
                                    R = Cb
                                    R = {[2] = 3, [3] = R}
                                    R[1] = R
                                    Cb = Sa
                                    Ka = Cb and 0x1ae or 0x100
                                else
                                    Ka, ya = 0xc7e / Ka, Va._["_G"]
                                end
                            elseif Ka >= 0xfd then
                                if Ka <= 253 then
                                    B, Ka, Pb = "Save", 0x31b, Na[1][Na[2]]["findModule"]
                                else
                                    K = Va:tc{tb}
                                    Ka, kb[1][kb[2]]["RequestPlaceEgg"] = 60, K
                                end
                            elseif Ka <= 250 then
                                _b = {[2] = 3, [3] = _b}
                                Ka, _b[1] = 0x3befc / Ka, _b
                                j, ga, ib, O, Sa = "Areas", Na[1][Na[2]]["requirePath"], l[1][l[2]], 4, "Data"
                            else
                                Wa, Ka, rb = "AskFieldEggCarry", 0x27f, Na[1][Na[2]]["findRemoteContains"]
                            end
                        elseif Ka > 266 then
                            if Ka <= 0x115 then
                                if Ka > 0x114 then
                                    Pb = Pb(B)
                                    Na["Success"] = Pb
                                    Ka, B, Pb = Ka + 0x12, "F5A33B", bb
                                elseif Ka > 0x113 then
                                    Ka, qa = 0x22a - Ka, Va._["getgenv"]
                                elseif Ka <= 0x10c then
                                    Pb = Pb(B)
                                    Ka, Na["TextOnAccent"] = Ka + 9, Pb
                                    B, Pb = "69D38B", bb
                                else
                                    fb = fb(Ta, Y)
                                    fb = {[2] = 3, [3] = fb}
                                    fb[1] = fb
                                    Ta = not fb[1][fb[2]]
                                    Ka = Ta and 0x2a189 / Ka or 0x1d7
                                end
                            elseif Ka <= 278 then
                                qa = qa()
--===== [Server Hop] Hop history persistence =====
                                ka, qa = qa["MMBHubHopHistory"], Va._["typeof"]
                                Ka, fb = 0x2b192 / Ka, ka
                            else
                                Ka, G = 0x157, G(S, w, vb)
                                P["IsWorldPositionWithinLocalPlotBounds"] = G
                                S, G, vb, w = N, Na[1][Na[2]]["pickFn"], "GetSlotOwner", "LookupOwner"
                            end
                        elseif Ka >= 0x106 then
                            if Ka >= 265 then
                                if Ka > 265 then
                                    Ka, K = 0x52, K(Gb)
                                else
                                    Pb = Pb(B, Fb, _b, ga)
                                    Ka = Pb and 0xda6b / Ka or 0x105e5 / Ka
                                end
                            elseif Ka > 262 then
                                lb = Va._["table"]
                                lb, pa, Ka, I = Cb, {}, 0x8e, lb["insert"]
                                pa["id"] = na
                                M = x["DisplayName"]
                                pa["name"] = M
                                t, M = x["Price"], Va._["tonumber"]
                            else
                                Ka, ob = Ka + -0x9a, ob(v)
                            end
                        elseif Ka >= 257 then
                            if Ka > 257 then
                                Pb = Pb(B)
                                Na["Scrim"] = Pb
                                Ka, Pb = 0x182, 0.48
                                Na["ScrimTransparency"] = Pb
                                E = Na
                                E = {[2] = 3, [3] = E}
                                E[1] = E
                                B, Na, Pb, Fb = "Ember", ua[1][ua[2]].RegisterTheme, ua[1][ua[2]], E[1][E[2]]
                            else
                                Ka, K = 0x16f - Ka, K(Gb)
                            end
                        else
                            Ka = Cb and 0xcf or Ka + 0xc6
                        end
                    elseif Ka >= 340 then
                        if Ka >= 0x17a then
                            if Ka < 394 then
                                if Ka < 0x182 then
                                    if Ka < 0x17b then
                                        P = P(G, S, w)
                                        Ka, J["RequestHatchEgg"] = 0x2ddda / Ka, P
                                        w, G, S, P = "RequestCompleteHatchEgg", ab, "FinishHatch", Na[1][Na[2]]["pickFn"]
                                    elseif Ka > 0x17b then
                                        Wa = Wa(tb)
                                        Ka = Wa and Ka + -0x133 or 0x21d - Ka
                                    else
                                        vb = vb(rb, Wa, tb)
                                        w["Deserialize"] = vb
                                        Ka, S = 0x3f1 - Ka, w
                                        S = {[2] = 3, [3] = S}
                                        S[1] = S
                                        tb, K, vb, rb, Wa = "MayEnterFuse", "CanSelectPet", {}, Na[1][Na[2]]["pickFn"], h
                                    end
                                elseif Ka < 0x185 then
                                    Ka = Ka + 0x250
                                    Na(Pb, B, Fb)
                                    B, Na, Pb = "Ember", ua[1][ua[2]].SetTheme, ua[1][ua[2]]
                                elseif Ka > 389 then
                                    Ka = fb and 504 or 0x50b - Ka
                                else
                                    Ka, K = 0x3fd2 / Ka, K(Gb)
                                end
                            elseif Ka > 0x195 then
                                if Ka < 0x198 then
                                    Ka, Pb = 0x38b - Ka, Pb(B)
                                    Na["Error"] = Pb
                                    Pb, B = bb, "6FA8DC"
                                elseif Ka > 0x198 then
                                    Ka, Pb = 0x1ac2c / Ka, Pb(B)
                                    Na["AccentPressed"] = Pb
                                    B, Pb = "1A0A04", bb
                                else
                                    j = j(ab, N, Lb, sa)
                                    Ka = j and 0x3af8 / Ka or 0x4950 / Ka
                                end
                            elseif Ka < 0x191 then
                                if Ka <= 394 then
                                    K = K(Gb, X, da)
                                    Ka = K and 9 or 0x2804 / Ka
                                else
                                    I(lb, pa)
                                    I, lb = x["name"], x["id"]
                                    Ka, ta[1][ta[2]][I] = 0x4bf - Ka, lb
                                    I, lb = x["name"], x["price"]
                                    R[1][R[2]][I] = lb
                                end
                            elseif Ka > 401 then
                                Ka, Wa = 482 - Ka, Wa(tb)
                            else
                                Ka, Y, Ta, fb, u = 0x2ce, "Areas", qa, qa.WaitForChild, 8
                            end
                        elseif Ka <= 357 then
                            if Ka > 0x15e then
                                if Ka < 353 then
                                    A = Va._["table"]
                                    Ka, ca, A, Aa = 0x284e0 / Ka, p, Y[1][Y[2]], A["insert"]
                                elseif Ka > 0x161 then
                                    Ka, K = 0x258 - Ka, K(Gb)
                                else
                                    za = za(nb)
                                    za = {[2] = 3, [3] = za}
                                    za[1] = za
                                    nb = za[1][za[2]]
                                    nb = {[2] = 3, [3] = nb}
                                    nb[1] = nb
                                    T, eb = 18, #nb[1][nb[2]]
                                    Ka = eb > T and 0x24a or 0x4e2ab / Ka
                                end
                            elseif Ka <= 343 then
                                if Ka < 0x156 then
                                    Lb = Lb(sa, d, h, Ib, kb)
                                    Ka = Lb and 0xd480 / Ka or 18
                                elseif Ka <= 0x156 then
                                    la = la()
                                    la = {[2] = 3, [3] = la}
                                    la[1] = la
                                    ea = {}
                                    La = ea
                                    La = {[2] = 3, [3] = La}
                                    La[1] = La
                                    g = {}
                                    ea = g
                                    ea = {[2] = 3, [3] = ea}
                                    ea[1] = ea
                                    g = false
                                    g = {[2] = 3, [3] = g}
                                    g[1] = g
                                    Ja = nil
                                    Ja = {[2] = 3, [3] = Ja}
                                    Ja[1] = Ja
                                    F = 0
                                    F = {[2] = 3, [3] = F}
                                    F[1] = F
                                    Fa = 0
                                    Fa = {[2] = 3, [3] = Fa}
                                    Fa[1] = Fa
                                    Ca = 0
                                    Ca = {[2] = 3, [3] = Ca}
                                    Ca[1] = Ca
                                    Qa = 0
                                    Qa = {[2] = 3, [3] = Qa}
                                    Qa[1] = Qa
                                    sb = {}
                                    Ha = sb
                                    Ha = {[2] = 3, [3] = Ha}
                                    Ha[1] = Ha
                                    db = {}
                                    sb = db
                                    sb = {[2] = 3, [3] = sb}
                                    sb[1] = sb
                                    C = {}
                                    db = C
                                    db = {[2] = 3, [3] = db}
                                    db[1] = db
                                    ja = {}
                                    C = ja
                                    C = {[2] = 3, [3] = C}
                                    C[1] = C
                                    ka = {}
                                    ja = ka
                                    ja = {[2] = 3, [3] = ja}
                                    ja[1] = ja
                                    ka = Va._["getgenv"]
                                    Ka = ka and 0x114 or 0x178bc / Ka
                                else
                                    G = G(S, w, vb)
                                    P["GetSlotOwner"] = G
                                    J = P
                                    J = {[2] = 3, [3] = J}
                                    Ka, J[1] = 0x16f, J
                                    vb, G, rb, S, w = "LooksLikeFirstAreaUid", {}, "IsFirstAreaUid", Na[1][Na[2]]["pickFn"], Lb
                                end
                            else
                                Sa = Sa(j, ab, N, Lb)
                                Ka = Sa and 0x5d or Ka + -156
                            end
                        elseif Ka > 0x16f then
                            if Ka <= 0x171 then
                                ca(Va.d(U))
                                U, Ka, ca, mb = wb[1][wb[2]]["RenderStepped"], 0x325, Na[1][Na[2]]["track"], Va:x{Na, jb, Ya, cb}
                                U, va = U.Connect, U
                            else
                                Pa = Pa(Q, Xa)
                                Ka, Pa = 0x30b, {[2] = 3, [3] = Pa}
                                Pa[1] = Pa
                                Q, ob = Va._["game"], "TweenService"
                                Q, Xa = Q.GetService, Q
                            end
                        elseif Ka < 366 then
                            if Ka > 361 then
                                Ka, S = 0x3fe54 / Ka, S(w, vb, rb)
                                G["BuildSlotKey"] = S
                                P = G
                                P = {[2] = 3, [3] = P}
                                P[1] = P
                                vb, S, rb, w, Wa = sa, {}, "ReadSnapshot", Na[1][Na[2]]["pickFn"], "GetRuntimeSnapshot"
                            else
                                Ka, G = 0x118, G(S, w, vb)
                                P["GetPlotData"] = G
                                w, G, vb, S = "ContainsLocalPoint", Na[1][Na[2]]["pickFn"], "IsWorldPositionWithinLocalPlotBounds", N
                            end
                        elseif Ka > 0x16e then
                            Ka, S = 0x209d4 / Ka, S(w, vb, rb)
                            G["IsFirstAreaUid"] = S
                            rb, S, w, vb = "BuildSlotKey", Na[1][Na[2]]["pickFn"], Lb, "SlotKey"
                        else
                            ta = ta(R)
                            Ka, R = 494 - Ka, "table"
                            r = ta == R
                        end
                    elseif Ka > 310 then
                        if Ka >= 325 then
                            if Ka < 334 then
                                if Ka <= 326 then
                                    if Ka > 0x145 then
                                        Ka = Ka + -79
                                        r(ta)
                                    else
                                        Pb = Pb(B)
                                        Ka, Na["TextTertiary"] = Ka + -15, Pb
                                        Pb, B = bb, "735447"
                                    end
                                else
                                    Ka, Bb = 0x1ee, Bb(q, o)
                                    Oa["protect_gui"] = Bb
                                    v = Oa
                                    v = {[2] = 3, [3] = v}
                                    v[1] = v
                                    Bb, Oa = Va:Jb{ob, ya}, Va._["pcall"]
                                end
                            elseif Ka <= 338 then
                                if Ka <= 0x14e then
                                    Ka = 0x227
                                    Y(Va.d(u))
                                else
                                    Ka = 0x209 - Ka
                                    Gb(X, da, n, ba)
                                end
                            else
                                Ka, Db = 0x484 - Ka, Db(wb, hb)
                                Db = {[2] = 3, [3] = Db}
                                Db[1] = Db
                                wb, a = Va._["game"], "RunService"
                                wb, hb = wb.GetService, wb
                            end
                        elseif Ka < 0x13d then
                            if Ka > 313 then
                                Ka, M = Ka + -0x23, 0
                            elseif Ka <= 312 then
                                Ka, U = 0x315, Va.c(U(va, mb))
                            else
                                jb, aa = {}, 0.55
                                jb["GrabDelay"] = aa
                                aa = 0.12
                                jb["ReturnPace"] = aa
                                aa = 1.35
                                jb["ArriveDistance"] = aa
                                aa = 14
                                jb["MoveTimeout"] = aa
                                aa = 0.08
                                jb["DropRetryDelay"] = aa
                                aa = 1.2
                                jb["DropVerifyTimeout"] = aa
                                aa = 0.18
                                jb["RegrabDelay"] = aa
                                aa = 1
                                jb["RegrabTimeout"] = aa
                                _ = jb
                                _ = {[2] = 3, [3] = _}
                                _[1] = _
                                jb = true
                                jb = {[2] = 3, [3] = jb}
                                jb[1] = jb
                                na = {}
                                aa = na
                                aa = {[2] = 3, [3] = aa}
                                aa[1] = aa
                                na = nil
                                na = {[2] = 3, [3] = na}
                                na[1] = na
                                x = nil
                                x = {[2] = 3, [3] = x}
                                x[1] = x
                                I = nil
                                I = {[2] = 3, [3] = I}
                                I[1] = I
                                lb = nil
                                lb = {[2] = 3, [3] = lb}
                                lb[1] = lb
                                pa = nil
                                pa = {[2] = 3, [3] = pa}
                                Ka, pa[1] = Ka + 40, pa
                                M = nil
                                M = {[2] = 3, [3] = M}
                                M[1] = M
                                t = nil
                                t = {[2] = 3, [3] = t}
                                t[1] = t
                                Ob = nil
                                Ob = {[2] = 3, [3] = Ob}
                                Ob[1] = Ob
                                y = nil
                                y = {[2] = 3, [3] = y}
                                y[1] = y
                                Hb = nil
                                Hb = {[2] = 3, [3] = Hb}
                                Hb[1] = Hb
                                nb, za = Va._["game"], Va._["tostring"]
                                nb = nb["JobId"]
                            end
                        elseif Ka >= 321 then
                            if Ka <= 0x141 then
                                Ka, K = 30, K(Gb)
                            else
                                Ka, K = 475 - Ka, K(Gb)
                            end
                        else
                            wb = wb(hb)
                            Db = not wb
                            Ka = Db and 123 or 0x10df2 / Ka
                        end
                    elseif Ka <= 0x12e then
                        if Ka < 0x123 then
                            if Ka >= 0x11a then
                                if Ka <= 282 then
                                    qa, ka, Ka, fb = cb[1][cb[2]], cb[1][cb[2]].FindFirstChild, 0x1c4be / Ka, "__OBJECTS"
                                else
                                    Ka = 0x316
                                    u(Va.d(zb))
                                    zb, Ab, u = a[1][a[2]]["TeleportInitFailed"], Va:Ua{Ia, ob}, Na[1][Na[2]]["track"]
                                    zb, b = zb.Connect, zb
                                end
                            else
                                Ka, pa["price"] = 0x2a1, M
                            end
                        elseif Ka < 0x129 then
                            if Ka > 0x123 then
                                Pb = Pb(B)
                                Na["Warning"] = Pb
                                Ka, Pb, B = 0x197, bb, "EF5B5B"
                            else
                                Ka, tb = 0x93c6 / Ka, tb(K)
                            end
                        elseif Ka <= 297 then
                            K = K(Gb, X, da)
                            Ka = K and Ka + -54 or 17
                        else
                            Ka, N = 11, N(Lb)
                        end
                    elseif Ka >= 308 then
                        if Ka <= 0x135 then
                            if Ka > 0x134 then
                                Ka, K = 0xc12 / Ka, K(Gb)
                            else
                                Ka, pa = 0x279, 0
                            end
                        else
                            Pb = Pb(B)
                            Na["TextDisabled"] = Pb
                            Ka, B, Pb = 0x48472 / Ka, "F26A2E", bb
                        end
                    elseif Ka <= 0x130 then
                        if Ka <= 0x12f then
                            Pb = Pb(B)
                            Na["ControlHover"] = Pb
                            B, Ka, Pb = "512E1F", 0x4c0 - Ka, bb
                        else
                            Ka, P = 0x4b2f0 / Ka, P(G, S, w)
                            J["RequestEquipTool"] = P
                            P, w, G, S = Na[1][Na[2]]["pickFn"], "RequestPlaceEgg", ab, "PlantEgg"
                        end
                    else
                        Ka, K = 0x62, K(Gb)
                    end
                elseif Ka >= 108 then
                    if Ka >= 150 then
                        if Ka <= 0xaa then
                            if Ka > 160 then
                                if Ka < 0xa7 then
                                    if Ka > 0xa3 then
                                        Ka, sa, d = 0x3fd, Na[1][Na[2]]["findModule"], "AssetRoster"
                                    elseif Ka <= 161 then
                                        Ka, ta = 326, Va._["table"]
                                        ta, r = Eb[1][Eb[2]], ta["sort"]
                                    else
                                        K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], 0x141, "AskChoose"
                                    end
                                elseif Ka <= 0xa8 then
                                    if Ka <= 167 then
                                        Ka, Gb, K = Ka + 0xde, "FetchSummary", Na[1][Na[2]]["findRemoteContains"]
                                    else
                                        K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], Ka + 0x62, "FinishReveal"
                                    end
                                else
                                    sa, N, d, Lb, Ka, h = 6, Na[1][Na[2]]["requirePath"], "Client", l[1][l[2]], 0x491 - Ka, "PlotState"
                                end
                            elseif Ka < 0x9b then
                                if Ka < 152 then
                                    if Ka > 0x96 then
                                        Ka = K and Ka + -0x59 or 0x74
                                    else
                                        u = u(zb)
                                        zb = "function"
                                        Ka, Y = 0x329 - Ka, u == zb
                                    end
                                elseif Ka > 152 then
                                    tb["WORN_SNAPSHOT"] = K
                                    Wa = tb
                                    Ka, rb["Trails"] = 0x2ed, Wa
                                    K, Gb, X, da, tb = Na[1][Na[2]]["remoteFrom"], Ib, "GroupPerk", "RedeemPerk", {}
                                else
                                    Db = Va._["type"]
                                    Ka, Va._["typeof"] = 97, Db
                                end
                            elseif Ka <= 158 then
                                if Ka > 0x9d then
                                    Ka = 0x9910 / Ka
                                    ua(bb)
                                elseif Ka > 0x9b then
                                    Ka, Wa, tb = 405, Na[1][Na[2]]["findRemoteContains"], "AskFieldEggSnapshot"
                                else
                                    Ka, h, Ib = 0x346, Na[1][Na[2]]["findModule"], "FuseKernel"
                                end
                            else
                                kb, Ka, d, Ib, h, sa = "AssetRoster", 0x3fc, l[1][l[2]], "Client", 4, Na[1][Na[2]]["requirePath"]
                            end
                        elseif Ka >= 185 then
                            if Ka < 0xbf then
                                if Ka >= 0xbc then
                                    if Ka <= 188 then
                                        r, Ka, ta = Na[1][Na[2]]["cloneList"], 0x205bc / Ka, ra[1][ra[2]]
                                    else
                                        ua, Ka, bb = Va._["pcall"], 0x311, Va:P{v, ya}
                                    end
                                else
                                    aa = Va._["table"]
                                    na, aa, Ka, jb = Cb, Eb[1][Eb[2]], 0x29e, aa["insert"]
                                end
                            elseif Ka > 0xc2 then
                                Ka, _ = 0x246, O
                            elseif Ka <= 0xc0 then
                                if Ka > 191 then
                                    ua, Ka, bb, Na, E = Va._["error"], 0x339, "[MMB HUB] UI load failed: ", o, Va._["tostring"]
                                else
                                    wb, Db = Va._["table"], Va:Y()
                                    Ka, wb["pack"] = 2, Db
                                end
                            else
                                Ka, Sa, j = 0x327, Na[1][Na[2]]["findModule"], "Trails"
                            end
                        elseif Ka < 0xb4 then
                            if Ka >= 175 then
                                if Ka > 175 then
                                    K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], 0x3ff, "AskDoff"
                                else
                                    Ka = ya and 0xbc - Ka or 0xf6
                                end
                            else
                                Gb = not K
                                Ka = Gb and 0x6a or 355 - Ka
                            end
                        elseif Ka < 0xb6 then
                            Ka, K, Gb = 502 - Ka, Na[1][Na[2]]["findRemoteContains"], "AskWornSnapshot"
                        elseif Ka > 182 then
                            ba, z, X, n, ra, c, L, yb, Eb, r, da = "Rare", "Mythic", {}, "Uncommon", "Secret", "Legendary", "Cosmic", "Epic", "Eternal", "Divine", "Common"
                            X[1], X[2], X[3], X[4], X[5], X[6], X[7], X[8], X[9], X[10] = da, n, ba, yb, c, z, L, ra, Eb, r
                            Gb = X
                            Gb = {[2] = 3, [3] = Gb}
                            Gb[1] = Gb
                            n, da = 1, {}
                            da["Common"] = n
                            n = 2
                            da["Uncommon"] = n
                            n = 3
                            da["Rare"] = n
                            n = 4
                            da["Epic"] = n
                            n = 5
                            da["Legendary"] = n
                            n = 6
                            da["Mythic"] = n
                            n = 7
                            da["Cosmic"] = n
                            n = 8
                            da["Secret"] = n
                            n = 9
                            da["Eternal"] = n
                            n = 10
                            da["Divine"] = n
                            X = da
                            X = {[2] = 3, [3] = X}
                            X[1] = X
                            c, n, yb, ba = "Silver", {}, "Rainbow", "Golden"
                            n[1], n[2], n[3] = ba, yb, c
                            da = n
                            da = {[2] = 3, [3] = da}
                            da[1] = da
                            L, c, ba, yb, z = "Biggest Size", "Nearest", {}, "Rarest", "Furthest"
                            ba[1], ba[2], ba[3], ba[4] = yb, c, z, L
                            n = ba
                            n = {[2] = 3, [3] = n}
                            n[1] = n
                            L, c, yb, z = "Most Duplicates", "Highest Rarity", {}, "Lowest Rarity"
                            yb[1], yb[2], yb[3] = c, z, L
                            ba = yb
                            ba = {[2] = 3, [3] = ba}
                            ba[1] = ba
                            z, c, L = "Base", {}, "Treadmill"
                            c[1], c[2] = z, L
                            yb = c
                            yb = {[2] = 3, [3] = yb}
                            yb[1] = yb
                            z, Eb, r, ra, L = {}, "Auto Hatch", "Auto Treadmill", "Auto Place Egg", "Auto Steal Egg"
                            z[1], z[2], z[3], z[4] = L, ra, Eb, r
                            c = z
                            c = {[2] = 3, [3] = c}
                            c[1] = c
                            ra, ta, r, Eb, L = "PrioritySlot1", "PrioritySlot4", "PrioritySlot3", "PrioritySlot2", {}
                            L[1], L[2], L[3], L[4] = ra, Eb, r, ta
                            z = L
                            z = {[2] = 3, [3] = z}
                            z[1] = z
                            ta, ra, r, Eb = "After Steal Count", {}, "Timed Interval", "No Matching Eggs"
                            ra[1], ra[2], ra[3] = Eb, r, ta
                            L = ra
                            L = {[2] = 3, [3] = L}
                            L[1] = L
                            Cb, jb, Eb, ta, aa, x, R, r, na, _ = "Jungle", "Volcano", {}, "Lake", "Abyss Ocean", "Cosmic", "Desert", "Forest", "Prehistoric", "Snow"
                            Eb[1], Eb[2], Eb[3], Eb[4], Eb[5], Eb[6], Eb[7], Eb[8], Eb[9] = r, ta, R, Cb, _, jb, aa, na, x
                            ra = Eb
                            ra = {[2] = 3, [3] = ra}
                            ra[1] = ra
                            r = {}
                            Eb = r
                            Eb = {[2] = 3, [3] = Eb}
                            Eb[1] = Eb
                            r = ga
                            Ka = r and 0xeb or 0x137 - Ka
                        else
                            Ka, tb["ACKNOWLEDGE_INFO"] = Ka + -0x24, K
                            Gb, K, X, da = Ib, Na[1][Na[2]]["remoteFrom"], "Fusery", "LoadPet"
                        end
                    elseif Ka > 0x83 then
                        if Ka > 142 then
                            if Ka <= 147 then
                                if Ka <= 0x92 then
                                    if Ka <= 143 then
                                        tb["REQUEST_CLAIM_ALL"] = K
                                        Wa = tb
                                        Ka, rb["Index"] = Ka + 0x2e7, Wa
                                        da, X, Gb, K, tb = "SellPet", "PetSatchel", Ib, Na[1][Na[2]]["remoteFrom"], {}
                                    else
                                        K = K(Gb, X, da)
                                        Ka = K and Ka + -36 or 0x832c / Ka
                                    end
                                else
                                    Ka, ya = 0x235 - Ka, Va._["getgenv"]
                                end
                            elseif Ka > 0x94 then
                                wb, Db = Va._["unpack"], Va._["table"]
                                Ka, Db["unpack"] = Ka + -0x36, wb
                            else
                                Ka, K = 204, Va:C{rb}
                                kb[1][kb[2]]["RequestCarryAreaEgg"] = K
                            end
                        elseif Ka >= 138 then
                            if Ka <= 141 then
                                if Ka <= 140 then
                                    if Ka <= 138 then
                                        Ib, J, kb, G, Ka, h, P = l[1][l[2]], "Shared", 4, "FuseKernel", 0x22a, Na[1][Na[2]]["requirePath"], "Util"
                                    else
                                        K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], 0x3df - Ka, "BeginFuse"
                                    end
                                else
                                    K = K(Gb, X, da)
                                    Ka = K and 82 or 0x5c88 / Ka
                                end
                            else
                                M = M(t)
                                Ka = M and 0x119 or 316
                            end
                        elseif Ka < 135 then
                            Db = ya[1][ya[2]]["__MMB_HUB_RUNNING"]
                            Ka = Db and Ka + 76 or 222
                        elseif Ka <= 135 then
                            Ka, j = 0x1383 / Ka, j(ab)
                        else
                            Ka, K = Ka + -70, tb[1][tb[2]]
                        end
                    elseif Ka < 0x7b then
                        if Ka <= 0x74 then
                            if Ka < 113 then
                                if Ka <= 108 then
                                    ob = {[2] = 3, [3] = ob}
                                    ob[1] = ob
                                    Ka, Oa, v = 0x1461c / Ka, Va:s{ob}, Va._["pcall"]
                                else
                                    Ka, tb["INSERT_MOB"] = 429, K
                                    K, da, X, Gb = Na[1][Na[2]]["remoteFrom"], "BeginFuse", "Fusery", Ib
                                end
                            elseif Ka > 113 then
                                Gb = kb[1][kb[2]]["RequestPlaceEgg"]
                                K = not Gb
                                Ka = K and 136 or 0x1de8 / Ka
                            else
                                ya = Va._["getgenv"]
                                Ka = ya and 147 or 175
                            end
                        elseif Ka >= 118 then
                            if Ka <= 0x76 then
                                Ka = K and 148 or 0xcc
                            else
                                Ka, ga, ib = 0x235, Na[1][Na[2]]["findModule"], "Areas"
                            end
                        else
                            Ka, K, Gb = 426 - Ka, Na[1][Na[2]]["findRemoteContains"], "AskCollect"
                        end
                    elseif Ka > 0x80 then
                        if Ka >= 130 then
                            if Ka > 130 then
                                Ab, p = u(zb, b)
                                b = Ab
                                Ka = b == nil and 0x1fa9a / Ka or 0xb420 / Ka
                            else
                                tb = {[2] = 3, [3] = tb}
                                tb[1] = tb
                                Gb = kb[1][kb[2]]["RequestCarryAreaEgg"]
                                K = not Gb
                                Ka = K and 0x281e / Ka or 0x76
                            end
                        else
                            Ka, jb = Ka + 486, Va._["table"]
                            jb, _, aa = Cb, jb["sort"], Va:sb()
                        end
                    elseif Ka > 126 then
                        Ka = r and 0x7200 / Ka or 188
                    elseif Ka < 124 then
                        wb = Va._["game"]
                        Db = wb["Loaded"]
                        Db, Ka, wb = Db.Wait, 0x328, Db
                    elseif Ka <= 124 then
                        Gb = nil
                        Ka, K = 0x128 - Ka, ab ~= Gb
                    else
                        ib = {[2] = 3, [3] = ib}
                        Ka, ib[1] = 0x315 - Ka, ib
                        O, ab, j, Sa, N = Na[1][Na[2]]["requirePath"], "Data", 4, l[1][l[2]], "Gears"
                    end
                elseif Ka >= 60 then
                    if Ka < 0x53 then
                        if Ka > 72 then
                            if Ka >= 79 then
                                if Ka < 80 then
                                    Ka, K = 0x246a / Ka, rb[1][rb[2]]
                                elseif Ka <= 80 then
                                    Ka, P = 0xa00 / Ka, ab["AreaEggCarryStateChanged"]
                                else
                                    tb["COMPLETE_REVEAL"] = K
                                    X, K, Ka, Gb, da = "Fusery", Na[1][Na[2]]["remoteFrom"], Ka + 0x278, Ib, "ConfirmBriefing"
                                end
                            elseif Ka >= 0x4b then
                                if Ka <= 0x4b then
                                    Ka, N, j, Sa, Lb, ab = Ka + 275, "Data", l[1][l[2]], Na[1][Na[2]]["requirePath"], "Trails", 4
                                else
                                    Wa = {[2] = 3, [3] = Wa}
                                    Ka, Wa[1] = 0x396 - Ka, Wa
                                    tb, K = Na[1][Na[2]]["findRemote"], "RF/EggWorld/AskPlaceEgg"
                                end
                            else
                                Ka, wb, Db = 0x332 - Ka, ya[1][ya[2]]["__MMB_HUB_SHUTDOWN"], Va._["pcall"]
                            end
                        elseif Ka >= 66 then
                            if Ka <= 0x46 then
                                if Ka > 68 then
                                    Ka = K and 231 or 38
                                elseif Ka <= 0x42 then
                                    Ka = K and Ka + 0xbc or 0x3c
                                else
                                    tb["REQUEST_BASE_UPGRADE"] = K
                                    Wa = tb
                                    Ka, rb["Plots"] = Ka + 0x146, Wa
                                    K, X, Gb, da, tb = Na[1][Na[2]]["remoteFrom"], "Treadmill", Ib, "AskTierRaise", {}
                                end
                            else
                                Ka, K, Gb = 0xcb, Na[1][Na[2]]["findRemoteContains"], "BaseUpgrade"
                            end
                        elseif Ka >= 62 then
                            if Ka > 62 then
                                P = ab["CarryChanged"]
                                Ka = P and 32 or Ka + 15
                            else
                                Ka, K = Ka + 0x36, Va:_b{Wa}
                                kb[1][kb[2]]["RequestAreaEggSnapshot"] = K
                            end
                        else
                            Gb = nil
                            K = Pb[1][Pb[2]] ~= Gb
                            Ka = K and 0xb8 - Ka or Ka + 112
                        end
                    elseif Ka <= 0x5f then
                        if Ka > 90 then
                            if Ka > 93 then
                                wb, Ka, Db = Va._["typeof"], 0x1e5, Va._["type"]
                            elseif Ka > 92 then
                                sa, Lb, ab, j, Ka, N = "Treadmills", "Data", l[1][l[2]], Na[1][Na[2]]["requirePath"], Ka + 0x13b, 4
                            else
                                Ka, Gb, K = 0x6e54 / Ka, "WearBest", Na[1][Na[2]]["findRemoteContains"]
                            end
                        elseif Ka > 0x56 then
                            ob = Db[1][Db[2]]["PlayerAdded"]
                            v, Ka, ob = ob, 352 - Ka, ob.Wait
                        elseif Ka > 0x54 then
                            J, h, Ka, d, P, kb, Ib = "Util", l[1][l[2]], 0x26d, Na[1][Na[2]]["requirePath"], "AssetItems", "Shared", 4
                        elseif Ka > 0x53 then
                            Ka, Ib, kb = 0x2e8 - Ka, Na[1][Na[2]]["findModule"], "Remotes"
                        else
                            tb["REQUEST_EQUIP_STATIC"] = K
                            Ka, da, X, Gb, K = Ka + 0x387, "AskDoff", "Treadmill", Ib, Na[1][Na[2]]["remoteFrom"]
                        end
                    elseif Ka < 0x64 then
                        if Ka < 97 then
                            Fb, Ka, _b = Na[1][Na[2]]["findModule"], 0x371, "BaseUpgrade"
                        elseif Ka <= 0x61 then
                            Db, Ka, wb = Va._["type"], 0x2e1, ya[1][ya[2]]["__MMB_HUB_SHUTDOWN"]
                        else
                            Ka = K and 0x18 or 201
                        end
                    elseif Ka > 104 then
                        da, Ka, ba, n, Gb, X = "Some game modules were not found - a few features may no-op", 0x152, 5, "Warning", Na[1][Na[2]]["notify"], "Bind"
                    elseif Ka <= 0x64 then
                        h, Ka, d = "AssetItems", 0x16b48 / Ka, Na[1][Na[2]]["findModule"]
                    else
                        rb = {[2] = 3, [3] = rb}
                        rb[1] = rb
                        Wa, Ka, tb = Na[1][Na[2]]["findRemote"], Ka + 280, "RF/EggWorld/AskFieldEggSnapshot"
                    end
                elseif Ka <= 27 then
                    if Ka < 18 then
                        if Ka < 10 then
                            if Ka < 2 then
                                kb = Va:na()
                                Ka, Na[1][Na[2]]["pickFn"] = 213, kb
                                G, w, J, S, P = ab, "GetAreaEggSnapshot", {}, "ReadFieldEggs", Na[1][Na[2]]["pickFn"]
                            elseif Ka <= 2 then
                                Db, wb = Va._["type"], Va._["table"]
                                Ka, wb = 0x574 / Ka, wb["unpack"]
                            else
                                Ka, tb["REQUEST_UPGRADE"] = Ka + 0x2b4, K
                                da, Gb, X, K = "AskWearStill", Ib, "Treadmill", Na[1][Na[2]]["remoteFrom"]
                            end
                        elseif Ka > 13 then
                            K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], 357, "AskBaseTierRaise"
                        elseif Ka < 11 then
                            tb["REQUEST_REDEEM"] = K
                            Ka, Wa = 0x8d, tb
                            rb["OfflineAssets"] = Wa
                            Gb, da, X, K, tb = Ib, "FinishReveal", "Fusery", Na[1][Na[2]]["remoteFrom"], {}
                        elseif Ka > 11 then
                            ya = {[2] = 3, [3] = ya}
                            ya[1] = ya
                            Db, Ka, wb = Va._["type"], 0x2c8 - Ka, Va._["table"]
                            wb = wb["pack"]
                        else
                            Ib, Lb, kb, Ka, sa, h, d = "Util", Na[1][Na[2]]["requirePath"], "AreaEggSlotIdentity", 0x154, l[1][l[2]], "Shared", 4
                        end
                    elseif Ka < 0x17 then
                        if Ka < 19 then
                            Ka, Lb, sa = 0x3a3, Na[1][Na[2]]["findModule"], "AreaEggSlotIdentity"
                        elseif Ka <= 19 then
                            Ka, N, ab = 459, "EggState", Na[1][Na[2]]["findModule"]
                        else
                            B = {[2] = 3, [3] = B}
                            Ka, B[1] = Ka + 0x2f0, B
                            O, ib, ga, _b, Fb = "BaseUpgrade", "Client", 4, l[1][l[2]], Na[1][Na[2]]["requirePath"]
                        end
                    elseif Ka >= 26 then
                        if Ka <= 0x1a then
                            Ka, Gb, K = 0x2b9, "AskTierRaise", Na[1][Na[2]]["findRemoteContains"]
                        else
                            Ka, tb["START_FUSE"] = Ka + 466, K
                            Wa = tb
                            rb["FuseMachine"] = Wa
                            da, Gb, tb, X, K = "AskPurchase", Ib, {}, "Trailwear", Na[1][Na[2]]["remoteFrom"]
                        end
                    elseif Ka <= 23 then
                        tb["REQUEST_UNEQUIP"] = K
                        Wa = tb
                        Ka, rb["Treadmills"] = 0x2b3, Wa
                        X, tb, Gb, K, da = "Codex", {}, Ib, Na[1][Na[2]]["remoteFrom"], "AskRedeemAll"
                    else
                        tb["EQUIP_BEST"] = K
                        Ka, Wa = 0x129, tb
                        rb["Backpack"] = Wa
                        X, K, Gb, tb, da = "Homestead", Na[1][Na[2]]["remoteFrom"], Ib, {}, "AskBaseTierRaise"
                    end
                elseif Ka < 0x2c then
                    if Ka < 0x25 then
                        if Ka > 32 then
                            Ka, Gb, K = 0x338 - Ka, "SellPet", Na[1][Na[2]]["findRemoteContains"]
                        elseif Ka <= 30 then
                            Ka, tb["REQUEST_SELECT"] = Ka + 0x297, K
                            X, K, da, Gb = "Trailwear", Na[1][Na[2]]["remoteFrom"], "AskWornSnapshot", Ib
                        else
                            J["AreaEggCarryStateChanged"] = P
                            w, Ka, P, S, G = "RequestCarryAreaEgg", 0x38f, Na[1][Na[2]]["pickFn"], "CarryFieldEgg", ab
                        end
                    elseif Ka >= 38 then
                        if Ka <= 38 then
                            K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], 219, "SELL_ASSET"
                        else
                            tb["GET_SUMMARY"] = K
                            da, Gb, Ka, X, K = "AskCollect", Ib, Ka + 377, "AwayEarnings", Na[1][Na[2]]["remoteFrom"]
                        end
                    else
                        j = {[2] = 3, [3] = j}
                        Ka, j[1] = 0x3fa, j
                        Lb, d, sa, N, ab = 6, "EggState", "Client", l[1][l[2]], Na[1][Na[2]]["requirePath"]
                    end
                elseif Ka < 52 then
                    if Ka <= 46 then
                        if Ka <= 0x2c then
                            tb["REQUEST_PURCHASE"] = K
                            da, Ka, Gb, X, K = "AskChoose", 0x292, Ib, "Trailwear", Na[1][Na[2]]["remoteFrom"]
                        else
                            Ka, j, ab = 135, Na[1][Na[2]]["findModule"], "Treadmills"
                        end
                    else
                        K, Ka, Gb = Na[1][Na[2]]["findRemoteContains"], 0x3f4, "AskWearStill"
                    end
                elseif Ka >= 54 then
                    if Ka <= 0x36 then
                        Ka, Gb, K = 0x8040 / Ka, "RedeemPerk", Na[1][Na[2]]["findRemoteContains"]
                    else
                        Ka, Sa, O = 0x2de, "Gears", Na[1][Na[2]]["findModule"]
                    end
                else
                    Ka, N, Lb = Ka + 0xfa, Na[1][Na[2]]["findModule"], "PlotState"
                end
            elseif Ka < 0x2c6 then
                if Ka <= 0x23b then
                    if Ka <= 0x1e7 then
                        if Ka <= 459 then
                            if Ka <= 0x1af then
                                if Ka > 0x1aa then
                                    if Ka <= 430 then
                                        if Ka <= 0x1ad then
                                            K = K(Gb, X, da)
                                            Ka = K and 0x2d3f / Ka or 0x8c
                                        else
                                            _, Ka, jb = Va._["typeof"], Ka + 443, Sa["Directory"]
                                        end
                                    else
                                        Na(Pb)
                                        Ka, Pb = 476, Va:Vb{E, ua}
                                    end
                                elseif Ka <= 418 then
                                    if Ka < 416 then
                                        ka = ka(qa, fb)
                                        Ka = ka and 0x2fa or 0x3c3
                                    elseif Ka > 0x1a0 then
                                        Ka, ya = 175, ya()
                                    else
                                        Ka, f = 0x32600 / Ka, Va.c(f(oa, Ra))
                                    end
                                elseif Ka <= 0x1a3 then
                                    K = K(Gb, X, da)
                                    Ka = K and 10 or 117
                                else
                                    Ka, B = 0x14, B(Fb)
                                end
                            elseif Ka <= 0x1c6 then
                                if Ka >= 444 then
                                    if Ka <= 444 then
                                        K = K(Gb, X, da)
                                        Ka = K and 0xa9f8 / Ka or Ka + -352
                                    else
                                        _ = {}
                                        Cb = _
                                        Cb = {[2] = 3, [3] = Cb}
                                        Cb[1] = Cb
                                        Ka = O and 0x309 or Ka + -0x8d
                                    end
                                elseif Ka > 0x1b3 then
                                    ca(Va.d(U))
                                    Ka, U, mb, ca = Ka + 322, Ya[1][Ya[2]]["InputBegan"], Va:la{gb}, Na[1][Na[2]]["track"]
                                    U, va = U.Connect, U
                                else
                                    pa = pa(M)
                                    M = "table"
                                    lb = pa == M
                                    Ka = lb and 460 or Ka + 383
                                end
                            elseif Ka > 0x1ca then
                                Ka, ab = 0x130ce / Ka, ab(N)
                            else
                                Pb = Pb(B)
                                Na["BorderStrong"] = Pb
                                B, Ka, Pb = "FFF1E8", 0x23c, bb
                            end
                        elseif Ka >= 0x1d6 then
                            if Ka > 480 then
                                if Ka < 0x1e5 then
                                    Pb = Pb(B)
                                    Ka, Na["SurfaceActive"] = Ka + 219, Pb
                                    B, Pb = "352017", bb
                                elseif Ka <= 485 then
                                    Db = Db(wb)
                                    wb = "function"
                                    Ka = Db ~= wb and 0x27d - Ka or 0x246 - Ka
                                else
                                    Pb = Pb(B)
                                    Na["SurfaceHover"] = Pb
                                    Ka, Pb, B = 0x1e4, bb, "4A2B1D"
                                end
                            elseif Ka < 0x1dc then
                                if Ka > 0x1d6 then
                                    Ka, Y = 0x2b0, Va._["Instance"]
                                    Ta, Y = Y["new"], "Folder"
                                else
                                    V(f, oa, Ra, ha)
                                    oa, V, Ka, f = "Success", Na[1][Na[2]]["setStatus"], 0x4b636 / Ka, "Ready"
                                end
                            elseif Ka > 0x1dc then
                                Ra, V, Ka, f, oa = 60, Na[1][Na[2]]["applyFpsCap"], 0x3bd, Na[1][Na[2]]["optionValue"], "FpsCap"
                            else
                                Na(Pb)
                                Ka, Pb = 0x42f - Ka, Va:ic{ua}
                            end
                        elseif Ka <= 0x1d2 then
                            if Ka <= 0x1d1 then
                                if Ka <= 463 then
                                    if Ka > 0x1cc then
                                        Ka = 0x16d56 / Ka
                                        ua(bb)
                                    else
                                        Ka, pa, M = 0x4c978 / Ka, Va._["typeof"], I["DisplayName"]
                                    end
                                else
                                    Ka = 416
                                    ca(Va.d(U))
                                    U = {}
                                    ca = U
                                    ca = {[2] = 3, [3] = ca}
                                    ca[1] = ca
                                    U = false
                                    U = {[2] = 3, [3] = U}
                                    U[1] = U
                                    va = {[2] = 3, [3] = va}
                                    va[1] = va
                                    va[1][va[2]] = Va:Pb{ca}
                                    mb = {[2] = 3, [3] = mb}
                                    mb[1] = mb
                                    mb[1][mb[2]] = Va:B{Na, fa, T, eb}
                                    ia = {[2] = 3, [3] = ia}
                                    ia[1] = ia
                                    V, ia[1][ia[2]] = Va:Ub{Na, jb, ob}, Va:Xb{Na, fa, s, ub, zb}
                                    Na[1][Na[2]]["stabilizeStealRoot"] = V
                                    f, V, Ra = wb[1][wb[2]]["Heartbeat"], Na[1][Na[2]]["track"], Va:J{va, Ma, Na, Da, A, ia, mb, db, eb, cb, Pa, jb, fa, Ab, gb, U, ub}
                                    oa, f = f, f.Connect
                                end
                            else
                                fb = fb(Ta, Y, u)
                                Ka, qa[1][qa[2]] = Ka + 0x1b1, fb
                            end
                        elseif Ka <= 0x1d3 then
                            Ka, M, pa = 435, I, Va._["typeof"]
                        else
                            Ka = 131
                            Aa(A, ca)
                        end
                    elseif Ka < 0x20e then
                        if Ka >= 0x1f5 then
                            if Ka > 0x1ff then
                                if Ka > 0x208 then
                                    Ka = 0x38d
                                    p()
                                    Aa, p = Va:mb{ob}, Va._["pcall"]
                                elseif Ka <= 0x202 then
                                    Ka = Ka + 57
                                    ca(Va.d(U))
                                    mb, ca, U = Va:Ia{gb}, Na[1][Na[2]]["track"], Ya[1][Ya[2]]["InputChanged"]
                                    U, va = U.Connect, U
                                else
                                    Ka, Mb = 0x156, Mb()
                                    Mb = {[2] = 3, [3] = Mb}
                                    Mb[1] = Mb
                                    La = la
                                    la = La["clock"]
                                end
                            elseif Ka >= 0x1fa then
                                if Ka <= 506 then
                                    Ya = Ya(pb, Ma)
                                    Ya = {[2] = 3, [3] = Ya}
                                    Ka, Ya[1] = Ka + 356, Ya
                                    pb, cb = Va._["game"], "Lighting"
                                    Ma, pb = pb, pb.GetService
                                else
                                    Ka, ib = 126, ib(O)
                                end
                            elseif Ka > 0x1f5 then
                                u, fb, Ta, Ka, Y = 6, ka[1][ka[2]].WaitForChild, ka[1][ka[2]], 0x1d2, "GuardAreas"
                            else
                                rb = rb(Wa, tb, K)
                                vb["CalculateFusePrice"] = rb
                                w = vb
                                Ka, w = Ka + -57, {[2] = 3, [3] = w}
                                w[1] = w
                                vb = Va:ob{Na}
                                Na[1][Na[2]]["remoteFrom"] = vb
                                rb, tb, K, X, Gb, da = {}, {}, Na[1][Na[2]]["remoteFrom"], "Haul", Ib, "WearBest"
                            end
                        elseif Ka <= 0x1f0 then
                            if Ka > 494 then
                                V(Va.d(f))
                                Ka, V, f = Ka + 500, Na[1][Na[2]]["isOn"], "AntiGameplayPause"
                            elseif Ka < 493 then
                                Pb = Pb(B)
                                Na["Sidebar"] = Pb
                                B, Ka, Pb = "2A1811", Ka + 0x18d, bb
                            elseif Ka > 0x1ed then
                                Oa = Oa(Bb)
                                Ka, q, Bb = 0x479 - Ka, Va:G{ya}, Va._["pcall"]
                            else
                                K = K(Gb, X, da)
                                Ka = K and 0x219 - Ka or 0xcd
                            end
                        elseif Ka > 497 then
                            Pb = Pb(B)
                            Ka, Na["Info"] = 0x1fbd0 / Ka, Pb
                            Pb, B = bb, "090403"
                        else
                            P = P(G, S, w)
                            J["RequestCompleteHatchEgg"] = P
                            P, G, Ka, S, w = Na[1][Na[2]]["pickFn"], ab, 0x130, "WearEggTool", "RequestEquipTool"
                        end
                    elseif Ka > 0x229 then
                        if Ka > 0x231 then
                            if Ka <= 0x235 then
                                Ka, ga = 0xdf, ga(ib)
                            else
                                Ka, U = Ka + 0x12b, Va.c(U(va, mb))
                            end
                        elseif Ka > 0x22d then
                            Ka, G = 0x39a - Ka, G(S, w, vb)
                            P["GetRespawnPointCFrame"] = G
                            G, S, vb, w = Na[1][Na[2]]["pickFn"], N, "GetPlotData", "ResolvePlot"
                        elseif Ka >= 0x22c then
                            if Ka > 0x22c then
                                qa = qa()
                                Ka, qa["MMBHubHopHistory"] = 0x3bc, ka
                            else
                                K = K(Gb, X, da)
                                Ka = K and Ka + -0x202 or 0xa7
                            end
                        else
                            h = h(Ib, kb, J, P, G)
                            Ka = h and 0x2030c / Ka or 155
                        end
                    elseif Ka <= 0x223 then
                        if Ka > 0x21e then
                            Ka, lb = 0x18f, Va._["table"]
                            lb, I, pa = r[1][r[2]], lb["insert"], x["name"]
                        elseif Ka >= 0x219 then
                            if Ka <= 0x219 then
                                gb = gb()
                                gb = {[2] = 3, [3] = gb}
                                Ka, gb[1] = 0x3be, gb
                                Da = Va._["tick"]
                            else
                                Ka, Y, Ta, fb, qa = 0x272, 8, "__OBJECTS", cb[1][cb[2]], cb[1][cb[2]].WaitForChild
                            end
                        else
                            Ka, V = Ka + 0xbf, Na[1][Na[2]]["enableFpsBoost"]
                        end
                    elseif Ka >= 0x227 then
                        if Ka <= 0x227 then
                            Y = Va:V{Na}
                            Na[1][Na[2]]["getUnplacedEggUids"] = Y
                            Y = Va:za{Na}
                            Na[1][Na[2]]["placingEnabled"] = Y
                            Y = Va:eb{_a}
                            Na[1][Na[2]]["isPlotFull"] = Y
                            Y = Va:ga{_a, Na}
                            Na[1][Na[2]]["markPlotFull"] = Y
                            Y = Va:va{J}
                            Na[1][Na[2]]["getPlacementLocalCFrames"] = Y
                            Y = Va:Ka{eb, Na}
                            Na[1][Na[2]]["canAutoPlace"] = Y
                            Y = Va:xc{kb, eb, jb, _a, Na, W}
                            Na[1][Na[2]]["runAutoPlaceEggs"] = Y
                            Y = Va:Kb{eb, Na}
                            Na[1][Na[2]]["canAutoHatch"] = Y
                            Y = Va:jc{jb, Na, kb}
                            Na[1][Na[2]]["runAutoOpenReadyEggs"] = Y
                            Y = Va:fc{S}
                            Na[1][Na[2]]["getPetItemData"] = Y
                            Y = Va:Ba{ob}
                            Na[1][Na[2]]["findToolByUid"] = Y
                            Y = Va:hb{Na, ob}
                            Na[1][Na[2]]["holdUid"] = Y
                            Y = Va:sc{vb, Na}
                            Na[1][Na[2]]["sellUid"] = Y
                            Y = Va:Qc{Na}
                            Na[1][Na[2]]["getSellablePets"] = Y
                            Y = Va:F{jb, Na, eb}
                            Na[1][Na[2]]["runAutoSellPets"] = Y
                            Y = Va:qb{Na}
                            Na[1][Na[2]]["getSellableEggUids"] = Y
                            Y = Va:U{jb, Na, kb, eb}
                            Na[1][Na[2]]["runAutoSellEggs"] = Y
                            Y = Va:vb{w, Na}
                            Na[1][Na[2]]["fuseGroups"] = Y
                            Y = Va:zb{X, Na}
                            Na[1][Na[2]]["pickFuseGroup"] = Y
                            Y = Va:gc{Na, w}
                            Na[1][Na[2]]["fusePrice"] = Y
                            Y = Va:X{cb}
                            Na[1][Na[2]]["getFuseMachinePosition"] = Y
                            Ka, Y = 0x6be2e / Ka, Va:ib{vb, Na, jb}
                            Na[1][Na[2]]["runAutoFusePets"] = Y
                            Y = Va:u{Ua, cb, vb, Na}
                            Na[1][Na[2]]["runAutoEquipBest"] = Y
                            Y = Va:aa{r, Na, R, ob, ta, vb}
                            Na[1][Na[2]]["runAutoEquipBestTrail"] = Y
                            Y = Va:xa()
                            Na[1][Na[2]]["gearBaseName"] = Y
                            Y = Va:ja{Na, ob, Cb}
                            Na[1][Na[2]]["runAutoEquipBestGear"] = Y
                            Y = Va:Rc{r, Na, R, vb, ta}
                            Na[1][Na[2]]["runAutoBuyTrail"] = Y
                            Y = Va:Mb{Fb, Na, j, vb}
                            Na[1][Na[2]]["runAutoUpgrades"] = Y
                            Y = Va:Cc{vb, Na}
                            Na[1][Na[2]]["runAutoClaimIndex"] = Y
                            Y = Va:ba{vb, Na}
                            Na[1][Na[2]]["runClaimOfflineEarnings"] = Y
                            Y = Va:Ca{B, Na, vb, ob}
                            Na[1][Na[2]]["runAutoClaimGroupReward"] = Y
                            Y = Va:ac{ob, cb}
                            Na[1][Na[2]]["deleteOwnPetRenders"] = Y
                            Y = Va:ab{J}
                            Na[1][Na[2]]["getTreadmillStand"] = Y
                            Y = Va:Q{ob}
                            Na[1][Na[2]]["isDoubleSpeedVisible"] = Y
                            Y = Va:bc{Na}
                            Na[1][Na[2]]["dismountTreadmill"] = Y
                            Y = Va:Oa{vb, ub, Na}
                            Na[1][Na[2]]["stopTreadmillTraining"] = Y
                            Y = Va:Qa{eb, Na}
                            Na[1][Na[2]]["canAutoTreadmill"] = Y
                            Y = Va:Ab{vb, Na, ub}
                            Na[1][Na[2]]["runAutoTreadmillTraining"] = Y
                            b, Ab, zb, Aa, p, u = "Pet Area", "Treadmill", "Base", "Lobby Entry", "Fuse Machine", {}
                            u[1], u[2], u[3], u[4], u[5] = zb, b, Ab, p, Aa
                            Y = u
                            Y = {[2] = 3, [3] = Y}
                            Y[1] = Y
                            zb, u = ra[1][ra[2]], Va._["ipairs"]
                        else
                            Ka, K = 0x2c, K(Gb)
                        end
                    else
                        Pb = Pb(B)
                        Ka, Na["SurfaceSecondary"] = 0x4127c / Ka, Pb
                        B, Pb = "3D2419", bb
                    end
                elseif Ka < 0x288 then
                    if Ka > 0x26b then
                        if Ka > 0x276 then
                            if Ka >= 0x27f then
                                if Ka >= 0x280 then
                                    if Ka <= 0x280 then
                                        Cb = r(ta, R)
                                        R = Cb
                                        Ka = R == nil and 0x321 - Ka or Ka + -455
                                    else
                                        Ka, u = 0x34c22 / Ka, Va.c(u(zb, b))
                                    end
                                else
                                    Ka, rb = 0x2e7 - Ka, rb(Wa)
                                end
                            elseif Ka <= 0x279 then
                                Ka, Cb[1][Cb[2]][lb] = 0x288, pa
                            else
                                qa = qa(fb)
                                fb = "table"
                                Ka = qa ~= fb and 0x3ba or 0x3bc
                            end
                        elseif Ka <= 0x271 then
                            if Ka > 0x26f then
                                ua = ua(bb, E)
                                Ka, ua = Ka + 0xe0, {[2] = 3, [3] = ua}
                                ua[1] = ua
                                E = Va._["Color3"]
                                Pb, Na, bb = "Dark", {}, E["fromHex"]
                                Na["Appearance"] = Pb
                                Pb, B = bb, "120B08"
                            elseif Ka >= 0x26e then
                                if Ka > 0x26e then
                                    Ka, K = 143, K(Gb)
                                else
                                    Ka, K = 0x286 - Ka, K(Gb)
                                end
                            else
                                d = d(h, Ib, kb, J, P)
                                Ka = d and 0x2f7 - Ka or Ka + -0x209
                            end
                        elseif Ka <= 0x273 then
                            if Ka <= 0x272 then
                                qa = qa(fb, Ta, Y)
                                fb = qa
                                Ka = fb and Ka + -0xe1 or 0x3ca
                            else
                                zb, Ka, u, Y, Ta = 10, 0x3cf, "AreaEggSlotsClient", cb[1][cb[2]], cb[1][cb[2]].WaitForChild
                            end
                        else
                            Ka, rb = Ka + -0x81, rb(Wa, tb, K)
                            vb["CanSelectPet"] = rb
                            tb, Wa, rb, K = "PriceFor", h, Na[1][Na[2]]["pickFn"], "CalculateFusePrice"
                        end
                    elseif Ka >= 0x256 then
                        if Ka <= 0x260 then
                            if Ka < 0x25a then
                                if Ka <= 0x256 then
                                    V, Ka, f = Na[1][Na[2]]["applyAntiGameplayPause"], 0x298, true
                                else
                                    P = P(G, S, w)
                                    J["RequestAreaEggSnapshot"] = P
                                    P = ab
                                    Ka = P and 0x41 or 0x20
                                end
                            elseif Ka > 0x25a then
                                Ka, K = 0x34a - Ka, K(Gb)
                            else
                                xb = xb(Pa, Q)
                                xb = {[2] = 3, [3] = xb}
                                xb[1] = xb
                                Pa, Xa = Va._["game"], "CoreGui"
                                Q, Ka, Pa = Pa, 372, Pa.GetService
                            end
                        elseif Ka >= 0x267 then
                            if Ka > 0x267 then
                                Pb = Pb(B)
                                Ka, Na["Border"] = 0x4536e / Ka, Pb
                                B, Pb = "87513A", bb
                            else
                                Ka = 0x307
                                _(jb, aa)
                                _, jb = Va._["ipairs"], Cb
                            end
                        else
                            Pb = Pb(B)
                            Na["ControlInset"] = Pb
                            Ka, Pb, B = 0x60f - Ka, bb, "301A12"
                        end
                    elseif Ka >= 0x24a then
                        if Ka >= 0x24c then
                            if Ka <= 0x24c then
                                Ka, D = 0x219, D()
                                D = {[2] = 3, [3] = D}
                                D[1] = D
                                Ia = nil
                                Ia = {[2] = 3, [3] = Ia}
                                Ia[1] = Ia
                                Ua = 0
                                Ua = {[2] = 3, [3] = Ua}
                                Ua[1] = Ua
                                W = 1
                                W = {[2] = 3, [3] = W}
                                W[1] = W
                                _a = 0
                                _a = {[2] = 3, [3] = _a}
                                _a[1] = _a
                                gb = Va._["tick"]
                            else
                                Na(Pb)
                                Pb = {}
                                Na = Pb
                                Na = {[2] = 3, [3] = Na}
                                Na[1] = Na
                                Pb = Va:cc()
                                Na[1][Na[2]]["cloneList"] = Pb
                                Pb = Va:pc()
                                Na[1][Na[2]]["clearTable"] = Pb
                                Pb = Va:ma()
                                Na[1][Na[2]]["waitFor"] = Pb
                                Pb = Va:ya{ua}
                                Na[1][Na[2]]["notify"] = Pb
                                Pb = Va:Hc{ua}
                                Na[1][Na[2]]["getState"] = Pb
                                Pb = Va:yc{Na}
                                Na[1][Na[2]]["isOn"] = Pb
                                Pb = Va:dc{Na}
                                Na[1][Na[2]]["optionValue"] = Pb
                                Pb = Va:K{Na}
                                Na[1][Na[2]]["multiSelected"] = Pb
                                Pb = Va:Yb{Na}
                                Na[1][Na[2]]["multiHasAny"] = Pb
                                Pb = Va:zc{Na}
                                Ka, Na[1][Na[2]]["selectionAllows"] = 0x109, Pb
                                Pb = Va:g()
                                Na[1][Na[2]]["requirePath"] = Pb
                                Pb = Va:ua{l}
                                Na[1][Na[2]]["findModule"] = Pb
                                Pb = Va:oa{l}
                                Na[1][Na[2]]["findRemote"] = Pb
                                Pb = Va:D{l}
                                Na[1][Na[2]]["findRemoteContains"] = Pb
                                Pb = Va:v()
                                Na[1][Na[2]]["pickFromTable"] = Pb
                                Pb, ga, Fb, _b, B = Na[1][Na[2]]["requirePath"], "Save", 6, "Shared", l[1][l[2]]
                            end
                        else
                            Ka, T = 0x28e, Va._["string"]
                            T, Ba, Ea, eb = nb[1][nb[2]], 1, 18, T["sub"]
                        end
                    elseif Ka > 0x246 then
                        B = B(Fb, _b, ga, ib, O)
                        Ka = B and 0x14 or 0xf4
                    elseif Ka > 0x23c then
                        Ka, jb, aa = 0x335 - Ka, Va._["typeof"], _
                    else
                        Pb = Pb(B)
                        Na["Text"] = Pb
                        B, Ka, Pb = "D7B6A5", 0x81508 / Ka, bb
                    end
                elseif Ka <= 0x2a1 then
                    if Ka > 0x293 then
                        if Ka < 0x299 then
                            if Ka > 0x297 then
                                Ka = 0x587 - Ka
                                V(f)
                            elseif Ka <= 0x294 then
                                Ka, Ib = 0, Ib(kb)
                            else
                                O = O(Sa, j, ab, N)
                                Ka = O and 75 or 0x3a
                            end
                        elseif Ka > 0x29e then
                            Ka = 0x3a9
                            I(lb, pa)
                        elseif Ka > 0x299 then
                            Ka = 0x68b00 / Ka
                            jb(aa, na)
                        else
                            Ma = Ma(cb, l)
                            Ma = {[2] = 3, [3] = Ma}
                            Ka, Ma[1] = 0x3b2, Ma
                            cb, xb = Va._["game"], "Workspace"
                            cb, l = cb.GetService, cb
                        end
                    elseif Ka <= 0x28f then
                        if Ka <= 0x28c then
                            if Ka >= 0x28b then
                                if Ka <= 0x28b then
                                    Bb = Bb(q)
                                    Ka, o, q = Ka + 0xe9, Va:Ra(), Va._["pcall"]
                                else
                                    Ka, P = 0x17a, P(G, S, w)
                                    J["IsLocalEggReady"] = P
                                    G, P, w, S = ab, Na[1][Na[2]]["pickFn"], "RequestHatchEgg", "BeginHatch"
                                end
                            else
                                x, I = jb(aa, na)
                                na = x
                                Ka = na == nil and 0x3c1 - Ka or 0x49e18 / Ka
                            end
                        elseif Ka <= 0x28e then
                            eb = eb(T, Ba, Ea)
                            Ka, T = Ka + 0xfd, "..."
                            nb[1][nb[2]] = eb .. T
                        else
                            pa = pa(M)
                            Ka = pa and 0x508 - Ka or 0x134
                        end
                    elseif Ka <= 0x292 then
                        if Ka > 0x291 then
                            K = K(Gb, X, da)
                            Ka = K and 0x4d1c / Ka or 0xa3
                        else
                            V(f, oa)
                            return
                        end
                    else
                        Ka = Y and 0x2c6 or 0x58a65 / Ka
                    end
                elseif Ka < 0x2b9 then
                    if Ka >= 0x2b0 then
                        if Ka > 0x2b3 then
                            K = K(Gb, X, da)
                            Ka = K and Ka + -0x21c or 0x1e744 / Ka
                        elseif Ka <= 0x2b0 then
                            Ta = Ta(Y)
                            Ta = {[2] = 3, [3] = Ta}
                            Ta[1] = Ta
--===== [ESP] Egg ESP overlay =====
                            Y = "MMBEggEsp"
                            Ta[1][Ta[2]]["Name"] = Y
                            Ta[1][Ta[2]]["Parent"] = cb[1][cb[2]]
                            Y = Va:Qb{aa}
                            Na[1][Na[2]]["track"] = Y
                            Y = Va:Ac{na}
                            Na[1][Na[2]]["setStatus"] = Y
                            Y = Va:L{I}
                            Na[1][Na[2]]["setJob"] = Y
                            Y = Va:Ic{Ea, x}
                            Na[1][Na[2]]["setStolen"] = Y
                            Y = Va:rb{Na}
                            Na[1][Na[2]]["copyText"] = Y
                            Y = Va:ha{ob}
                            Na[1][Na[2]]["getHumanoid"] = Y
                            Y = Va:M{ob}
                            Na[1][Na[2]]["getRoot"] = Y
                            Y = Va:E{Pb}
                            Na[1][Na[2]]["getSave"] = Y
                            Y = Va:j{Na}
                            Na[1][Na[2]]["netInvoke"] = Y
                            Y = Va:kb{Na}
                            Na[1][Na[2]]["netCall"] = Y
                            Y = Va:vc()
                            Na[1][Na[2]]["countTable"] = Y
                            Y = Va:ia()
                            Na[1][Na[2]]["formatNumber"] = Y
                            Y = Va:_a()
                            Na[1][Na[2]]["formatElapsed"] = Y
                            Y = Va:Ib{ib}
                            Na[1][Na[2]]["resolveRarity"] = Y
                            Y = Va:o{ib}
                            Na[1][Na[2]]["assetName"] = Y
                            Y = Va:pa()
                            Na[1][Na[2]]["recordMutations"] = Y
                            Y = Va:O{Na}
                            Na[1][Na[2]]["matchesMutationFilter"] = Y
                            Y = Va:Oc{Na}
                            Na[1][Na[2]]["matchesEggFilters"] = Y
                            Y = Va:Va{ka}
                            Na[1][Na[2]]["getLaneZ"] = Y
                            Y = Va:Wa{Na, ka}
                            Na[1][Na[2]]["getLaneY"] = Y
                            Y = Va:Sb{Na, ka}
                            Na[1][Na[2]]["getEntryPosition"] = Y
                            Y = Va:rc{qa}
                            Na[1][Na[2]]["getZoneModel"] = Y
                            Y = Va:Na{Na}
                            Na[1][Na[2]]["getZoneLaneCenter"] = Y
                            Y = Va:wa{Na, ra}
                            Na[1][Na[2]]["getCorridorBounds"] = Y
                            Y = Va:A{Na}
                            Na[1][Na[2]]["clampToCorridor"] = Y
                            Y = Va:k()
                            Na[1][Na[2]]["stripCheatMovers"] = Y
                            Y = Va:i()
                            Na[1][Na[2]]["stopSoftMove"] = Y
                            Y = Va:Wb{ob, Na}
                            Na[1][Na[2]]["placeRoot"] = Y
                            Y = Va:ea{Na, jb, Q, _}
                            Na[1][Na[2]]["glideTo"] = Y
                            Y = Va:R{Na}
                            Na[1][Na[2]]["rawTeleport"] = Y
                            Y = Va:qa{Na}
                            Na[1][Na[2]]["travelTo"] = Y
                            Y = Va:Fc{ob, Na, cb}
                            Na[1][Na[2]]["groundedY"] = Y
                            Y = Va:Sa{Na}
                            Na[1][Na[2]]["anchorStealRoot"] = Y
                            Y = Va:Lc()
                            Na[1][Na[2]]["stealSpeed"] = Y
                            Y = Va:ub{ob}
                            Na[1][Na[2]]["swapStealHumanoid"] = Y
                            Y = Va:wb{cb, ob, Na}
                            Na[1][Na[2]]["prepareStealHumanoid"] = Y
                            Y = Va:_c{ob, jb, _, wb, Na}
                            Na[1][Na[2]]["humanoidStealMoveTo"] = Y
                            Y = Va:T{ob, Na}
                            Na[1][Na[2]]["specialEggTeleport"] = Y
                            Y = Va:ra{Na}
                            Na[1][Na[2]]["stealMoveTo"] = Y
                            Y = Va:Ya{Na}
                            Na[1][Na[2]]["buildStealPath"] = Y
                            Y = Va:nb{Na}
                            Na[1][Na[2]]["stealAlong"] = Y
                            Y = Va:Pc{J}
                            Na[1][Na[2]]["getBasePosition"] = Y
                            Y = Va:gb{Na, J}
                            Na[1][Na[2]]["getPetAreaStandPosition"] = Y
                            Y = Va:y{J, Na}
                            Na[1][Na[2]]["isNearPlot"] = Y
                            Y = Va:Dc{Na}
                            Na[1][Na[2]]["ensureAtPlot"] = Y
                            Y = Va:Bc{cb, fb}
                            Na[1][Na[2]]["findEggInstanceByUid"] = Y
                            Y = Va:t{Na, eb, kb, jb, Ba, _}
                            Na[1][Na[2]]["dropThenPickupFast"] = Y
                            Y = Va:sa{Na}
                            Na[1][Na[2]]["returnToBase"] = Y
                            Y = Va:Ta{kb}
                            Na[1][Na[2]]["getAreaEggs"] = Y
                            Y = Va:l{Na}
                            Na[1][Na[2]]["findAreaEggRecord"] = Y
                            Y = Va:Fb()
                            Na[1][Na[2]]["getSlotEggPosition"] = Y
                            Y = Va:H{Na}
                            Na[1][Na[2]]["isBigEgg"] = Y
                            Y = Va:yb{Na, X}
                            Na[1][Na[2]]["eggScore"] = Y
                            Y = Va:w{Na}
                            Na[1][Na[2]]["isStealCandidate"] = Y
                            Y = Va:bb{Na, fb}
                            Na[1][Na[2]]["pickStealTarget"] = Y
                            Y = Va:Rb{Na}
                            Na[1][Na[2]]["stealingEnabled"] = Y
                            Y = Va:m{Na}
                            Na[1][Na[2]]["eggInventoryCount"] = Y
                            Y = Va:ta{Na, _b}
                            Na[1][Na[2]]["eggInventoryFull"] = Y
                            Y = Va:uc{eb, Na}
                            Na[1][Na[2]]["canAutoSteal"] = Y
                            Y = Va:kc{P, kb, eb, Na}
                            Na[1][Na[2]]["tryCarryEgg"] = Y
                            Y = Va:xb{T, Na, jb}
                            Na[1][Na[2]]["prepareForestEggBeforeSteal"] = Y
                            Y = Va:lc{T, Na, eb, Ba, _, jb}
                            Na[1][Na[2]]["stealEgg"] = Y
                            Y = Va:Hb{Na, eb}
--===== [AutoSteal] Steal-engine method bindings =====
                            Na[1][Na[2]]["runAutoSteal"] = Y
                            Y = Va:ca{kb, eb}
                            Na[1][Na[2]]["runAutoDropEgg"] = Y
                            Y = Va:ec{Na, eb, J}
                            Na[1][Na[2]]["runAutoReturn"] = Y
                            Y = kb[1][kb[2]]["AreaEggCarryStateChanged"]
                            Ka = Y and 0x2c7 or Ka + -0x1d
                        else
                            K = K(Gb, X, da)
                            Ka = K and 0x342 - Ka or 0xc8
                        end
                    elseif Ka >= 0x2a9 then
                        if Ka > 0x2a9 then
                            Ka, pa = 0x332, pa(M)
                            M = "string"
                            lb = pa == M
                        else
                            u(Va.d(zb))
                            u = Va:Ma{hb}
                            Na[1][Na[2]]["fetchServerPage"] = u
                            u = Va:Cb{ja, Na}
                            Na[1][Na[2]]["pickHopTargets"] = u
                            u = Va:p{a, Ia, Na, jb, ob}
                            Na[1][Na[2]]["tryTeleportTo"] = u
                            u = Va:q{Nb, xa, jb, Na}
                            Na[1][Na[2]]["serverHop"] = u
                            u = Va:Xa{xa, eb, L, Ea, i, D, Na}
                            Na[1][Na[2]]["runServerHop"] = u
                            u = Va:Ga{a, ob}
                            Na[1][Na[2]]["rejoinServer"] = u
                            u = Va:wc{Na}
                            Na[1][Na[2]]["webhookPing"] = u
                            u = Va:mc{hb, Na}
                            Na[1][Na[2]]["httpPost"] = u
                            u = Va:Mc{Na}
                            Na[1][Na[2]]["sendWebhookEmbed"] = u
                            u = Va:da()
                            Na[1][Na[2]]["embedField"] = u
                            Jb[1][Jb[2]], u = Va:Pa{sb, Na}, Va:pb{g, Ha, La, F, Fa, Ja, ea, Qa, X, Ea, Ca, Na}
                            Na[1][Na[2]]["trackWebhookEvents"] = u
                            u = Va:Tb{Fa, Na, Qa, nb, Mb, ob, Ca}
                            Na[1][Na[2]]["buildSummaryEmbed"] = u
                            u = Va:Jc{Fa, Na, Qa, sb, Ca, Ha}
                            Na[1][Na[2]]["sendSummary"] = u
                            u = Va:oc{la, Na}
                            Na[1][Na[2]]["runWebhookSummary"] = u
                            u = Va:lb{Pa, xb, ob}
                            Na[1][Na[2]]["applyAntiGameplayPause"] = u
                            u = Va:Lb{Na, e, m}
                            Na[1][Na[2]]["destroyRenderOverlay"] = u
                            u = Va:Gc{Pa, e}
                            Na[1][Na[2]]["buildRenderOverlay"] = u
                            u = Va:Db{H, wb, Na}
                            Na[1][Na[2]]["applyRendering"] = u
                            Ka, zb, b = Ka + 328, {}, true
                            zb["ParticleEmitter"] = b
                            zb["Trail"] = b
                            zb["Smoke"] = b
                            zb["Fire"] = b
                            zb["Sparkles"] = b
                            u = zb
                            u = {[2] = 3, [3] = u}
                            u[1] = u
                            zb = Va:Ha()
                            Na[1][Na[2]]["setEffectEnabled"] = zb
                            zb = Va:Ob{cb, wa, u, qb, pb, Na}
                            Na[1][Na[2]]["enableFpsBoost"] = zb
                            zb = Va:Gb{wa, qb, Na, pb}
                            Na[1][Na[2]]["disableFpsBoost"] = zb
                            zb = Va:fb{Na, ma}
                            Na[1][Na[2]]["applyFpsCap"] = zb
                            zb = Va:ka{Na, k, ob}
                            Na[1][Na[2]]["handleDisconnect"] = zb
                            Aa, p, b = Na[1][Na[2]]["canAutoSteal"], {}, {}
                            p["Ready"] = Aa
                            Aa = Na[1][Na[2]]["runAutoSteal"]
                            p["Run"] = Aa
                            Aa = 0.25
                            p["Interval"] = Aa
                            Ab = p
                            b["Auto Steal Egg"] = Ab
                            Aa, p = Na[1][Na[2]]["canAutoPlace"], {}
                            p["Ready"] = Aa
                            Aa = Na[1][Na[2]]["runAutoPlaceEggs"]
                            p["Run"] = Aa
                            Aa = 0.45
                            p["Interval"] = Aa
                            Ab = p
                            b["Auto Place Egg"] = Ab
                            Aa, p = Na[1][Na[2]]["canAutoHatch"], {}
                            p["Ready"] = Aa
                            Aa = Na[1][Na[2]]["runAutoOpenReadyEggs"]
                            p["Run"] = Aa
                            Aa = 0.55
                            p["Interval"] = Aa
                            Ab = p
                            b["Auto Hatch"] = Ab
                            Aa, p = Na[1][Na[2]]["canAutoTreadmill"], {}
                            p["Ready"] = Aa
                            Aa = Na[1][Na[2]]["runAutoTreadmillTraining"]
                            p["Run"] = Aa
                            Aa = 1.2
                            p["Interval"] = Aa
                            Ab = p
                            b["Auto Treadmill"] = Ab
                            zb = b
                            zb = {[2] = 3, [3] = zb}
                            zb[1] = zb
                            b = Va:Nb{Na, z, c, zb}
                            Na[1][Na[2]]["priorityOrder"] = b
                            b = Va:db{Ta, Nb, x, r, yb, lb, I, n, Ob, Eb, Gb, ua, t, da, L, Y, za, pa, ya, y, Hb, _b, c, jb, z, nb, M, aa, ba, Na, na}
                            Ab = b
                        end
                    else
                        V = V(f)
                        Ka = V and 0x568dc / Ka or 0x482 - Ka
                    end
                elseif Ka <= 0x2bd then
                    if Ka <= 0x2bb then
                        if Ka <= 0x2ba then
                            if Ka <= 0x2b9 then
                                Ka, K = 0x1881 / Ka, K(Gb)
                            else
                                Db = Db(wb)
                                wb = "function"
                                Ka = Db ~= wb and Ka + -0x225 or 0x10306 / Ka
                            end
                        else
                            Db = Db(wb)
                            wb = "function"
                            Ka = Db ~= wb and 0xbf or 2
                        end
                    else
                        K = K(Gb, X, da)
                        Ka = K and Ka + -0x26a or 0x2f
                    end
                elseif Ka > 0x2bf then
                    Ka, r = 0x3b8 - Ka, r(ta)
                    Eb[1][Eb[2]] = r
                else
                    Ka, Pb = 0x12f, Pb(B)
                    Na["Control"] = Pb
                    Pb, B = bb, "43271B"
                end
            elseif Ka < 0x353 then
                if Ka <= 0x313 then
                    if Ka < 0x2ed then
                        if Ka < 0x2d4 then
                            if Ka <= 0x2cd then
                                if Ka <= 0x2ca then
                                    if Ka >= 0x2c7 then
                                        if Ka <= 0x2c7 then
                                            zb, u = kb[1][kb[2]]["AreaEggCarryStateChanged"], Va._["typeof"]
                                            Ka, zb = 0x96, zb["Connect"]
                                        else
                                            K = K(Gb, X, da)
                                            Ka = K and 182 or 0x398 - Ka
                                        end
                                    else
                                        b, u, Y = Va:W{eb, Ba, Na, Jb, Ea}, kb[1][kb[2]]["AreaEggCarryStateChanged"], Na[1][Na[2]]["track"]
                                        zb, Ka, u = u, 0x7026a / Ka, u.Connect
                                    end
                                else
                                    Ka = Ka + -0xed
                                    V()
                                end
                            elseif Ka <= 0x2ce then
                                Ka, fb = 0x3ca, fb(Ta, Y, u)
                            else
                                w = w(vb, rb, Wa)
                                S["GetRuntimeSnapshot"] = w
                                Ka, G = 0x17b, S
                                G = {[2] = 3, [3] = G}
                                G[1] = G
                                tb, rb, w, vb, Wa = "Deserialize", d, {}, Na[1][Na[2]]["pickFn"], "Decode"
                            end
                        elseif Ka >= 0x2e1 then
                            if Ka >= 0x2e8 then
                                if Ka <= 0x2e8 then
                                    Db(wb)
                                    Ka, wb = 0x3b4, Va._["task"]
                                    Db, wb = wb["wait"], 0.1
                                else
                                    hb = hb(a, Ya)
                                    Ka, hb = Ka + 0x29, {[2] = 3, [3] = hb}
                                    hb[1] = hb
                                    a, pb = Va._["game"], "TeleportService"
                                    Ya, a = a, a.GetService
                                end
                            elseif Ka > 0x2e1 then
                                Pb = Pb(B)
                                Na["AccentHover"] = Pb
                                Ka, Pb, B = 0x199, bb, "D95520"
                            else
                                Db = Db(wb)
                                wb = "function"
                                Ka = Db == wb and 0x32b - Ka or Ka + -0x25b
                            end
                        elseif Ka > 0x2d5 then
                            Ka, O = 0x329 - Ka, O(Sa)
                        elseif Ka <= 0x2d4 then
                            jb, Ka, aa = Va._["pairs"], 0x2d5, _
                        else
                            jb, aa, na = jb(aa)
                            jb, aa, na = Va.b(jb, aa, na)
                            x, I = jb(aa, na)
                            na = x
                            Ka = na == nil and 0x139 or 0x4a8 - Ka
                        end
                    elseif Ka < 0x307 then
                        if Ka < 0x2fa then
                            if Ka >= 0x2ef then
                                if Ka <= 0x2ef then
                                    V, Ka, f = Na[1][Na[2]]["isOn"], Ka + -0x4d, "FpsBoost"
                                else
                                    Ka, U = Ka + -0x120, Va.c(U(va, mb))
                                end
                            else
                                K = K(Gb, X, da)
                                Ka = K and 0x2aca2 / Ka or 54
                            end
                        elseif Ka >= 0x304 then
                            if Ka <= 0x304 then
                                Fb = Fb(_b, ga, ib, O)
                                Ka = Fb and 0xf5 or 0x364 - Ka
                            else
                                Ka = 0x2d7b5 / Ka
                                v(Oa)
                                Oa, q, o, Bb = {}, ya[1][ya[2]], "gethui", Va._["rawget"]
                            end
                        elseif Ka <= 0x2fa then
                            fb, ka = "Areas", cb[1][cb[2]]["__OBJECTS"]
                            Ka, qa, ka = 0x320, ka, ka.FindFirstChild
                        else
                            Ka, U = Ka + -0xfb, Va.c(U(va, mb))
                        end
                    elseif Ka < 0x30e then
                        if Ka < 0x309 then
                            _, jb, aa = _(jb)
                            _, jb, aa = Va.b(_, jb, aa)
                            na, x = _(jb, aa)
                            aa = na
                            Ka = aa == nil and Ka + -321 or 0x223
                        elseif Ka > 0x309 then
                            Q = Q(Xa, ob)
                            Q = {[2] = 3, [3] = Q}
                            Q[1] = Q
                            v, Ka, Xa = "PathfindingService", 0x61e - Ka, Va._["game"]
                            ob, Xa = Xa, Xa.GetService
                        else
                            _ = O["Directory"]
                            Ka = _ and 0x6e676 / Ka or 198
                        end
                    elseif Ka < 0x312 then
                        if Ka <= 0x30e then
                            Pb = Pb(B)
                            Na["Background"] = Pb
                            Pb, Ka, B = bb, 0x4fa - Ka, "21130E"
                        else
                            Ka = 0xd0
                            ua(bb)
                        end
                    elseif Ka > 0x312 then
                        Xa = Xa(ob, v)
                        ob = Db[1][Db[2]]["LocalPlayer"]
                        Ka = ob and 0x6c or 90
                    else
                        a = a(Ya, pb)
                        Ka, a = 506, {[2] = 3, [3] = a}
                        a[1] = a
                        Ya, Ma = Va._["game"], "UserInputService"
                        Ya, pb = Ya.GetService, Ya
                    end
                elseif Ka < 0x32f then
                    if Ka > 0x322 then
                        if Ka >= 0x328 then
                            if Ka <= 0x329 then
                                if Ka > 0x328 then
                                    Db(wb)
                                    Db, hb = Va._["game"], "Players"
                                    wb, Ka, Db = Db, 0x47c - Ka, Db.GetService
                                else
                                    Ka = 218
                                    Db(wb)
                                end
                            else
                                Ib = Ib(kb, J, P, G)
                                Ka = Ib and 0 / Ka or 84
                            end
                        elseif Ka > 0x325 then
                            Ka, Sa = 93, Sa(j)
                        else
                            Ka, U = 0x1bb, Va.c(U(va, mb))
                        end
                    elseif Ka <= 0x31b then
                        if Ka <= 0x316 then
                            if Ka > 0x315 then
                                Ka, zb = 0x83586 / Ka, Va.c(zb(b, Ab))
                            elseif Ka <= 0x314 then
                                Ka, K = 70, K(Gb)
                            else
                                Ka = 0x2f1
                                ca(Va.d(U))
                                U, ca, mb = Ya[1][Ya[2]]["InputBegan"], Na[1][Na[2]]["track"], Va:tb{Na}
                                va, U = U, U.Connect
                            end
                        else
                            Ka, Pb = 0x28f41 / Ka, Pb(B)
                        end
                    elseif Ka >= 0x320 then
                        if Ka > 0x320 then
                            u, zb, b = u(zb)
                            u, zb, b = Va.b(u, zb, b)
                            Ab, p = u(zb, b)
                            b = Ab
                            Ka = b == nil and 0x3de or 0x482 - Ka
                        else
                            Ka, ka = Ka + 0xa3, ka(qa, fb)
                        end
                    else
                        Ka, pa, M, lb = Ka + -142, Va._["tonumber"], I["MoneyCost"], I["DisplayName"]
                    end
                elseif Ka <= 0x33c then
                    if Ka > 0x332 then
                        if Ka < 0x33b then
                            Ka, E = 0x3d7 - Ka, E(Na)
                            bb = bb .. E
                        elseif Ka > 0x33b then
                            Ka, U = 0x4a97c / Ka, Va.c(U(va, mb))
                        else
                            rb = rb(Wa)
                            Ka = rb and 0x68 or Ka + -0x240
                        end
                    elseif Ka > 0x331 then
                        Ka = lb and 0x31d or 0x288
                    elseif Ka <= 0x330 then
                        if Ka > 0x32f then
                            na, x = _(jb, aa)
                            aa = na
                            Ka = aa == nil and 0x4f6 - Ka or 0x223
                        else
                            qa = {[2] = 3, [3] = qa}
                            qa[1] = qa
                            fb = ka[1][ka[2]]
                            Ka = fb and Ka + 0xb9 or 0x188
                        end
                    else
                        wb = wb(hb, a)
                        wb = {[2] = 3, [3] = wb}
                        wb[1] = wb
                        Ka, Ya, hb = 0x2e9, "HttpService", Va._["game"]
                        hb, a = hb.GetService, hb
                    end
                elseif Ka > 0x349 then
                    if Ka <= 0x34c then
                        Pb = Pb(B)
                        Na["SurfaceRaised"] = Pb
                        Ka, B, Pb = 0x3d3, "160C09", bb
                    else
                        Pb = Pb(B)
                        Ka, Na["Canvas"] = 0x30e, Pb
                        B, Pb = "1A100C", bb
                    end
                elseif Ka > 0x346 then
                    tb = tb(K)
                    Ka = tb and 0x3cb - Ka or 0x2c24f / Ka
                elseif Ka > 0x342 then
                    Ka, h = Ka + -0x258, h(Ib)
                elseif Ka <= 0x33d then
                    _, jb, aa = _(jb)
                    _, jb, aa = Va.b(_, jb, aa)
                    na, x = _(jb, aa)
                    aa = na
                    Ka = aa == nil and 129 or 0x107
                else
                    Ka, K = 0x250ec / Ka, K(Gb)
                end
            elseif Ka > 0x3ba then
                if Ka > 0x3dc then
                    if Ka < 0x3f4 then
                        if Ka > 0x3e7 then
                            if Ka > 0x3e8 then
                                Ab()
                                Ka, Ab = 0x20d, {[2] = 3, [3] = Ab}
                                Ab[1] = Ab
                                Ab[1][Ab[2]] = Va:hc{eb, _b, Na, t, pa, M, Hb, lb, Ob, Mb, y, jb}
                                p = Ab[1][Ab[2]]
                            else
                                Ka, fb = 392, not qa[1][qa[2]]
                            end
                        elseif Ka < 0x3e4 then
                            if Ka > 0x3dd then
                                u = Va:I{Na}
                                Na[1][Na[2]]["resolveWaypoint"] = u
                                u = Va:Bb{Na}
                                Na[1][Na[2]]["espDistanceLimit"] = u
                                u = Va:La{Na}
                                Na[1][Na[2]]["withinEspRange"] = u
                                u = Va:Ec{X}
                                Na[1][Na[2]]["espColorFor"] = u
                                u = Va:Aa{Ta, db}
                                Na[1][Na[2]]["ensureEspEntry"] = u
                                u = Va:h{Ta, Na, C}
                                Na[1][Na[2]]["drawEspAt"] = u
                                u = Va:Nc{db}
                                Na[1][Na[2]]["releaseEsp"] = u
                                u = Va:cb{Na, db}
                                Na[1][Na[2]]["clearAllEsp"] = u
                                u = Va:Da{Na}
                                Na[1][Na[2]]["collectEggEsp"] = u
                                u = Va:Ea{qa, Na}
                                Na[1][Na[2]]["collectGuardEsp"] = u
                                u = Va:N{cb, Na, G}
                                Na[1][Na[2]]["collectPetEsp"] = u
                                u = Va:Eb{Db, Na, ob}
                                Na[1][Na[2]]["collectPlayerEsp"] = u
                                u = Va:Fa{cb, Na}
                                Na[1][Na[2]]["collectMachineEsp"] = u
                                u = Va:jb{cb, Na, Db, ob, J}
                                Na[1][Na[2]]["collectPlotEsp"] = u
                                u = Va:n{C, Na, db}
                                Na[1][Na[2]]["runEsp"] = u
                                Ka, u = 0x73f - Ka, Va:z{ja, Na}
                                Na[1][Na[2]]["rememberVisited"] = u
                                b, zb, u = Va._["game"], Va._["tostring"], Na[1][Na[2]]["rememberVisited"]
                                b = b["JobId"]
                            else
                                Ka = 0x1d6
                                V(Va.d(f))
                                ha, oa, Ra, f, V = 4, "Ready", "Success", "MMB HUB", Na[1][Na[2]]["notify"]
                            end
                        elseif Ka <= 0x3e4 then
                            V = V(f)
                            Ka = V and 0x256 or 0x6d3 - Ka
                        else
                            N = N(Lb, sa, d, h)
                            Ka = N and 11 or 0x41b - Ka
                        end
                    elseif Ka >= 0x3fc then
                        if Ka >= 0x3fd then
                            if Ka <= 0x3fd then
                                Ka, sa = 0x156fe / Ka, sa(d)
                            else
                                Ka, K = 23, K(Gb)
                            end
                        else
                            sa = sa(d, h, Ib, kb)
                            Ka = sa and 0x156a8 / Ka or 166
                        end
                    elseif Ka <= 0x3f5 then
                        if Ka <= 0x3f4 then
                            Ka, K = 0x1481c / Ka, K(Gb)
                        else
                            P = P(G, S, w)
                            J["RequestPlaceEgg"] = P
                            Ka, kb = Ka + -452, J
                            kb = {[2] = 3, [3] = kb}
                            kb[1] = kb
                            vb, P, w, S, G = "GetRespawnPointCFrame", {}, "FindRespawnCFrame", N, Na[1][Na[2]]["pickFn"]
                        end
                    else
                        ab = ab(N, Lb, sa, d)
                        Ka = ab and 0x2a404 / Ka or 0x13
                    end
                elseif Ka < 0x3cf then
                    if Ka < 0x3be then
                        if Ka > 0x3bc then
                            Ka, f = 0x3dd, Va.c(f(oa, Ra))
                        elseif Ka > 0x3bb then
                            Ka, ja[1][ja[2]] = Ka + -0x2a2, ka
                        else
                            Pb = Pb(B)
                            Ka, Na["Accent"] = 0xad002 / Ka, Pb
                            B, Pb = "FF7A38", bb
                        end
                    elseif Ka > 0x3ca then
                        l = l(xb, Pa)
                        Ka, l = 0x25a, {[2] = 3, [3] = l}
                        l[1] = l
                        Q, xb = "GuiService", Va._["game"]
                        xb, Pa = xb.GetService, xb
                    elseif Ka >= 0x3c3 then
                        if Ka > 0x3c3 then
                            Ka, ka[1][ka[2]] = 0x737 - Ka, fb
                        else
                            ka = {[2] = 3, [3] = ka}
                            ka[1] = ka
                            qa = not ka[1][ka[2]]
                            Ka = qa and 0x21e or 0x36d
                        end
                    else
                        Da = Da()
                        Da = {[2] = 3, [3] = Da}
                        Da[1] = Da
                        k = false
                        Ka, k = Ka + -438, {[2] = 3, [3] = k}
                        k[1] = k
                        H = false
                        H = {[2] = 3, [3] = H}
                        H[1] = H
                        e = nil
                        e = {[2] = 3, [3] = e}
                        e[1] = e
                        wa = {}
                        m = wa
                        m = {[2] = 3, [3] = m}
                        m[1] = m
                        wa = nil
                        wa = {[2] = 3, [3] = wa}
                        wa[1] = wa
                        qb = nil
                        qb = {[2] = 3, [3] = qb}
                        qb[1] = qb
                        ma = false
                        ma = {[2] = 3, [3] = ma}
                        ma[1] = ma
                        la = Va._["os"]
                        Mb = la["clock"]
                    end
                elseif Ka >= 0x3d6 then
                    if Ka > 0x3da then
                        Ka, qa = 0x32f, qa(fb, Ta)
                    elseif Ka >= 0x3d9 then
                        if Ka > 0x3d9 then
                            K = K(Gb, X, da)
                            Ka = K and 0x3f1 - Ka or 177
                        else
                            r, ta, R = r(ta)
                            r, ta, R = Va.b(r, ta, R)
                            Cb = r(ta, R)
                            R = Cb
                            Ka = R == nil and 0xa1 or Ka + -0x320
                        end
                    else
                        ga = ga(ib, O, Sa, j)
                        Ka = ga and 0x3576a / Ka or 0x1c87a / Ka
                    end
                elseif Ka <= 0x3d2 then
                    if Ka <= 0x3cf then
                        Ka, Ta = 0x701d9 / Ka, Ta(Y, u, zb)
                        fb[1][fb[2]] = Ta
                    else
                        Na(Pb, B)
                        Pb, Ka, Na = Va:fa{ua}, 0x581 - Ka, Va._["pcall"]
                    end
                else
                    Ka, Pb = 0x5f7 - Ka, Pb(B)
                    Na["SurfaceInset"] = Pb
                    B, Pb = "2F1B13", bb
                end
            elseif Ka < 0x38b then
                if Ka > 0x36d then
                    if Ka > 0x376 then
                        if Ka <= 0x379 then
                            Pb = Pb(B)
                            Ka, Na["Surface"] = 0x6c5 - Ka, Pb
                            B, Pb = "352017", bb
                        else
                            Ka, Ta, fb, Y = 0x113, cb[1][cb[2]], cb[1][cb[2]].FindFirstChild, "AreaEggSlotsClient"
                        end
                    elseif Ka <= 0x374 then
                        if Ka >= 0x371 then
                            if Ka > 0x371 then
                                q, o = q(o)
                                Ka = Oa and 0xe8 or 0xca
                            else
                                Ka, Fb = 0x34b25 / Ka, Fb(_b)
                            end
                        else
                            Ka, P = 0x5fc - Ka, P(G, S, w)
                            J["RequestDropHeldAreaEgg"] = P
                            S, w, P, G = "IsReadyToHatch", "IsLocalEggReady", Na[1][Na[2]]["pickFn"], ab
                        end
                    else
                        K = K(Gb, X, da)
                        Ka = K and 0xf244 / Ka or 0x24
                    end
                elseif Ka < 0x361 then
                    if Ka < 0x356 then
                        Ka, K = 0x36e - Ka, K(Gb)
                    elseif Ka <= 0x356 then
                        Ka, _b = 0x341fc / Ka, _b(ga)
                    else
                        Ka, pb = 0x8bf2e / Ka, pb(Ma, cb)
                        pb = {[2] = 3, [3] = pb}
                        pb[1] = pb
                        Ma, l = Va._["game"], "VirtualUser"
                        cb, Ma = Ma, Ma.GetService
                    end
                elseif Ka >= 0x369 then
                    if Ka <= 0x369 then
                        _ = _(jb)
                        jb = "table"
                        Ka, Cb = 256, _ == jb
                    else
                        qa = ka[1][ka[2]]
                        Ka = qa and 0x397 or 0x69c - Ka
                    end
                elseif Ka <= 0x361 then
                    Ka, zb = 0x47e - Ka, Va.c(zb(b))
                else
                    Ka = Ka + -0x22e
                    ca(Va.d(U))
                    mb, U, ca = Va:Ja{A, jb, Na}, ob[1][ob[2]]["CharacterAdded"], Na[1][Na[2]]["track"]
                    U, va = U.Connect, U
                end
            elseif Ka < 0x3a3 then
                if Ka < 0x391 then
                    if Ka < 0x38d then
                        eb = false
                        eb = {[2] = 3, [3] = eb}
                        eb[1] = eb
                        T = false
                        T = {[2] = 3, [3] = T}
                        T[1] = T
                        Ba = nil
                        Ba = {[2] = 3, [3] = Ba}
                        Ka, Ba[1] = 0x24c, Ba
                        Ea = 0
                        Ea = {[2] = 3, [3] = Ea}
                        Ea[1] = Ea
                        Jb = nil
                        Jb = {[2] = 3, [3] = Jb}
                        Jb[1] = Jb
                        fa = false
                        fa = {[2] = 3, [3] = fa}
                        fa[1] = fa
                        ub = {}
                        s = ub
                        s = {[2] = 3, [3] = s}
                        s[1] = s
                        ub = false
                        ub = {[2] = 3, [3] = ub}
                        ub[1] = ub
                        xa = false
                        xa = {[2] = 3, [3] = xa}
                        xa[1] = xa
                        Nb = 0
                        Nb = {[2] = 3, [3] = Nb}
                        Nb[1] = Nb
                        i = 0
                        i = {[2] = 3, [3] = i}
                        i[1] = i
                        Ia = Va._["os"]
                        D = Ia["clock"]
                    elseif Ka > 0x38d then
                        P = P(G, S, w)
                        J["RequestCarryAreaEgg"] = P
                        P, w, S, Ka, G = Na[1][Na[2]]["pickFn"], "RequestDropHeldAreaEgg", "DropFieldEgg", Ka + -0x1f, ab
                    else
                        p(Aa)
                        p = {[2] = 3, [3] = p}
                        Ka, p[1] = 0x33c, p
                        Aa, p[1][p[2]] = nil, Va:S()
                        Aa = {[2] = 3, [3] = Aa}
                        Aa[1] = Aa
                        A = {[2] = 3, [3] = A}
                        A[1] = A
                        mb, U, A[1][A[2]], ca = Va:r{Na, jb}, Ya[1][Ya[2]]["JumpRequest"], Va:Kc{ob, Aa, Na, p}, Na[1][Na[2]]["track"]
                        U, va = U.Connect, U
                    end
                elseif Ka >= 0x39e then
                    if Ka <= 0x39e then
                        Ka, Pb = 0x145, Pb(B)
                        Na["TextSecondary"] = Pb
                        Pb, B = bb, "A47B69"
                    else
                        Ka, d = 0x8a, d(h)
                    end
                elseif Ka > 0x391 then
                    Ka, Ta, qa, fb = 0x3dc, "GuardAreas", ka[1][ka[2]].FindFirstChild, ka[1][ka[2]]
                else
                    Pb = Pb(B)
                    Ka, Na["ControlPressed"] = 0x261, Pb
                    Pb, B = bb, "1A0F0B"
                end
            elseif Ka <= 0x3ae then
                if Ka <= 0x3a9 then
                    if Ka < 0x3a8 then
                        Ka, Lb = 0xa0, Lb(sa)
                    elseif Ka > 0x3a8 then
                        na, x = _(jb, aa)
                        aa = na
                        Ka = aa == nil and 0x81 or 0x4b0 - Ka
                    else
                        ib = ib(O, Sa, j, ab)
                        Ka = ib and 126 or 240
                    end
                else
                    Ka, Pb = 0x619 - Ka, Pb(B)
                    Na["BorderSubtle"] = Pb
                    B, Pb = "5B3424", bb
                end
            elseif Ka > 0x3b4 then
                qa = {}
                qa, Ka, ka = Va._["getgenv"], 0x22d, qa
            elseif Ka > 0x3b2 then
                Ka = 0x86
                Db(wb)
            else
                Ka, cb = 0x3cd, cb(l, xb)
                cb = {[2] = 3, [3] = cb}
                cb[1] = cb
                l, Pa = Va._["game"], "ReplicatedStorage"
                l, xb = l.GetService, l
            end
        until false
    end
end,
Fe = function (e, a)
    return function ()
        local d, c, b, _
        _ = 0xc8
        while true do
            if _ < 200 then
                d = e.c(d(c, b))
                return e.d(d)
            else
                _, b, d = 164, "PlayerGui", a[1][1][a[1][2]]
                c, d = d, d.WaitForChild
            end
        end
    end
end,
lc = function (e, h)
    return function (d)
        local a, m, f, g, c, i, o, b, j, _, n, l, k, p
        j = 60
        repeat
            if j <= 112 then
                if j <= 0x47 then
                    if j < 0x1e then
                        if j > 10 then
                            if j > 12 then
                                j, p = 2, p(f, _, o)
                                o = h[2][1][h[2][2]]
                                _, o = o["specialEggTeleport"], c[1][c[2]]
                            else
                                _ = h[2][1][h[2][2]]
                                o, j, f = h[5][1][h[5][2]], 192, _["waitFor"]
                                l, _, o = e:We{h[2], m, h[3], d, c}, o["GrabDelay"], 0.04
                            end
                        elseif j <= 7 then
                            if j < 2 then
                                _(o)
                                l, o = true, h[3][1][h[3][2]]
                                _ = o == l
                                return _
                            elseif j > 2 then
                                j, b = j + 0x40, e.c(b(i, g, k))
                            else
                                _ = _(o)
                                f = not _
                                j = f and 257 - j or 114
                            end
                        else
                            j, n = 0x87a / j, not c[1][c[2]]
                        end
                    elseif j > 0x39 then
                        if j >= 68 then
                            if j > 68 then
                                j = j + 0x5e
                                o(l, e.d(b))
                            else
                                o = e._["task"]
                                _, j, o = o["wait"], 218, 0.05
                            end
                        else
                            d = {[2] = 3, [3] = d}
                            d[1] = d
                            j, m = 0xd4, h[2][1][h[2][2]]
                            c = m["swapStealHumanoid"]
                        end
                    elseif j > 53 then
                        _ = false
                        h[1][1][h[1][2]] = _
                        return _
                    elseif j < 0x2a then
                        _ = _()
                        o = 2.5
                        j, f = 0x13ec / j, _ + o
                    elseif j <= 42 then
                        f = false
                        h[1][1][h[1][2]] = f
                        return f
                    else
                        c = c(m)
                        c = {[2] = 3, [3] = c}
                        c[1] = c
                        n = h[2][1][h[2][2]]
                        j, m = 0x5d, n["getRoot"]
                    end
                elseif j >= 102 then
                    if j >= 0x6b then
                        if j < 111 then
                            a = m[1][m[2]]["Position"]
                            p, n = m[1][m[2]]["Position"], a.X
                            j, f, a = j + -0x53, h[2][1][h[2][2]], p.Z
                            p, o, _, f = f["groundedY"], m[1][m[2]]["Position"], a, n
                            o = o.Y
                        elseif j > 0x6f then
                            j, o = 0xdc, h[2][1][h[2][2]]
                            _ = o["stealingEnabled"]
                        else
                            _ = d[1][d[2]]["Name"]
                            _, j, h[4][1][h[4][2]] = false, j + -0x6e, _
                            h[1][1][h[1][2]], o = _, e._["task"]
                            o, _ = h[5][1][h[5][2]], o["wait"]
                            o = o["ReturnPace"]
                        end
                    elseif j <= 0x68 then
                        if j > 102 then
                            _(o)
                            _ = h[3][1][h[3][2]]
                            j = _ and j + 0x5a or 68
                        else
                            c = false
                            h[1][1][h[1][2]] = c
                            return c
                        end
                    else
                        j, o = j + -25, o()
                        _ = o < f
                    end
                elseif j <= 0x55 then
                    if j > 0x50 then
                        j, o = 168, h[2][1][h[2][2]]
                        l, b, _, o = c[1][c[2]].Z, c[1][c[2]].Y, o["groundedY"], c[1][c[2]].X
                    elseif j > 74 then
                        j = _ and j + 0x83 or 0xc2
                    else
                        j = 0xdf
                        c()
                        n = m
                        m = n["prepareForestEggBeforeSteal"]
                    end
                elseif j > 91 then
                    m = m()
                    m = {[2] = 3, [3] = m}
                    m[1] = m
                    n = not m[1][m[2]]
                    j = n and j + 124 or 10
                else
                    c = false
                    h[1][1][h[1][2]] = c
                    return c
                end
            elseif j <= 204 then
                if j < 0xaa then
                    if j < 0x98 then
                        if j <= 128 then
                            if j <= 0x72 then
                                j, o = 266 - j, h[2][1][h[2][2]]
                                _ = o["stealingEnabled"]
                            else
                                n = false
                                h[1][1][h[1][2]] = n
                                return n
                            end
                        else
                            m = h[2][1][h[2][2]]
                            j, c = j + -0x38, m["stabilizeStealRoot"]
                        end
                    elseif j < 165 then
                        _ = _()
                        f = not _
                        j = f and 0xc2 - j or 0x720 / j
                    elseif j <= 0xa5 then
                        j, o = 104, h[2][1][h[2][2]]
                        _, o = o["tryCarryEgg"], d[1][d[2]]
                    else
                        _ = _(o, l, b)
                        l = h[2][1][h[2][2]]
                        o, l, j, i = l["placeRoot"], m[1][m[2]], 0x498 / j, e._["CFrame"]
                        g, k, i, b = _, c[1][c[2]].Z, c[1][c[2]].X, i["new"]
                    end
                elseif j > 194 then
                    if j > 195 then
                        m = h[2][1][h[2][2]]
                        j, c, m = 0x35, m["getSlotEggPosition"], d[1][d[2]]
                    else
                        j = _ and j + -10 or 209
                    end
                elseif j >= 192 then
                    if j > 0xc0 then
                        o = h[3][1][h[3][2]]
                        _ = not o
                        j = _ and j + -137 or j + -0x53
                    else
                        j = 0x1680 / j
                        f(_, o, l)
                        o = e._["os"]
                        _ = o["clock"]
                    end
                elseif j <= 170 then
                    _ = h[6][1][h[6][2]]
                    j = _ and 0x11a - j or 195
                else
                    o = h[3][1][h[3][2]]
                    j, _ = 0x18a - j, not o
                end
            elseif j <= 220 then
                if j < 217 then
                    if j < 211 then
                        j = _ and 246 or 0x50
                    elseif j <= 211 then
                        o = h[2][1][h[2][2]]
                        j, _ = 233, o["getRoot"]
                    else
                        c()
                        n = m
                        j, m = 240, n["prepareStealHumanoid"]
                    end
                elseif j < 0xda then
                    j = n and j + -0x59 or j + -0x6e
                elseif j <= 0xda then
                    j = 0x90c4 / j
                    _(o)
                else
                    j, _ = 0xc3, _()
                end
            elseif j > 240 then
                if j <= 0xf6 then
                    l = e._["os"]
                    j, o = 351 - j, l["clock"]
                else
                    f = false
                    h[1][1][h[1][2]] = f
                    return f
                end
            elseif j <= 233 then
                if j <= 0xdf then
                    m = m()
                    c = not m
                    j = c and 0x66 or 0xb1b4 / j
                else
                    _ = _()
                    m[1][m[2]] = _
                    j = m[1][m[2]] and 85 or 165
                end
            else
                m = m()
                c = not m
                j = c and 0x5b or 0x82
            end
        until false
    end
end,
Ra = function (e)
    return function ()
        local b, d, f, _, c
        _ = 0x58
        while true do
            if _ < 121 then
                if _ > 0x4a then
--===== [UI] External UI library loader (original URL kept intact) =====
                    d, _, f, c = e._["loadstring"], 0xb1, "https://raw.githubusercontent.com/TND-Hub/TND-Hub/refs/heads/main/TNDHubUI.min.lua", e._["game"]
                    c, b = c.HttpGet, c
                else
                    d = e.c(d())
                    return e.d(d)
                end
            elseif _ <= 121 then
                _, d = 195 - _, d(e.d(c))
            else
                _, c = 0x79, e.c(c(b, f))
            end
        end
    end
end,
rd = function (e, a)
    return function ()
        local d, c
        d, c = a[1][1][a[1][2]], true
        d["Anchored"] = c
        return
    end
end,
gb = function (e, h)
    return function ()
        local i, f, b, a, g, d, j, c
        j = 126
        repeat
            if j <= 79 then
                if j > 0x39 then
                    if j > 62 then
                        j = c and 164 - j or 57
                    else
                        i = i(a, g, f)
                        c = b + i
                        return c
                    end
                elseif j > 0x21 then
                    c = h[1][1][h[1][2]]
                    j, d = 0x42 - j, c["getBasePosition"]
                elseif j <= 9 then
                    d = e.c(d())
                    return e.d(d)
                else
                    j, c = 0xdaa / j, h[2][1][h[2][2]]
                    d = c["GetPlotData"]
                end
            elseif j > 126 then
                j, c = 206 - j, d["PetArea"]
            elseif j <= 0x6a then
                if j > 85 then
                    d = d()
                    c = d
                    j = c and 127 or 185 - j
                else
                    i = d["PetArea"]
                    b, j, a = i["Position"], j + -0x17, e._["Vector3"]
                    g, i, a = 4, a["new"], 0
                    f = a
                end
            else
                c = h[2][1][h[2][2]]
                d = c["GetPlotData"]
                j = d and 33 or 0x39
            end
        until false
    end
end,
aa = function (e, h)
    return function ()
        local m, p, i, a, c, l, j, n, b, f, _, d, o
        j = 72
        repeat
            if j < 0x80 then
                if j < 0x5f then
                    if j > 71 then
                        if j < 78 then
                            j, c = 0x47, h[2][1][h[2][2]]
                            d = c["getSave"]
                        elseif j > 78 then
                            j = b and j + 0x6a or 0xb1
                        else
                            p = h[2][1][h[2][2]]
                            f, a = h[6][1][h[6][2]], p["netInvoke"]
                            j, p = 0xf5, f["Trails"]
                            p = p["WORN_SNAPSHOT"]
                        end
                    elseif j >= 0x3e then
                        if j <= 0x3e then
                            b = h[5][1][h[5][2]]
                            l = b[o]
                            b = l
                            j = b and j + 0xb2 or 155 - j
                        else
                            d = d()
                            c = d
                            j = c and 241 or 0xb3 - j
                        end
                    elseif j <= 0x21 then
                        _ = h[2][1][h[2][2]]
                        j, l, f = 226 - j, h[6][1][h[6][2]], _["netInvoke"]
                        o = l["Trails"]
                        o, _ = m, o["REQUEST_SELECT"]
                    else
                        j = p and 0x1858 / j or 0x8f
                    end
                elseif j <= 109 then
                    if j > 0x6c then
                        j = f and 0xd6 - j or 0xe0d / j
                    elseif j > 0x69 then
                        j, n, m = 171, c, e._["typeof"]
                    elseif j <= 0x5f then
                        f = f(_)
                        _ = "table"
                        p = f == _
                        j = p and 121 or 38
                    else
                        f = false
                        return f
                    end
                elseif j <= 0x79 then
                    if j <= 116 then
                        f = f(_)
                        j, p = 38, a[f]
                    else
                        f, j, _ = e._["tostring"], 0x74, h[4][1][h[4][2]]
                        _ = _["UserId"]
                    end
                else
                    j, f = 0x35a6 / j, p == m
                end
            elseif j > 0xb1 then
                if j <= 0xf0 then
                    if j >= 0xcb then
                        if j > 0xcb then
                            j, b = 0x5730 / j, c[l]
                        else
                            m, j, n = l, 177, b
                        end
                    elseif j <= 193 then
                        f(_, o)
                        f = true
                        return f
                    else
                        i = h[3][1][h[3][2]]
                        b = i[o]
                        j = b and 0x787d / j or 0x89
                    end
                elseif j <= 245 then
                    if j > 0xf1 then
                        j, a = 95, a(p)
                        f, _ = e._["typeof"], a
                    else
                        j, c = 0x15d - j, d["TrailInventory"]
                    end
                else
                    m, p, j, a, n = nil, h[1][1][h[1][2]], 376 - j, e._["ipairs"], -1
                end
            elseif j > 156 then
                if j > 171 then
                    _, o = a(p, f)
                    f = _
                    j = f == nil and 0xff - j or 62
                elseif j <= 164 then
                    f = not m
                    j = f and 273 - j or 0x7e
                else
                    m = m(n)
                    n = "table"
                    j = m ~= n and 0x6834 / j or 248
                end
            elseif j > 143 then
                if j <= 0x9b then
                    j = b > n and 0x7ae9 / j or j + 0x16
                else
                    m = false
                    return m
                end
            elseif j > 137 then
                j, p = 0xa4, nil
            elseif j <= 128 then
                a, p, f = a(p)
                a, p, f = e.b(a, p, f)
                _, o = a(p, f)
                f = _
                j = f == nil and 78 or 0x3e
            else
                j, b = 0x124 - j, 0
            end
        until false
    end
end,
Fc = function (s, h)
    return function (d, c, A)
        local b, l, r, k, _, v, p, z, w, a, e, f, t, y, m, i, o, x, n, j, g, u, q, B
        j = 0x9e
        repeat
            if j < 159 then
                if j >= 87 then
                    if j >= 130 then
                        if j <= 144 then
                            if j < 0x8c then
                                if j > 0x82 then
                                    j, g = j + 0x6b, s._["RaycastParams"]
                                    i = g["new"]
                                else
                                    j = e <= 0 and 0xa7 or 0x5c6c / j
                                end
                            elseif j > 0x8c then
                                j = m and 0x1d or 254
                            else
                                j = 0x67e8 / j
                                m(u, p)
                            end
                        elseif j > 0x9b then
                            a = h[2][1][h[2][2]]
                            j, n = 74, a["getLaneY"]
                        else
                            j, l = 0x7d, a["Size"]
                            l, r = 0.5, l.Y
                            _ = r * l
                        end
                    elseif j < 114 then
                        if j <= 0x5a then
                            if j <= 0x57 then
                                j, _ = 0xc9 - j, 1
                            else
                                j, a = 0x3d86 / j, a()
                                f = z
                                z = f["getHumanoid"]
                            end
                        else
                            j = e <= 0 and 0x29 or 66
                        end
                    elseif j >= 0x79 then
                        if j <= 121 then
                            j, m = 0x90, q <= l
                        else
                            j = _ and 114 or 212 - j
                        end
                    else
                        r, t = f + _, 1.5
                        l, i = n + t, {}
                        g, t = h[1][1][h[1][2]], i
                        i = g["Character"]
                        j = i and 0x14f - j or 134
                    end
                elseif j <= 57 then
                    if j >= 0x29 then
                        if j <= 0x37 then
                            if j >= 0x2e then
                                if j <= 0x2e then
                                    j, u = 0x49, s._["string"]
                                    p, m = u, u["find"]
                                    u, p = p["lower"], o
                                else
                                    j = y > v and 0xe8 - j or 226 - j
                                end
                            else
                                j = y < v and 0xda - j or 66
                            end
                        else
                            j, v = j + 152, s._["math"]
                            y, v, b = v["clamp"], k + r, 2
                            b, e = 5, n - b
                            b = n + b
                        end
                    elseif j <= 29 then
                        if j > 12 then
                            j, k = 0xb1, q
                        else
                            o = o(x, m, u)
                            m = s._["Vector3"]
                            u, x, m = -160, m["new"], 0
                            j, p = 0xa0, m
                        end
                    else
                        _ = a
                        j = _ and 0x9b or 0xfa0 / j
                    end
                elseif j > 0x45 then
                    if j > 73 then
                        n = n()
                        j, z = 164 - j, a
                        a = z["getRoot"]
                    else
                        j, u = 188, u(p)
                        p, B, w = "ground", true, 1
                    end
                elseif j < 66 then
                    v = 3
                    y = n + v
                    return y
                elseif j <= 66 then
                    i["FilterDescendantsInstances"] = t
                    x, b = s._["Vector3"], h[3][1][h[3][2]]
                    x, j, o, u, m = d, 12, x["new"], c, g
                else
                    j, l, r = 306 - j, 0, z["HipHeight"]
                    _ = r > l
                end
            elseif j <= 0xd1 then
                if j >= 182 then
                    if j < 191 then
                        if j <= 188 then
                            if j <= 0xb6 then
                                j = e ~= e and 0xb1 or 66
                            else
                                m = m(u, p, w, B)
                                u = nil
                                j, x = 0xe7, m ~= u
                            end
                        else
                            y = y + e
                            j = e > 0 and j + 0x38 or 0x82
                        end
                    elseif j >= 208 then
                        if j > 208 then
                            y = s.c(y(v, e, b))
                            return s.d(y)
                        else
                            j, f = 32, z["HipHeight"]
                        end
                    elseif j <= 0xbf then
                        j = e > 0 and j + -0x88 or 0x7f95 / j
                    else
                        y = y(v)
                        v = "number"
                        j = y == v and 0xb4d7 / j or j + -135
                    end
                elseif j >= 171 then
                    if j < 0xaf then
                        j = e ~= e and 0x29 or 0x42cc / j
                    elseif j <= 0xaf then
                        z = z()
                        _, f = z, 2
                        j = _ and 69 or j + 62
                    else
                        j = k and j + -0x78 or 336 - j
                    end
                elseif j >= 160 then
                    if j <= 160 then
                        j, x = 0x19f - j, x(m, u, p)
                        b, q, m = b.Raycast, b, i
                    else
                        j = y < v and 177 or 0x15d - j
                    end
                else
                    y, j, v = s._["typeof"], 197, A
                end
            elseif j >= 0xeb then
                if j > 0xf6 then
                    if j > 0xfe then
                        b = b(q, o, x, m)
                        q = not b
                        j = q and j + -0x4e or j + -0x16
                    else
                        u = s._["table"]
                        j, u, m, p = 140, t, u["insert"], b["Instance"]
                    end
                elseif j > 241 then
                    j = y > v and 0xaa16 / j or 0x82
                elseif j <= 0xed then
                    if j <= 0xeb then
                        v = s._["math"]
                        b, y, v = 2, v["clamp"], A
                        e, b = n - b, 5
                        j, b = 0xda, n + b
                    else
                        j = _ and 0xc090 / j or 269 - j
                    end
                else
                    i = i()
                    y = s._["Enum"]
                    k = y["RaycastFilterType"]
                    g = k["Exclude"]
                    i["FilterType"] = g
                    k = 40
                    k, v, y, g = nil, 20, 1, n + k
                    e = y
                    j = v ~= v and 0xb1 or 0xb3cf / j
                end
            elseif j < 0xe4 then
                if j <= 0xda then
                    y = s.c(y(v, e, b))
                    return s.d(y)
                else
                    j, g = j + 7, s._["table"]
                    i, g, k = g["insert"], t, h[1][1][h[1][2]]
                    k = k["Character"]
                end
            elseif j <= 231 then
                if j > 228 then
                    m = x
                    j = m and j + -87 or 0x6d2f / j
                else
                    j = 134
                    i(g, k)
                end
            else
                o = b["Position"]
                q, x = o.Y, b["Instance"]
                m, o = "Ground", x["Name"]
                x = o == m
                j = x and 464 - j or 0x2e
            end
        until false
    end
end,
He = function (e, h)
    return function (d)
        local f, c, _, b
        _ = 92
        while true do
            if _ >= 0x5c then
                if _ <= 175 then
                    if _ < 119 then
                        b, f = h[2][1][h[2][2]], d["ClassName"]
                        c = b[f]
                        _ = c and 0x3d or 0xee
                    elseif _ > 0x77 then
                        _ = 49
                        c(b, f)
                    else
                        _, c = 357 - _, c(b)
                    end
                else
                    _ = c and 89 or 0x31
                end
            elseif _ < 0x3d then
                return
            elseif _ <= 61 then
                b = h[1][1][h[1][2]]
                c, _, b = b["isOn"], 0x77, "FpsBoost"
            else
                _, b = 0xaf, h[1][1][h[1][2]]
                f, c, b = false, b["setEffectEnabled"], d
            end
        end
    end
end,
r = function (e, h)
    return function ()
        local i, _, b, d, c, a
        _ = 10
        while true do
            if _ > 166 then
                if _ <= 236 then
                    if _ > 187 then
                        c = c(b)
                        _, d = 187, not c
                    elseif _ <= 0xac then
                        b = h[1][1][h[1][2]]
                        _, c, b = 408 - _, b["isOn"], "InfJump"
                    else
                        _ = d and 0xf7 or _ + -21
                    end
                else
                    return
                end
            elseif _ <= 136 then
                if _ <= 0x2d then
                    if _ > 44 then
                        return
                    elseif _ > 10 then
                        a = e._["Enum"]
                        _, i = 144, a["HumanoidStateType"]
                        c, i, b = d.ChangeState, i["Jumping"], d
                    else
                        c = h[2][1][h[2][2]]
                        d = not c
                        _ = d and 187 or 0xac
                    end
                else
                    d = d()
                    _ = d and 0x2c or 0x2d
                end
            elseif _ <= 0x90 then
                _ = 0x2d
                c(b, i)
            else
                _, c = 0x5830 / _, h[1][1][h[1][2]]
                d = c["getHumanoid"]
            end
        end
    end
end,
Yc = function (e, g)
    return function ()
        local d, c, b, _
        _ = 211
        repeat
            if _ > 0xd3 then
                return d
            elseif _ <= 165 then
                _, c = _ + 0x34, g[1][1][g[1][2]]
                d = not c
            else
                b, c = nil, g[2][1][g[2][2]]
                d = c ~= b
                _ = d and 217 or 165
            end
        until false
    end
end,
Sc = function (e, a)
    return function ()
        local c, _, d
        _ = 234
        while true do
            if _ >= 234 then
                c, d = false, a[1][1][a[1][2]]
                d["Enabled"] = c
                c, _, d = d, 0x9b, d.Destroy
            else
                d(c)
                return
            end
        end
    end
end,
Ca = function (e, h)
    return function ()
        local a, d, g, c, b, j, i
        j = 0xd0
        while true do
            if j >= 0x60 then
                if j >= 208 then
                    if j > 0xd0 then
                        b(i)
                        j, i = j + -206, h[2][1][h[2][2]]
                        b, g = i["netInvoke"], h[3][1][h[3][2]]
                        a = g["GroupReward"]
                        i, a = a["CLAIM_REWARD"], c[1][c[2]]
                    else
                        j, c = 96, h[2][1][h[2][2]]
                        d = c["getSave"]
                    end
                elseif j > 0x60 then
                    j, c = 384 - j, false
                    c = {[2] = 3, [3] = c}
                    c[1] = c
                    b, i = e._["pcall"], e:wd{h[1], c, h[4]}
                else
                    d = d()
                    c = d
                    j = c and 90 or 159 - j
                end
            elseif j >= 63 then
                if j > 63 then
                    j, b, i = 0x3f, d["ClaimedGroupReward"], true
                    c = b == i
                else
                    j = c and j + -50 or 0x87
                end
            elseif j <= 13 then
                c = false
                return c
            else
                b(i, a)
                b = true
                return b
            end
        end
    end
end,
Df = {}, z = function (e, h)
    return function (d)
        local c, _, f, b
        _ = 0xe7
        repeat
            if _ < 0x8e then
                if _ > 0x64 then
                    if _ > 105 then
                        _ = 154 - _
                        c(b)
                    else
                        _ = c and _ + 0x79 or _ + 37
                    end
                elseif _ > 0x4d then
                    c = c(b)
                    b = 0x12c
                    _ = c >= b and 249 - _ or 38
                elseif _ <= 0x26 then
                    c, b = h[1][1][h[1][2]], true
                    c[d] = b
                    return
                else
                    b = b(f)
                    f = "string"
                    c = b ~= f
                    _ = c and 105 or 0x422c / _
                end
            elseif _ > 0xdc then
                if _ <= 0xe2 then
                    return
                else
                    f, _, b = d, 77, e._["typeof"]
                end
            elseif _ < 0x95 then
                _, b = 100, h[2][1][h[2][2]]
                b, c = h[1][1][h[1][2]], b["countTable"]
            elseif _ > 149 then
                b = ""
                _, c = 105, d == b
            else
                _, b = 116, h[2][1][h[2][2]]
                b, c = h[1][1][h[1][2]], b["clearTable"]
            end
        until false
    end
end,
t = function (e, h)
    return function ()
        local j, k, f, i, c, d, b, a
        j = 0x71
        while true do
            if j > 0x78 then
                if j > 0xb9 then
                    if j >= 0xe8 then
                        if j < 0xf3 then
                            if j <= 233 then
                                if j > 232 then
                                    k = e._["os"]
                                    j, a = 0x38, k["clock"]
                                else
                                    j = 0x20
                                    k(f)
                                end
                            else
                                i = h[4][1][h[4][2]]
                                j = i and 35 or 0xd0
                            end
                        elseif j > 246 then
                            j = j + -75
                            i(a)
                            a = h[1][1][h[1][2]]
                            f, a, i, k = e:ad{h[2]}, 0.25, a["waitFor"], 0.03
                        elseif j > 243 then
                            j, k = 0x8688 / j, k()
                            a = k < i
                        else
                            f = e._["os"]
                            j, k = j + 3, f["clock"]
                        end
                    elseif j <= 208 then
                        if j < 191 then
                            j, i = 52, h[2][1][h[2][2]]
                        elseif j <= 0xbf then
                            a, j, i = h[3][1][h[3][2]], 0xb9, e._["pcall"]
                            a = a["RequestAreaEggSnapshot"]
                        else
                            j = i and 0x88 or 0x48
                        end
                    elseif j > 211 then
                        j = 0x115 - j
                        k(f)
                    else
                        f = e._["task"]
                        f, j, k = 0.04, 0xbf38 / j, f["wait"]
                    end
                elseif j < 0xa5 then
                    if j < 0x8c then
                        if j <= 132 then
                            if j > 124 then
                                k = h[1][1][h[1][2]]
                                k, j, a = d, 165, k["findEggInstanceByUid"]
                            else
                                a = a()
                                j, i = 0x64c0 / j, a < b
                            end
                        else
                            j, i = 72, h[2][1][h[2][2]]
                        end
                    elseif j > 0x9a then
                        j, k = 0x14c - j, h[2][1][h[2][2]]
                        a = not k
                    elseif j <= 140 then
                        j = a and 0x110 - j or j + -42
                    else
                        d, c = h[1][1][h[1][2]], true
                        d["_regrabBusy"] = c
                        c, d = false, h[5][1][h[5][2]]
                        c = {[2] = 3, [3] = c}
                        c[1] = c
                        i = h[3][1][h[3][2]]
                        b = i["RequestDropHeldAreaEgg"]
                        j = b and 0x78 or 0xab
                    end
                elseif j > 0xad then
                    if j >= 0xb8 then
                        if j > 0xb8 then
                            j = j + -127
                            i(a)
                        else
                            j = 0xee
                            i(a)
                        end
                    else
                        f = h[1][1][h[1][2]]
                        k, j, f = f["tryCarryEgg"], 28, a
                    end
                elseif j <= 171 then
                    if j <= 0xa8 then
                        if j > 165 then
                            j = a and 0xf3 or 0x134 - j
                        else
                            a = a(k)
                            j = a and 0xaf or 0x30
                        end
                    else
                        j, a = 0x75, e._["os"]
                        i = a["clock"]
                    end
                else
                    j = 114
                    i(a, k, f)
                end
            elseif j <= 57 then
                if j < 0x23 then
                    if j > 12 then
                        if j < 28 then
                            j, a = 12, h[3][1][h[3][2]]
                            i = a["RequestDropHeldAreaEgg"]
                        elseif j > 0x1c then
                            a = h[4][1][h[4][2]]
                            j = a and 0xa4 or 0x1500 / j
                        else
                            j = 0x30
                            k(f)
                        end
                    elseif j < 10 then
                        if j <= 4 then
                            j = 0xe9
                            i(a)
                        else
                            d = false
                            return d
                        end
                    elseif j > 10 then
                        j = i and 10 or 0x558 / j
                    else
                        j, a, i = 0x102 - j, e:cd{h[3]}, e._["pcall"]
                    end
                elseif j < 48 then
                    if j >= 0x2b then
                        if j <= 0x2b then
                            i = h[4][1][h[4][2]]
                            j = i and 0x1fbf / j or 0x5f - j
                        else
                            f, j, k = h[3][1][h[3][2]], 213, e._["pcall"]
                            f = f["RequestAreaEggSnapshot"]
                        end
                    else
                        k = e._["os"]
                        j, a = 0x7c, k["clock"]
                    end
                elseif j > 0x38 then
                    j = 0xab
                    b(i)
                elseif j <= 0x34 then
                    if j > 48 then
                        j = i and 0x2a4 / j or 0x270 / j
                    else
                        f = h[2][1][h[2][2]]
                        k = not f
                        j = k and 130 - j or 0x7d - j
                    end
                else
                    a = a()
                    j, f = 0x58 - j, h[6][1][h[6][2]]
                    k = f["RegrabTimeout"]
                    i = a + k
                end
            elseif j >= 0x6b then
                if j >= 114 then
                    if j < 117 then
                        a = h[2][1][h[2][2]]
                        i = not a
                        j = i and j + -7 or 233
                    elseif j <= 117 then
                        j, i = 0x163 - j, i()
                        k = h[6][1][h[6][2]]
                        a = k["DropVerifyTimeout"]
                        b = i + a
                    else
                        i, j, b = e:bd{c, h[3]}, 0x1ab8 / j, e._["pcall"]
                    end
                elseif j >= 109 then
                    if j > 0x6d then
                        c = h[2][1][h[2][2]]
                        d = not c
                        j = d and 6 or 0x9a
                    else
                        a = h[3][1][h[3][2]]
                        i = a["RequestAreaEggSnapshot"]
                        j = i and 0x5153 / j or 0x3a
                    end
                else
                    a = e._["task"]
                    i, a = a["wait"], h[6][1][h[6][2]]
                    j, a = 4, a["RegrabDelay"]
                end
            elseif j <= 0x4d then
                if j < 72 then
                    if j <= 58 then
                        a = e._["task"]
                        a, j, i = h[6][1][h[6][2]], 184, a["wait"]
                        a = a["DropRetryDelay"]
                    else
                        f = h[2][1][h[2][2]]
                        k = not f
                        j = k and 275 - j or j + -32
                    end
                elseif j <= 0x48 then
                    j = i and 0x6d or 0x73 - j
                else
                    j = k and 0x7b - j or 0x40
                end
            elseif j <= 0x52 then
                f = h[3][1][h[3][2]]
                j, k = 0x4d, f["RequestAreaEggSnapshot"]
            else
                a, k = h[1][1][h[1][2]], false
                a["_regrabBusy"] = k
                f, k = true, h[2][1][h[2][2]]
                a = k == f
                return a
            end
        end
    end
end,
ie = function (e, a)
    return function ()
        local _, d, c
        _ = 0x85
        repeat
            if _ >= 133 then
                _, d = 0x26, a[1][1][a[1][2]]
                c, d = d, d.Destroy
            else
                d(c)
                return
            end
        until false
    end
end,
Ge = function (e, a)
    return function ()
        local d, _, c
        _ = 0xc9
        repeat
            if _ < 0xc9 then
                d(c)
                return
            else
                d = a[1][1][a[1][2]]
                _, d, c = 104, d.Destroy, d
            end
        until false
    end
end,
ce = function (e, a)
    return function ()
        local d, _, c
        _ = 0x35
        repeat
            if _ <= 53 then
                c = a[1][1][a[1][2]]
                _, c, d = 81, true, c["runAutoFusePets"]
            else
                d(c)
                return
            end
        until false
    end
end,
Ib = function (e, h)
    return function (d)
        local _, f, b, c
        _ = 170
        repeat
            if _ <= 98 then
                if _ < 40 then
                    if _ > 0x1f then
                        _, f = 0x124 - _, b["DisplayName"]
                    elseif _ < 27 then
                        f = h[1][1][h[1][2]]
                        b = f["Directory"]
                        c = b[d]
                        b = c
                        _ = b and 0x28 or _ + 75
                    elseif _ > 27 then
                        c = nil
                        return c
                    else
                        b = b(f)
                        f = "table"
                        _, c = 0xa4, b ~= f
                    end
                elseif _ <= 0x5e then
                    if _ <= 41 then
                        if _ > 0x28 then
                            f = b["_id"]
                            _ = f and 255 or 0x25
                        else
                            _, b = 98, c["Rarity"]
                        end
                    else
                        f = nil
                        return f
                    end
                else
                    f = not b
                    _ = f and 0xc0 - _ or 41
                end
            elseif _ > 150 then
                if _ >= 170 then
                    if _ <= 170 then
                        b, _, f = e._["typeof"], 136, d
                    else
                        return f
                    end
                else
                    _ = c and 0x1f or 0xbb - _
                end
            elseif _ < 142 then
                if _ <= 102 then
                    f, b = h[1][1][h[1][2]], e._["typeof"]
                    _, f = 0x1b, f["Directory"]
                else
                    b = b(f)
                    f = "string"
                    c = b ~= f
                    _ = c and 0x4fb0 / _ or 0x8e
                end
            elseif _ > 142 then
                _ = c and 0xa4 or 0x3bc4 / _
            else
                b = h[1][1][h[1][2]]
                _, c = 150, not b
            end
        until false
    end
end,
vd = function (e, a)
    return function ()
        local b, d, _, c
        _ = 0x4c
        while true do
            if _ > 0x4c then
                d(c, b)
                return
            else
                b, d = a[1][1][a[1][2]], a[2][1][a[2][2]]
                _, d, c = 176, d.EquipTool, d
            end
        end
    end
end,
Ed = function (e, a)
    return function ()
        local c, d, b, _
        _ = 0xdf
        repeat
            if _ < 223 then
                d = e.c(d(c, b))
                return e.d(d)
            else
                b, d = a[1][1][a[1][2]], e._["game"]
                _, d, c = 0x42, d.HttpGet, d
            end
        until false
    end
end,
Da = function (s, h)
    return function ()
        local e, r, k, g, v, j, i, t, u, p, b, n, d, c, f, l, a, _, m
        j = 127
        repeat
            if j > 135 then
                if j >= 0xd9 then
                    if j < 235 then
                        if j < 223 then
                            if j <= 217 then
                                j, v = j + -212, "?"
                            else
                                j, k = 0x1810 / j, s._["string"]
                                g, u, e, v, k = k["format"], i, r, s._["tostring"], "%s\n%s"
                            end
                        elseif j <= 229 then
                            if j > 223 then
                                j, n = 95, s.c(n())
                            else
                                j = t and 0xad or 231
                            end
                        else
                            p, f = m(n, a)
                            a = p
                            j = a == nil and j + 4 or 434 - j
                        end
                    elseif j > 0xf0 then
                        if j <= 244 then
                            k = k(u)
                            u, v = s._["tostring"], t
                            j = v and 0x4c4 / j or 0x1cd - j
                        else
                            j, i = 57, h[1][1][h[1][2]]
                            t, i = i["withinEspRange"], _["Position"]
                        end
                    elseif j <= 0xed then
                        if j > 235 then
                            j, l = 419 - j, c
                        else
                            return
                        end
                    else
                        j, k = 0x154 - j, h[1][1][h[1][2]]
                        g, u, v = k["drawEspAt"], "egg_", f["Uid"]
                        u, k, v, b = _["Position"], u .. v, i, h[1][1][h[1][2]]
                        e, b = b["espColorFor"], t
                    end
                elseif j <= 0xaf then
                    if j <= 0xa5 then
                        if j >= 0x91 then
                            if j <= 0x91 then
                                j, m = 166 - j, not c
                            else
                                j, t = 0x130 - j, "Carried"
                                l = r == t
                            end
                        else
                            j = l and j + 98 or 0xb6
                        end
                    elseif j > 0xad then
                        c = c(m)
                        m = not d
                        j = m and 0x631f / j or j + -0x9a
                    else
                        i = h[1][1][h[1][2]]
                        j, t, i = j + -0x31, i["resolveRarity"], f["AssetCategory"]
                    end
                elseif j < 0xc9 then
                    if j > 0xb6 then
                        j, l = 0x3c38 / j, d
                    else
                        t = l
                        j = t and 0xfd or 0xdf
                    end
                elseif j <= 0xc9 then
                    t = "Dropped"
                    l = r == t
                    j = l and 0x154 - j or 0x16e - j
                else
                    _ = f["BottomCFrame"]
                    j = _ and j + -0x7f or 18
                end
            elseif j < 0x57 then
                if j <= 31 then
                    if j >= 27 then
                        if j <= 28 then
                            if j > 27 then
                                j, v = 0x2f4 / j, s.c(v(e))
                            else
                                g = g(k, u, s.d(v))
                                j, i = 240, g
                            end
                        else
                            return
                        end
                    elseif j <= 0x12 then
                        if j <= 5 then
                            j = j + 0x66
                        else
                            j, _ = 0x4c, f["BoundsCFrame"]
                        end
                    else
                        j = m and 0x1f or 0x7b
                    end
                elseif j <= 76 then
                    if j > 0x45 then
                        j = _ and 0x70 or j + 0x9b
                    elseif j > 57 then
                        i = i(g, k, s.d(u))
                        k = "Dropped"
                        g = r == k
                        j = g and 0x57 or j + 0x41
                    else
                        j, t = 0xdf, t(i)
                    end
                else
                    j = l and 0xb6 or 0xc9
                end
            elseif j >= 112 then
                if j < 0x7f then
                    if j <= 123 then
                        if j <= 112 then
                            t, r = "Slot", f["State"]
                            l = r == t
                            j = l and j + 0x4c or 194 - j
                        else
                            a, m = h[1][1][h[1][2]], s._["ipairs"]
                            j, n = 229, a["getAreaEggs"]
                        end
                    else
                        t = t(i)
                        j, g = 368 - j, s._["string"]
                        i, u, g = g["format"], h[1][1][h[1][2]], "%s [%s]"
                        u, k = f["AssetCategory"], u["assetName"]
                    end
                elseif j >= 0x86 then
                    if j <= 134 then
                        k = "Carried"
                        j, g = 0xdd - j, r == k
                    else
                        j, d = 175, d(c)
                        m = h[1][1][h[1][2]]
                        m, c = "EspCarriedEggs", m["isOn"]
                    end
                else
                    j, c = 0x87, h[1][1][h[1][2]]
                    d, c = c["isOn"], "EspWorldEggs"
                end
            elseif j <= 97 then
                if j > 0x5f then
                    j = 0xe7
                    g(k, u, v, e, b)
                elseif j > 87 then
                    m, n, a = m(s.d(n))
                    m, n, a = s.b(m, n, a)
                    p, f = m(n, a)
                    a = p
                    j = a == nil and j + 140 or 298 - j
                else
                    j = g and 307 - j or 240
                end
            elseif j <= 0x64 then
                e = e(b)
                j, b = 0x61, nil
            else
                j, u = 0x1cd7 / j, s.c(u(v))
            end
        until false
    end
end,
wa = function (s, h)
    return function ()
        local a, g, t, r, d, i, j, u, n, o, _, m, c, e, l, p, f, k
        j = 0xa6
        repeat
            if j > 166 then
                if j <= 0xd2 then
                    if j < 0xc8 then
                        if j <= 190 then
                            k = k(u, o)
                            c, u = k, s._["math"]
                            j, k, u, e = j + 2, u["min"], m, t["Position"]
                            o = e.Z
                            o = o - g
                        else
                            k = k(u, o)
                            m, u = k, s._["math"]
                            u, e, k = n, t["Position"], u["max"]
                            j, o = j + -0x23, e.Z
                            o = o + g
                        end
                    elseif j > 0xc9 then
                        j, p = 0x1c1 - j, h[1][1][h[1][2]]
                        a = p["getEntryPosition"]
                    elseif j <= 0xc8 then
                        j, t = 0x2a30 / j, h[1][1][h[1][2]]
                        t, l = r, t["getZoneModel"]
                    else
                        j, i, k, g = j + 0x19, t.IsA, "BasePart", t
                    end
                elseif j >= 0xf0 then
                    if j <= 240 then
                        _, r = a(p, f)
                        f = _
                        j = f == nil and 210 or 200
                    else
                        a, p, f = a(p)
                        a, p, f = s.b(a, p, f)
                        _, r = a(p, f)
                        f = _
                        j = f == nil and 210 or j + -0x36
                    end
                elseif j <= 0xe2 then
                    j, i = 0x2b42 / j, i(g, k)
                else
                    a = a()
                    f = s._["math"]
                    _, f, p, r = a.X, d, f["min"], 0x14
                    j, _ = 66, _ - r
                end
            elseif j <= 121 then
                if j <= 65 then
                    if j > 54 then
                        i = t
                        j = i and 0x3309 / j or 49
                    elseif j > 49 then
                        l = l(t)
                        t = l
                        j = t and 0x79 or 119 - j
                    elseif j <= 8 then
                        j, k = 190, k(u, o)
                        u, d = s._["math"], k
                        e, u, k = t["Position"], c, u["max"]
                        o = e.X
                        o = o + i
                    else
                        j = i and 128 or j + 191
                    end
                elseif j <= 0x42 then
                    p = p(f, _)
                    d = p
                    return d, c, m, n
                else
                    i, g, j, t = l, "Bounds", 0x4048 / j, l.FindFirstChild
                end
            elseif j > 0x9d then
                m = s._["math"]
                d, n = m["huge"], m
                j, m = 254, n["huge"]
                c, a = -m, n
                p, m = a, a["huge"]
                a = p["huge"]
                p, a, n = h[2][1][h[2][2]], s._["ipairs"], -a
            elseif j > 0x88 then
                j, k = 240, k(u, o)
                n = k
            elseif j <= 128 then
                k = t["Size"]
                g, k = k.X, 0.5
                i, j, u = g * k, 8, t["Size"]
                u, k = 0.5, u.Z
                g, u = k * u, s._["math"]
                e, u, k = t["Position"], d, u["min"]
                o = e.X
                o = o - i
            else
                j, t = 65, t(i, g)
            end
        until false
    end
end,
Gc = function (e, h)
    return function ()
        local f, i, a, c, b, _, k, d, g, j
        j = 49
        while true do
            if j <= 110 then
                if j >= 37 then
                    if j <= 0x32 then
                        if j >= 0x31 then
                            if j > 0x31 then
                                a = a(k, f)
                                i["AnchorPoint"] = a
                                j, k = 296 - j, e._["UDim2"]
                                k, f, a = 0.5, 0, k["new"]
                                _, g = k, 6
                            else
                                d = h[2][1][h[2][2]]
                                j = d and 150 or 0x22
                            end
                        elseif j <= 37 then
                            j = c and 0x378 / j or 0xbff / j
                        else
                            b = b(i, a)
                            c["Size"] = b
                            i = e._["Color3"]
                            i, j, b = 10, j + 131, i["fromRGB"]
                            k, a = 12, i
                        end
                    elseif j >= 93 then
                        if j > 0x5d then
                            i = i(a)
                            k = e._["Vector2"]
                            k, f, j, a = 0.5, 0, 0x32, k["new"]
                        else
                            j, c = j + 34, e._["gethui"]
                        end
                    else
                        j, c = 0x6b - j, h[1][1][h[1][2]]
                    end
                elseif j >= 0x18 then
                    if j <= 0x1b then
                        if j > 24 then
                            i = i(a, k)
                            b["Size"] = i
                            i = 1
                            b["BackgroundTransparency"] = i
                            k = e._["Enum"]
                            a = k["Font"]
                            i = a["GothamMedium"]
                            j, b["Font"] = 42 - j, i
                            i = 0x18
                            b["TextSize"] = i
                            a = e._["Color3"]
                            a, k, i, f = 226, 0xe6, a["fromRGB"], 0xee
                        else
                            j, d["Parent"] = 0x1500 / j, c
                            b = e._["Instance"]
                            b, c = "Frame", b["new"]
                        end
                    else
                        j = d and 0xfd or 0x1ba / j
                    end
                elseif j >= 13 then
                    if j <= 13 then
                        j, c = 0x659 / j, e._["Instance"]
                        c, d = "ScreenGui", c["new"]
                    else
                        i = i(a, k, f)
                        b["TextColor3"] = i
                        i = "MMB HUB"
                        b["Text"] = i
                        b["Parent"] = c
                        a = e._["Instance"]
                        j, a, i = 0x6e, "TextLabel", a["new"]
                    end
                else
                    j, i = 202, i(a, k)
                    b["AnchorPoint"] = i
                    a = e._["UDim2"]
                    a, i = 0.5, a["fromScale"]
                    k = a
                end
            elseif j >= 0x96 then
                if j > 224 then
                    if j > 0xf6 then
                        return
                    else
                        a = a(k, f, _, g)
                        i["Position"] = a
                        j, k = 0x6c96 / j, e._["UDim2"]
                        f, a, k = 0x16, k["fromOffset"], 0x190
                    end
                elseif j >= 0xca then
                    if j > 0xca then
                        c = c(b)
                        j, i = j + -0xb1, e._["UDim2"]
                        i, b = 1, i["fromScale"]
                        a = i
                    else
                        i = i(a, k)
                        b["Position"] = i
                        j, a = 0x1b, e._["UDim2"]
                        a, i, k = 400, a["fromOffset"], 30
                    end
                elseif j <= 0x96 then
                    c = h[2][1][h[2][2]]
                    j, d = j + -116, c["Parent"]
                else
                    b = b(i, a, k)
                    c["BackgroundColor3"] = b
                    b = 0
                    j, c["BorderSizePixel"] = 111, b
                    c["Parent"] = d
                    i = e._["Instance"]
                    b, i = i["new"], "TextLabel"
                end
            elseif j > 0x7a then
                if j > 0x7d then
                    j, c = 37, c()
                else
                    d = d(c)
                    c = "MMBRenderInfo"
                    d["Name"] = c
                    c = true
                    d["IgnoreGuiInset"] = c
                    c = false
                    d["ResetOnSpawn"] = c
                    c = 500
                    d["DisplayOrder"] = c
                    c = e._["gethui"]
                    j = c and 0xda - j or 37
                end
            elseif j < 0x71 then
                b = b(i)
                a = e._["Vector2"]
                a, j, i, k = 0.5, 114 - j, a["new"], 1
            elseif j > 0x71 then
                a = a(k, f, _)
                i["TextColor3"] = a
                a = "Made with <3 - MMB HUB"
                i["Text"] = a
                i["Parent"] = c
                h[2][1][h[2][2]] = d
                return
            else
                a = a(k, f)
                i["Size"] = a
                a = 1
                i["BackgroundTransparency"] = a
                f = e._["Enum"]
                k = f["Font"]
                a = k["Code"]
                i["Font"] = a
                a = 15
                i["TextSize"] = a
                j, k = j + 9, e._["Color3"]
                f, k, _, a = 200, 0x78, 150, k["fromRGB"]
            end
        end
    end
end,
pd = function (e, a)
    return function ()
        local c, d
        d, c = a[1][1][a[1][2]], false
        d["Anchored"] = c
        return
    end
end,
nd = function (e, a)
    return function ()
        local c, _, d, b
        _ = 0x95
        repeat
            if _ > 0x95 then
                d(c, b)
                return
            else
                _, c = 0xaf, a[2][1][a[2][2]]
                b, d = e:td{a[1]}, c["Completed"]
                c, d = d, d.Connect
            end
        until false
    end
end,
Od = function (e, a)
    return function ()
        local _, c, d
        _ = 20
        while true do
            if _ <= 20 then
                _, c = 27, e._["task"]
                c, d = e:de{a[1]}, c["spawn"]
            else
                d(c)
                return
            end
        end
    end
end,
se = function (e, g)
    return function ()
        local b, c, d, f, _
        _ = 134
        while true do
            if _ <= 120 then
                if _ >= 0x27 then
                    if _ > 39 then
                        d, b, f, _, c = e._["sethiddenproperty"], "GameplayPaused", false, _ + 73, g[1][1][g[1][2]]
                    else
                        return
                    end
                else
                    d, _, c = g[1][1][g[1][2]], _ + 21, false
                    d["GameplayPaused"] = c
                end
            elseif _ > 0x86 then
                _ = 0x27
                d(c, b, f)
            else
                d = e._["sethiddenproperty"]
                _ = d and 0x78 or 0x12
            end
        end
    end
end,
kc = function (e, h)
    return function (d)
        local m, a, _, g, f, n, c, b, j, k, l
        j = 151
        repeat
            if j >= 0x91 then
                if j >= 0xb0 then
                    if j < 0xe1 then
                        if j < 0xbc then
                            j, n = 0x77, n(a)
                        elseif j > 0xbc then
                            n, a, k = n(e.d(a))
                            n, a, k = e.b(n, a, k)
                            f, _ = n(a, k)
                            k = f
                            j = k == nil and 0x19a0 / j or 0x120 - j
                        else
                            j = k and 0xe3 - j or 0x3c38 / j
                        end
                    elseif j < 226 then
                        c = false
                        return c
                    elseif j <= 0xe2 then
                        j = c and 451 - j or 145
                    else
                        j = g and 158 or 88
                    end
                elseif j > 0x9e then
                    if j <= 0xa7 then
                        j, a = 205, e.c(a())
                    else
                        n = h[2][1][h[2][2]]
                        j, m = 226, n["RequestCarryAreaEgg"]
                        c = not m
                    end
                elseif j > 0x97 then
                    l = h[1][1][h[1][2]]
                    b, g, j, l = _["NestId"], l["BuildSlotKey"], 0x5c94 / j, _["AreaId"]
                elseif j >= 0x96 then
                    if j <= 0x96 then
                        g = g(l, b)
                        j, m[1][m[2]] = 0x20, g
                    else
                        c = not d
                        j = c and 226 or 0xab
                    end
                else
                    c = d["Name"]
                    c = {[2] = 3, [3] = c}
                    c[1] = c
                    m = nil
                    m = {[2] = 3, [3] = m}
                    m[1] = m
                    a = h[1][1][h[1][2]]
                    n = a["IsFirstAreaUid"]
                    j = n and 125 or j + -0x1a
                end
            elseif j > 0x52 then
                if j > 114 then
                    if j <= 119 then
                        j = n and j + -75 or 0x20
                    else
                        j, a = 301 - j, h[1][1][h[1][2]]
                        a, n = c[1][c[2]], a["IsFirstAreaUid"]
                    end
                elseif j > 88 then
                    n, a = n(a)
                    k = n
                    j = k and 14 or 302 - j
                elseif j <= 0x53 then
                    l = _["Uid"]
                    g = l == c[1][c[2]]
                    j = g and 0x6cf / j or j + 160
                else
                    f, _ = n(a, k)
                    k = f
                    j = k == nil and 0x20 or 83
                end
            elseif j >= 0x27 then
                if j < 44 then
                    k = true
                    return k
                elseif j <= 0x2c then
                    j, n, k = j + 123, e._["ipairs"], h[4][1][h[4][2]]
                    a = k["getAreaEggs"]
                else
                    k = h[3][1][h[3][2]]
                    return k
                end
            elseif j < 0x15 then
                f = true
                j, k = 202 - j, a == f
            elseif j <= 21 then
                l = h[1][1][h[1][2]]
                j, g = 0x13ef / j, l["BuildSlotKey"]
            else
                a, j, n = e:Ve{c, h[2], m}, 0x72, e._["pcall"]
            end
        until false
    end
end,
Lf = {}, Nd = function (e, h)
    return function ()
        local d, a, b, c, i, _
        _ = 182
        repeat
            if _ > 0x6f then
                c = h[2][1][h[2][2]]
                d, b = c["copyText"], e._["string"]
                a, b, c = e._["game"], "game:GetService(\"TeleportService\"):TeleportToPlaceInstance(%d, \"%s\", game:GetService(\"Players\").LocalPlayer)", b["format"]
                i, _, a = a["PlaceId"], 0x6f, h[1][1][h[1][2]]
            elseif _ <= 62 then
                d(c, b)
                return
            else
                c = c(b, i, a)
                _, b = 62, "Copied join script"
            end
        until false
    end
end,
mb = function (e, h)
    return function ()
        local j, i, g, c, b, a, d, f
        j = 210
        repeat
            if j > 101 then
                if j >= 0xd2 then
                    if j > 210 then
                        b, d, c = h[1][1][h[1][2]], e._["ipairs"], e._["getconnections"]
                        j, b = 176, b["Idled"]
                    else
                        c = e._["getconnections"]
                        d = not c
                        j = d and 0x29 or 224
                    end
                elseif j <= 153 then
                    a = {[2] = 3, [3] = a}
                    a[1] = a
                    j, g, f = j + -116, e._["pcall"], e:ve{a}
                else
                    j, c = j + -77, e.c(c(b))
                end
            elseif j < 0x3b then
                if j > 37 then
                    return
                else
                    j = 0x887 / j
                    g(f)
                end
            elseif j > 0x63 then
                return
            elseif j <= 59 then
                i, a = d(c, b)
                b = i
                j = b == nil and 0x65 or 0x99
            else
                d, c, b = d(e.d(c))
                d, c, b = e.b(d, c, b)
                i, a = d(c, b)
                b = i
                j = b == nil and 0x65 or 0x99
            end
        until false
    end
end,
jb = function (s, h)
    return function ()
        local g, k, o, i, u, n, j, p, _, t, c, l, a, b, f, r, e, m, d
        j = 0x5c
        while true do
            if j < 0x5b then
                if j <= 33 then
                    if j > 0x17 then
                        if j >= 0x20 then
                            if j > 32 then
                                c, m, n = c(s.d(m))
                                c, m, n = s.b(c, m, n)
                                a, p = c(m, n)
                                n = a
                                j = n == nil and 0xf5 or 0x69
                            else
                                k, j, g, i = l, 0x740 / j, s._["tostring"], "User "
                            end
                        elseif j <= 0x18 then
                            j, f, r, _ = 174, p[1][p[2]].FindFirstChild, "CenterPoint", p[1][p[2]]
                        else
                            k = k(u, o, e)
                            o = s._["Color3"]
                            b, e, j, o, u = 0xff, 170, 0xfc - j, 0xc8, o["fromRGB"]
                        end
                    elseif j < 11 then
                        if j > 2 then
                            d = d(c, m)
                            c = not d
                            j = c and j + 200 or 177 - j
                        else
                            i = h[2][1][h[2][2]]
                            t, g, k = i["drawEspAt"], "plot_", p[1][p[2]]["Name"]
                            i, g, u = g .. k, f["Position"], s._["string"]
                            j, o, e, k, u = 0x1f, p[1][p[2]]["Name"], r, u["format"], "Plot %s\n%s"
                        end
                    elseif j < 0x12 then
                        r, i = t["DisplayName"], h[4][1][h[4][2]]
                        j = t == i and 0x969 / j or 2
                    elseif j <= 18 then
                        _ = nil
                        _ = {[2] = 3, [3] = _}
                        j, _[1] = 155, _
                        r, l = s._["pcall"], s:qe{_, h[5], p}
                    else
                        g, j, t = l, 0xef, h[3][1][h[3][2]]
                        i, t = t, t.GetPlayerByUserId
                    end
                elseif j > 0x3f then
                    if j > 84 then
                        r = h[2][1][h[2][2]]
                        _, j, r = r["withinEspRange"], 0x1c8c / j, f["Position"]
                    elseif j <= 72 then
                        f = f(_, r)
                        j = f and 0xdc or 24
                    else
                        j, _ = 110, _(r)
                    end
                elseif j >= 51 then
                    if j > 0x3a then
                        j = 0x97
                        t(i, g, k, u, o)
                    elseif j > 0x33 then
                        j, g = 0x74 / j, g(k)
                        r = i .. g
                    else
                        l = l(t)
                        j = l and 0x17 or 2
                    end
                elseif j <= 40 then
                    return
                else
                    c = c(m)
                    d = not c
                    j = d and 0x28 or j + 90
                end
            elseif j <= 0xaa then
                if j > 119 then
                    if j < 0x9b then
                        if j > 133 then
                            a, p = c(m, n)
                            n = a
                            j = n == nil and 245 or 0x69
                        else
                            m, d = "Plots", h[1][1][h[1][2]]
                            j, d, c = 0x3a3 / j, d.FindFirstChild, d
                        end
                    elseif j > 0x9b then
                        n, m, j, c = d, d.GetChildren, 0x77, s._["ipairs"]
                    else
                        j = 0x1ee1 / j
                        r(l)
                        t, l, r = _[1][_[2]], s._["tonumber"], "Empty"
                    end
                elseif j <= 0x69 then
                    if j > 95 then
                        p = {[2] = 3, [3] = p}
                        j, p[1] = 0x48, p
                        f, _, r = p[1][p[2]].FindFirstChild, p[1][p[2]], "PlotSign"
                    elseif j > 0x5c then
                        j, _, r, l = j + -4, f.IsA, f, "BasePart"
                    elseif j <= 91 then
                        j, _ = 0x5994 / j, _(r, l)
                    else
                        m = h[2][1][h[2][2]]
                        j, c, m = 0x2b, m["isOn"], "EspPlots"
                    end
                elseif j <= 110 then
                    j = _ and 18 or 151
                else
                    j, m = 33, s.c(m(n))
                end
            elseif j < 221 then
                if j < 219 then
                    if j <= 174 then
                        j, f = j + 46, f(_, r)
                    else
                        return
                    end
                elseif j <= 0xdb then
                    i = " (You)"
                    j, r = 438 / j, r .. i
                else
                    _ = f
                    j = _ and j + -0x7d or j + 32
                end
            elseif j >= 245 then
                if j > 245 then
                    j = _ and 0x57 or j + -0x8e
                else
                    return
                end
            elseif j <= 221 then
                u = u(o, e, b)
                j, o = 63, nil
            else
                t = t(i, g)
                j = t and 0xa45 / j or 32
            end
        end
    end
end,
Re = function (e, g)
    return function ()
        local d, b, c, _
        _ = 67
        while true do
            if _ <= 0x43 then
                if _ <= 14 then
                    if _ <= 9 then
                        return d
                    else
                        b = g[1][1][g[1][2]]
                        _, c, b = _ + 0xc7, b["isOn"], "AutoReturn"
                    end
                else
                    c = g[2][1][g[2][2]]
                    d = not c
                    _ = d and 9 or 14
                end
            else
                c = c(b)
                _, d = 9, not c
            end
        end
    end
end,
Cc = function (e, g)
    return function ()
        local d, _, b, c
        _ = 0x4b
        while true do
            if _ < 0x4b then
                d(c)
                return
            else
                c = g[2][1][g[2][2]]
                d, b = c["netCall"], g[1][1][g[1][2]]
                _, c = 8, b["Index"]
                c = c["REQUEST_CLAIM_ALL"]
            end
        end
    end
end,
Nf = {}, qa = function (e, h)
    return function (d, c)
        local i, g, a, b, j
        j = 126
        while true do
            if j > 0x7e then
                b = e.c(b(i, a, g))
                return e.d(b)
            else
                i = h[1][1][h[1][2]]
                g, b, i, a = true, i["glideTo"], d, nil
                j, g = 181, c == g
            end
        end
    end
end,
ya = function (e, h)
    return function (d, c, b, i)
        local a, _, k, j, f
        j = 35
        repeat
            if j > 88 then
                if j > 163 then
                    f["Duration"] = _
                    k, j, a = a, 268 - j, a.Push
                else
                    j, _ = 0x58, "Info"
                end
            elseif j < 0x45 then
                if j > 0x23 then
                    a(k, f)
                    return
                else
                    k = h[1][1][h[1][2]]
                    a, f = k["Notify"], {}
                    f["Title"] = d
                    f["Content"] = c
                    _ = b
                    j = _ and 0x58 or 0xa3
                end
            elseif j <= 69 then
                j, _ = 0x12d - j, 3
            else
                f["Variant"] = _
                _ = i
                j = _ and 0xe8 or 69
            end
        until false
    end
end,
kb = function (e, h)
    return function (d, ...)
        local f, c, b, _
        _ = 0xec
        while true do
            if _ <= 151 then
                if _ >= 0x5c then
                    if _ < 0x8d then
                        _, c = 143 - _, c(b, f)
                    elseif _ <= 0x8d then
                        b = b(f)
                        f = "Instance"
                        c = b == f
                        _ = c and 0x5e2f / _ or 192 - _
                    else
                        b, _, c, f = e:re{d}, 0xc9, e._["pcall"], e.c(...)
                    end
                elseif _ <= 51 then
                    _ = c and _ + 100 or 89
                else
                    _, b = 0x415c / _, h[1][1][h[1][2]]
                    f, b, c = e.c(...), d[1][d[2]], b["netInvoke"]
                end
            elseif _ <= 0xc9 then
                if _ <= 0xbc then
                    if _ > 0xab then
                        c = e.c(c(b, e.d(f)))
                        return e.d(c)
                    else
                        _, b, c, f = 0x107 - _, d[1][d[2]], d[1][d[2]].IsA, "RemoteEvent"
                    end
                else
                    c = e.c(c(b, e.d(f)))
                    return e.d(c)
                end
            else
                d = {[2] = 3, [3] = d}
                d[1] = d
                _, b, f = 0x8d, e._["typeof"], d[1][d[2]]
            end
        end
    end
end,
Mf = function (a, b, c, d)
    a.Lf[d] = a.gf(b, c)
    return a.Lf[d]
end,
J = function (e, h)
    return function ()
        local d, a, g, b, i, _, c
        _ = 251
        repeat
            if _ > 200 then
                if _ < 461 then
                    if _ > 250 then
                        if _ > 0x18e then
                            if _ < 434 then
                                if _ >= 412 then
                                    if _ <= 422 then
                                        if _ > 412 then
                                            _, i = 0x36a - _, e.c(i(a, g))
                                        else
                                            _, i = 0x392, e.c(i(a, g))
                                        end
                                    else
                                        _ = 468 - _
                                        d(c)
                                    end
                                elseif _ > 408 then
                                    d = d(c, b)
                                    _ = d and 9 or 20
                                elseif _ <= 0x192 then
                                    d = d(c)
                                    _ = d and 105 or 0x73
                                else
                                    _, d = 247, d(c)
                                end
                            elseif _ > 0x1c4 then
                                if _ <= 0x1c6 then
                                    _ = 0x74
                                    d(c)
                                else
                                    d = d(c)
                                    _ = d and 0xab or 0x2ab - _
                                end
                            elseif _ <= 0x1b9 then
                                if _ < 440 then
                                    d = d(c)
                                    _ = d and 11 or 0x1b6 - _
                                elseif _ <= 440 then
                                    _ = 0x89
                                    c(b)
                                else
                                    d = d(c, b)
                                    _ = d and 0xa035 / _ or 0x22d - _
                                end
                            else
                                b = b(e.d(i))
                                _ = b and 0x27e - _ or 0x20
                            end
                        elseif _ <= 0x14a then
                            if _ >= 0x140 then
                                if _ > 328 then
                                    d = d(c, b)
                                    _ = d and 0xbd or 0x9a
                                elseif _ > 322 then
                                    d = d(c)
                                    c = h[0x10][1][h[0x10][2]]
                                    _ = d ~= c and 0x7498 / _ or 0xef
                                elseif _ > 320 then
                                    d = d(c, b)
                                    _ = d and 0x6c2c / _ or 453 - _
                                else
                                    _ = 0x28
                                    b(i)
                                end
                            elseif _ > 261 then
                                b = b(i)
                                c = not b
                                _ = c and 0xeefc / _ or _ + -205
                            elseif _ > 255 then
                                _ = _ + -58
                                d(c)
                            elseif _ <= 251 then
                                c = h[12][1][h[12][2]]
                                d = not c
                                _ = d and 180 or 0x34
                            else
                                c, d = h[3][1][h[3][2]], e._["pcall"]
                                _, c = 398, c["runAutoClaimGroupReward"]
                            end
                        elseif _ < 348 then
                            if _ < 339 then
                                d = d(c)
                                _ = d and 0xd9 or 0x65
                            elseif _ > 339 then
                                d = d(c)
                                _ = d and 0xc6 or 0x3b
                            else
                                c = c(b)
                                _ = c and 0x18b - _ or 89
                            end
                        elseif _ <= 374 then
                            if _ > 348 then
                                c = c(b)
                                _ = c and 21 or 0x20a - _
                            else
                                d(c)
                                _, c = 0x8e, h[3][1][h[3][2]]
                                c = c["runWebhookSummary"]
                            end
                        else
                            _ = 0x136f0 / _
                            d(c)
                        end
                    elseif _ > 0xe4 then
                        if _ < 0xef then
                            if _ > 233 then
                                if _ <= 234 then
                                    _, d = 411 - _, d(c)
                                else
                                    i, _, b = e:ed{h[2], h[10], h[4]}, 0x140, e._["pcall"]
                                end
                            elseif _ < 232 then
                                if _ > 230 then
                                    _, c = 0x2b164 / _, h[3][1][h[3][2]]
                                    c, d = "EspPlayers", c["isOn"]
                                else
                                    c, b = e._["pcall"], h[3][1][h[3][2]]
                                    _, b = 0xaa, b["stopTreadmillTraining"]
                                end
                            elseif _ <= 0xe8 then
                                _ = d and 0x5c70 / _ or 0x83
                            else
                                c = h[9][1][h[9][2]]
                                _, d = 0xde, not c
                            end
                        elseif _ < 243 then
                            if _ <= 241 then
                                if _ <= 0xef then
                                    b = h[3][1][h[3][2]]
                                    _, c, b = 374, b["isOn"], "WalkSpeedEnabled"
                                else
                                    b, d = "RobloxPromptGui", h[11][1][h[11][2]]
                                    c, _, d = d, 0x360, d.FindFirstChild
                                end
                            else
                                d(c)
                                _, d = _ + 1, false
                                h[13][1][h[13][2]] = d
                            end
                        elseif _ < 248 then
                            if _ <= 0xf3 then
                                a, _, c, d, b = h[3][1][h[3][2]], 0x19c, "sellPets", h[1][1][h[1][2]], e._["tonumber"]
                                a, i, g = "SellInterval", a["optionValue"], 6
                            else
                                _ = d and 370 - _ or 250
                            end
                        elseif _ > 0xf8 then
                            c, _, b = e._["next"], 0x1dc90 / _, h[8][1][h[8][2]]
                        else
                            d, _, c = e._["pcall"], _ + 0x64, h[3][1][h[3][2]]
                            c = c["trackWebhookEvents"]
                        end
                    elseif _ <= 0xda then
                        if _ <= 0xd3 then
                            if _ > 0xce then
                                if _ > 209 then
                                    _, c = _ + -2, h[9][1][h[9][2]]
                                    d = not c
                                else
                                    _ = d and 0x9f33 / _ or 412 - _
                                end
                            elseif _ >= 0xcb then
                                if _ <= 203 then
                                    _, c = 0x9e, h[3][1][h[3][2]]
                                    d, c = c["isOn"], "AutoBuyTrail"
                                else
                                    _, a = 461, h[3][1][h[3][2]]
                                    i, a = a["handleDisconnect"], "Roblox error prompt"
                                end
                            else
                                _, i = 0x2eb78 / _, e.c(i(a, g))
                            end
                        elseif _ > 217 then
                            _, d = 0x23f, h[14][1][h[14][2]]
                        elseif _ <= 216 then
                            _ = d and 233 - _ or 252 - _
                        else
                            c = h[13][1][h[13][2]]
                            _, d = 0x13e - _, not c
                        end
                    elseif _ >= 224 then
                        if _ <= 0xe2 then
                            if _ > 224 then
                                c = h[3][1][h[3][2]]
                                _, c, d = 402, "AutoEquipBestGear", c["isOn"]
                            else
                                _, b = 0x1b740 / _, true
                                c["UseJumpPower"] = b
                                b, a = e._["tonumber"], h[3][1][h[3][2]]
                                i, g, a = a["optionValue"], 0x32, "JumpPower"
                            end
                        else
                            c = h[3][1][h[3][2]]
                            _, c, d = _ + 6, "EspGuards", c["isOn"]
                        end
                    elseif _ > 0xde then
                        _, c = 0x40, h[13][1][h[13][2]]
                        d = not c
                    elseif _ <= 0xdb then
                        b, a, c, _, d = e._["tonumber"], h[3][1][h[3][2]], "fuse", 0x1aa06 / _, h[1][1][h[1][2]]
                        i, g, a = a["optionValue"], 8, "FuseInterval"
                    else
                        _ = d and _ + -0xcb or 354 - _
                    end
                elseif _ >= 0x2a3 then
                    if _ > 0x360 then
                        if _ <= 0x3ac then
                            if _ <= 0x392 then
                                if _ > 0x37e then
                                    b = b(e.d(i))
                                    _ = b and 0x404 - _ or 94
                                elseif _ < 0x36b then
                                    b = b(e.d(i))
                                    _ = b and 0x230e6 / _ or _ + -0x2b4
                                elseif _ > 0x36b then
                                    _ = _ + -0x30b
                                    d(c)
                                else
                                    _ = _ + -0x290
                                    d(c)
                                end
                            elseif _ > 0x3a6 then
                                d = d(c)
                                _ = d and 0x306c4 / _ or _ + -0x2db
                            elseif _ <= 0x39f then
                                _, d = 122, d(c)
                            else
                                d = d(c)
                                _ = d and 0x4b or 0x3f5 - _
                            end
                        elseif _ > 0x3f6 then
                            if _ > 0x3f8 then
                                d = d(c, b)
                                _ = d and 0x8c or 0xc8
                            else
                                d = d(c, b)
                                _ = d and 192 or _ + -0x374
                            end
                        elseif _ <= 0x3e5 then
                            if _ > 0x3b8 then
                                _, c = 0xb6, c(b, i)
                            elseif _ <= 0x3b6 then
                                _ = 0xe2
                                d(c)
                            else
                                b = b(e.d(i))
                                _ = b and 0x57 or 0x45
                            end
                        else
                            d = d(c, b)
                            _ = d and _ + -0x3dd or 0xdb
                        end
                    elseif _ >= 0x30a then
                        if _ <= 0x337 then
                            if _ < 0x32e then
                                if _ > 0x30a then
                                    d = d(c)
                                    _ = d and 48 or 40
                                else
                                    d = d(c, b)
                                    _ = d and 0x36c - _ or 243
                                end
                            elseif _ <= 0x32e then
                                d = d(c)
                                _ = d and 0x1fcc0 / _ or 0x2aed0 / _
                            else
                                _ = 137
                                c(b)
                            end
                        elseif _ < 0x355 then
                            _, i = 0x5c8 - _, i(a)
                            a, g, i = i, "ErrorPrompt", i.find
                        elseif _ <= 0x355 then
                            _, d = 0x1a3d6 / _, d(c)
                        else
                            d = d(c, b)
                            c = d
                            _ = c and _ + -0x2d3 or 0x26640 / _
                        end
                    elseif _ <= 0x2d4 then
                        if _ > 0x2bb then
                            b = b(e.d(i))
                            _ = b and 16 or 0x47
                        elseif _ >= 0x2b9 then
                            if _ > 0x2b9 then
                                _ = _ + -0x262
                                c(b)
                            else
                                c = c()
                                _ = c and 145 or 0x192f4 / _
                            end
                        else
                            _, c = 0x48, c()
                        end
                    elseif _ >= 0x2fc then
                        if _ <= 0x2fc then
                            _, d = 0x195e0 / _, d(c)
                        else
                            _ = 239
                            c(b)
                        end
                    else
                        _, b = 0x390 - _, b(i, a)
                    end
                elseif _ >= 0x21c then
                    if _ < 0x23e then
                        if _ < 0x232 then
                            if _ <= 0x221 then
                                if _ > 0x21c then
                                    d = d(c, b)
                                    _ = d and 218 or 89
                                else
                                    c = c()
                                    _ = c and 224 or 0xbc
                                end
                            else
                                d = d(c, b)
                                _ = d and 76 or 0x14082 / _
                            end
                        elseif _ >= 0x239 then
                            if _ <= 0x239 then
                                d = d(c)
                                _ = d and 0xff or 0xc8
                            else
                                _ = 0x83
                                d(c)
                            end
                        else
                            d = d(c)
                            _ = d and 0x1e98e / _ or 0x8c80 / _
                        end
                    elseif _ >= 0x27e then
                        if _ < 0x285 then
                            if _ > 0x27e then
                                _ = _ + -0x26d
                                d(c)
                            else
                                d = d(c)
                                _ = d and 0xaf or _ + -0x264
                            end
                        elseif _ > 0x285 then
                            _, i = 0x311 - _, i(a, g)
                        else
                            c = c()
                            _, b = 0x21a, h[15][1][h[15][2]]
                            d, b = c - b, e._["tick"]
                        end
                    elseif _ > 0x23f then
                        d = d(c)
                        _ = d and _ + -0x24e or _ + -0x232
                    elseif _ <= 0x23e then
                        c = c(b)
                        _ = c and 0x55 or 188
                    else
                        d()
                        c = h[3][1][h[3][2]]
                        _, c, d = 0x148, "NoClip", c["isOn"]
                    end
                elseif _ < 488 then
                    if _ > 0x1e1 then
                        if _ <= 0x1e2 then
                            d(c)
                            _, d = 0xf888 / _, false
                            h[13][1][h[13][2]] = d
                        else
                            d = d(c)
                            _ = d and 248 or 150
                        end
                    elseif _ <= 465 then
                        if _ < 464 then
                            _ = 0x9a
                            i(a)
                        elseif _ <= 0x1d0 then
                            _, d = _ + -0x121, d(c)
                        else
                            d = d(c)
                            _ = d and 149 or 0x27f - _
                        end
                    else
                        _, d = 0x2b37 / _, d(c)
                    end
                elseif _ > 0x1f6 then
                    if _ > 0x210 then
                        b = b()
                        i = h[4][1][h[4][2]]
                        i, c = 300, b - i
                        b = d >= i
                        _ = b and _ + -404 or 107
                    elseif _ <= 0x208 then
                        _ = 79
                        d(c)
                    else
                        d = d(c, b)
                        _ = d and _ + -0x1e9 or _ + -391
                    end
                elseif _ > 0x1f2 then
                    _, i = 0x2d4, e.c(i(a, g))
                elseif _ >= 0x1eb then
                    if _ <= 491 then
                        b = b(i, a)
                        _ = b and 0xbb or _ + -0x1b1
                    else
                        _, i = 0x361, e.c(i(a, g))
                    end
                else
                    c = c(b)
                    b = nil
                    _ = c ~= b and 0x227 - _ or _ + -351
                end
            elseif _ >= 107 then
                if _ > 0x98 then
                    if _ >= 181 then
                        if _ < 189 then
                            if _ <= 0xba then
                                if _ < 0xb8 then
                                    if _ > 181 then
                                        _ = c and 37 or 0x150 - _
                                    else
                                        _ = 174
                                        d(c)
                                    end
                                elseif _ <= 184 then
                                    _, i = _ + -0x38, 300
                                    b = c >= i
                                else
                                    _, c["WalkSpeed"] = 0x94, b
                                end
                            elseif _ <= 0xbb then
                                i = b
                                _ = i and 110 or 124
                            else
                                c = h[17][1][h[17][2]]
                                _ = c and 260 - _ or 0x8a
                            end
                        elseif _ <= 196 then
                            if _ <= 0xc3 then
                                if _ < 192 then
                                    c = h[3][1][h[3][2]]
                                    d, _, c = c["isOn"], _ + 0x26b, "AntiAfk"
                                elseif _ <= 192 then
                                    c = h[3][1][h[3][2]]
                                    _, c, d = _ + 0x172, "AutoSellEggs", c["isOn"]
                                else
                                    c, d = h[3][1][h[3][2]], e._["pcall"]
                                    _, c = 261, c["runAutoUpgrades"]
                                end
                            else
                                _, b, d, c = 0x2e5 - _, 2, h[1][1][h[1][2]], "dashboard"
                            end
                        elseif _ < 0xc6 then
                            d = d(c)
                            _ = d and 30 or 219
                        elseif _ > 0xc6 then
                            _, b, d, c = 0x1b9, 3, h[1][1][h[1][2]], "hop"
                        else
                            c = h[13][1][h[13][2]]
                            _, d = 0x3b, not c
                        end
                    elseif _ >= 170 then
                        if _ <= 174 then
                            if _ < 173 then
                                if _ > 170 then
                                    _, d, c = 0x3b6, e._["pcall"], h[3][1][h[3][2]]
                                    c = c["runAutoEquipBestTrail"]
                                else
                                    _ = 231 - _
                                    c(b)
                                end
                            elseif _ > 173 then
                                c = h[3][1][h[3][2]]
                                c, _, d = "AutoClaimGroupReward", 0x239, c["isOn"]
                            else
                                _, b = 0x702e / _, 8
                            end
                        elseif _ <= 0xb1 then
                            if _ > 175 then
                                _ = d and 0x571e / _ or 34
                            else
                                _ = d and 0xb1 or 228
                            end
                        else
                            return
                        end
                    elseif _ >= 0x9e then
                        if _ <= 160 then
                            if _ > 0x9e then
                                _, c = 216, h[13][1][h[13][2]]
                                d = not c
                            else
                                d = d(c)
                                _ = d and 133 or 185 - _
                            end
                        else
                            _ = 0x30a
                        end
                    elseif _ < 154 then
                        c = h[9][1][h[9][2]]
                        _, d = 0x181 - _, not c
                    elseif _ <= 0x9a then
                        return
                    else
                        _ = d and _ + -87 or _ + 88
                    end
                elseif _ < 132 then
                    if _ > 0x7b then
                        if _ < 0x80 then
                            if _ < 125 then
                                _ = i and 0x49a0 / _ or 253 - _
                            elseif _ <= 125 then
                                _, c = 0x41c - _, h[3][1][h[3][2]]
                                c, d = "EspMachines", c["isOn"]
                            else
                                _ = d and 0x42f0 / _ or _ + 0x69
                            end
                        elseif _ >= 129 then
                            if _ > 0x81 then
                                d, c, _, b, a = h[1][1][h[1][2]], "sellEggs", 201, e._["tonumber"], h[3][1][h[3][2]]
                                a, i, g = "SellEggInterval", a["optionValue"], 8
                            else
                                _ = i and 206 or _ + 25
                            end
                        else
                            _ = b and 0xec or 0x28
                        end
                    elseif _ >= 0x74 then
                        if _ <= 0x7a then
                            if _ <= 117 then
                                if _ > 0x74 then
                                    _, c = 0x9b, h[9][1][h[9][2]]
                                    d = not c
                                else
                                    _, d, b, c = 0xf7dc / _, h[1][1][h[1][2]], 5, "webhook"
                                end
                            else
                                _ = d and 0xf7 or _ + -41
                            end
                        else
                            _, b, c = 440, h[3][1][h[3][2]], e._["pcall"]
                            b = b["runEsp"]
                        end
                    elseif _ < 0x72 then
                        if _ > 0x6b then
                            _, i = 0x3548 / _, b["Visible"]
                        else
                            _ = b and 0x80 or 73
                        end
                    elseif _ <= 0x72 then
                        _ = 0x1b4 - _
                    else
                        _, c = 0xc5, h[3][1][h[3][2]]
                        d, c = c["isOn"], "AutoDeleteOwnPets"
                    end
                elseif _ <= 141 then
                    if _ < 137 then
                        if _ > 0x86 then
                            _ = d and _ + -14 or 125
                        elseif _ > 0x85 then
                            i = 60
                            _, b = 0x6b, c >= i
                        elseif _ > 132 then
                            c = h[9][1][h[9][2]]
                            _, d = 0xe07 / _, not c
                        else
                            b, c, _, d = 4, "upgrades", 0x19a, h[1][1][h[1][2]]
                        end
                    elseif _ <= 0x8c then
                        if _ > 0x8a then
                            c = h[3][1][h[3][2]]
                            _, d, c = 0x3a6, c["isOn"], "AutoClaimIndex"
                        elseif _ <= 137 then
                            c, _, b, d = "pets", _ + 0x36d, 5, h[1][1][h[1][2]]
                        else
                            b = h[3][1][h[3][2]]
                            _, c = 0x2a3, b["isDoubleSpeedVisible"]
                        end
                    else
                        c, _, b, i = d.FindFirstChild, 0x472 - _, d, "promptOverlay"
                    end
                elseif _ >= 0x95 then
                    if _ <= 150 then
                        if _ <= 0x95 then
                            d, c = e._["pcall"], h[3][1][h[3][2]]
                            _, c = 0xb5, c["runClaimOfflineEarnings"]
                        else
                            d, _, b, c = h[1][1][h[1][2]], 0xc15c / _, 4, "session"
                        end
                    else
                        i, _, a = e._["tostring"], _ + 0x2a0, b["Name"]
                    end
                elseif _ > 0x91 then
                    b = h[3][1][h[3][2]]
                    c, _, b = b["isOn"], 0x23e, "JumpPowerEnabled"
                elseif _ > 142 then
                    a, b = h[3][1][h[3][2]], e._["tonumber"]
                    _, i, a, g = 0x237 - _, a["optionValue"], "WalkSpeed", 32
                else
                    _ = 0x5334 / _
                    d(c)
                end
            elseif _ >= 58 then
                if _ <= 79 then
                    if _ < 0x46 then
                        if _ <= 0x3f then
                            if _ >= 61 then
                                if _ > 61 then
                                    b, c = h[3][1][h[3][2]], e._["pcall"]
                                    _, b = 0x337, b["clearAllEsp"]
                                else
                                    b = h[3][1][h[3][2]]
                                    b, _, c = "AntiGameplayPause", 339, b["isOn"]
                                end
                            elseif _ > 0x3a then
                                _ = d and 117 or 155
                            else
                                _, b, a, i = 0x2d5, c.FindFirstChildWhichIsA, "Frame", c
                            end
                        elseif _ > 68 then
                            _, b = 0x1773 / _, 8
                        elseif _ > 0x40 then
                            d = true
                            d, h[13][1][h[13][2]], _, c = e._["pcall"], d, 0x4048 / _, h[3][1][h[3][2]]
                            c = c["runAutoFusePets"]
                        else
                            _ = d and 233 or 0x3780 / _
                        end
                    elseif _ <= 0x49 then
                        if _ > 0x48 then
                            i = 300
                            b = d < i
                            _ = b and 0x101 - _ or _ + 55
                        elseif _ > 0x47 then
                            _ = c and 6 or 61
                        elseif _ > 70 then
                            _, b = 0x470 / _, 50
                        else
                            c = e._["task"]
                            _, d, c = 0xdac / _, c["spawn"], e:fd{h[7], h[3], h[6]}
                        end
                    elseif _ > 0x4c then
                        c = h[3][1][h[3][2]]
                        d, _, c = c["isOn"], 0x1d1, "AutoClaimOffline"
                    elseif _ > 0x4b then
                        _, c = 0x9048 / _, h[3][1][h[3][2]]
                        d, c = c["isOn"], "WebhookEnabled"
                    else
                        d, c = e._["pcall"], h[3][1][h[3][2]]
                        _, c = 0x253 - _, c["runAutoClaimIndex"]
                    end
                elseif _ <= 93 then
                    if _ >= 0x57 then
                        if _ >= 0x5b then
                            if _ <= 0x5b then
                                c, _, h[16][1][h[0x10][2]], b = h[5][1][h[5][2]], 0x304, d, d
                            else
                                _, c = 0x1b2, h[3][1][h[3][2]]
                                c, d = "AutoServerHop", c["isOn"]
                            end
                        elseif _ > 0x57 then
                            c, d, _, b = "esp", h[1][1][h[1][2]], 0x210, 1.25
                        else
                            _ = 0x3f8
                        end
                    elseif _ > 85 then
                        _, c = _ + 0xfc, h[3][1][h[3][2]]
                        c, d = "AutoSellPets", c["isOn"]
                    elseif _ <= 81 then
                        c = h[3][1][h[3][2]]
                        c, _, d = "EspPlots", 0x198, c["isOn"]
                    else
                        _, b = _ + 0x1c7, h[3][1][h[3][2]]
                        c = b["getHumanoid"]
                    end
                elseif _ < 101 then
                    if _ < 96 then
                        _, b = 0x29dc / _, 6
                    elseif _ > 96 then
                        c = h[3][1][h[3][2]]
                        _, d, c = _ + 0xf3, c["isOn"], "AutoFusePets"
                    else
                        _, c, d = 0xaa40 / _, h[3][1][h[3][2]], e._["pcall"]
                        c = c["runServerHop"]
                    end
                elseif _ <= 0x66 then
                    if _ > 0x65 then
                        c, d = h[3][1][h[3][2]], e._["pcall"]
                        _, c = _ + 0x1d6, c["runAutoSellPets"]
                    else
                        _ = d and 0xfe - _ or 0x5b88 / _
                    end
                else
                    d, _, c = e._["pcall"], _ + 0x315, h[3][1][h[3][2]]
                    c = c["runAutoEquipBestGear"]
                end
            elseif _ > 27 then
                if _ <= 0x28 then
                    if _ >= 36 then
                        if _ > 39 then
                            _, c = 0x5fc8 / _, h[3][1][h[3][2]]
                            d, c = c["isOn"], "AutoReconnect"
                        elseif _ >= 0x25 then
                            if _ > 37 then
                                _, c = 0x2a5 - _, h[3][1][h[3][2]]
                                d, c = c["isOn"], "EspWorldEggs"
                            else
                                i, a, _, b = c, "ErrorPrompt", _ + 454, c.FindFirstChild
                            end
                        else
                            _, c = _ + 421, h[3][1][h[3][2]]
                            d, c = c["isOn"], "AutoEquipBestTrail"
                        end
                    elseif _ >= 32 then
                        if _ <= 32 then
                            _, b = _ + 0x9a, 0x20
                        else
                            _, c = 0x377 - _, h[3][1][h[3][2]]
                            c, d = "EspPets", c["isOn"]
                        end
                    else
                        c, d = h[3][1][h[3][2]], e._["pcall"]
                        _, c = 0x36b, c["deleteOwnPetRenders"]
                    end
                elseif _ > 51 then
                    if _ <= 52 then
                        _, c, b, d = 0x60 - _, "core", 0.35, h[1][1][h[1][2]]
                    else
                        b = h[3][1][h[3][2]]
                        _, b, c = 0x2bb, true, b["applyAntiGameplayPause"]
                    end
                elseif _ <= 0x32 then
                    if _ < 0x30 then
                        d = d(c, b)
                        _ = d and 0xc08 / _ or 0xf0 - _
                    elseif _ <= 0x30 then
                        _, c = _ + 0x255, e._["tick"]
                    else
                        _ = 196
                        d(c)
                    end
                else
                    c = h[3][1][h[3][2]]
                    c, _, d = "WebhookDisconnectAlerts", 0x1e1, c["isOn"]
                end
            elseif _ <= 19 then
                if _ > 11 then
                    if _ > 17 then
                        _, d = 482, true
                        h[13][1][h[13][2]], d, c = d, e._["pcall"], h[3][1][h[3][2]]
                        c = c["runAutoSellEggs"]
                    elseif _ > 16 then
                        d, c = e._["pcall"], h[3][1][h[3][2]]
                        _, c = 449 - _, c["runAutoEquipBest"]
                    else
                        _, c["JumpPower"] = 0xbc, b
                    end
                elseif _ < 6 then
                    if _ > 2 then
                        _ = d and 0x180 / _ or 0x78 - _
                    else
                        d, c = e._["pcall"], h[3][1][h[3][2]]
                        _, c = 0x502 / _, c["runAutoBuyTrail"]
                    end
                elseif _ > 9 then
                    c = h[13][1][h[13][2]]
                    _, d = 4, not c
                elseif _ <= 6 then
                    _, i = 266, h[3][1][h[3][2]]
                    i, b = "AutoTreadmill", i["isOn"]
                else
                    c = h[3][1][h[3][2]]
                    _, c, d = 0x3ac, "AutoUpgrades", c["isOn"]
                end
            elseif _ > 0x19 then
                if _ <= 0x1a then
                    _, c = 464, h[3][1][h[3][2]]
                    d, c = c["isOn"], "EspCarriedEggs"
                else
                    _ = d and 2 or 20
                end
            elseif _ <= 23 then
                if _ >= 21 then
                    if _ <= 21 then
                        b = h[3][1][h[3][2]]
                        _, c = 0x2b9, b["getHumanoid"]
                    else
                        _ = d and 0x15a7 / _ or 154
                    end
                else
                    _, b, c, d = 0x40d - _, 12, "claims", h[1][1][h[1][2]]
                end
            else
                _, c = 0x32e, h[3][1][h[3][2]]
                d, c = c["isOn"], "AutoEquipBest"
            end
        until false
    end
end,
Ya = function (e, h)
    return function (d, c)
        local _, g, a, l, j, f, b, k, m, n
        j = 168
        while true do
            if j < 0x94 then
                if j >= 91 then
                    if j <= 0x6c then
                        if j <= 101 then
                            if j <= 0x5b then
                                k(f, e.d(_))
                                return a
                            else
                                n = n()
                                j, k = 0xaf - j, {}
                                a, f = k, e._["math"]
                                k, f = f["abs"], d.Z
                                f = f - m
                            end
                        else
                            j, _ = j + 111, e.c(_(g, l, b))
                        end
                    else
                        j, _ = 0x19, e.c(_(g, l, b))
                    end
                elseif j >= 0x31 then
                    if j <= 49 then
                        j, _ = j + 0x2a, e.c(_(g, l, b))
                    else
                        k = k(f)
                        f = 3
                        j = k > f and 0x2bf0 / j or j + 0x74
                    end
                else
                    j = 190
                    k(f, e.d(_))
                end
            elseif j <= 0xbe then
                if j < 168 then
                    if j <= 148 then
                        k = k(f)
                        f = 2
                        j = k > f and 0x172 - j or 0x68a4 / j
                    else
                        j, f = 137, e._["table"]
                        f, k, g = a, f["insert"], e._["Vector3"]
                        g, b, l, _ = d.X, m, n, g["new"]
                    end
                elseif j < 181 then
                    j, n = 234, h[1][1][h[1][2]]
                    m = n["getLaneZ"]
                elseif j > 0xb5 then
                    f = e._["math"]
                    f, j, _, k = d.X, 0x94, c.X, f["abs"]
                    f = f - _
                else
                    f = e._["table"]
                    g, j, f, k = e._["Vector3"], 0x22a5 / j, a, f["insert"]
                    b, g, l, _ = c.Z, c.X, n, g["new"]
                end
            elseif j <= 222 then
                if j <= 219 then
                    j = 0x9ad7 / j
                    k(f, e.d(_))
                else
                    f = e._["table"]
                    j, g, f, k = 0x5da8 / j, e._["Vector3"], a, f["insert"]
                    b, l, _, g = m, n, g["new"], c.X
                end
            else
                m = m()
                a = n
                j, n = j + -133, a["getLaneY"]
            end
        end
    end
end,
ka = function (e, h)
    return function (d)
        local j, g, c, i, _, f, k, a, b
        j = 0x75
        while true do
            if j >= 152 then
                if j < 0xd7 then
                    if j <= 0xa7 then
                        if j > 0x9b then
                            b = e._["task"]
                            c, b, i = b["delay"], 2, h[1][1][h[1][2]]
                            j, i = 0x1b66 / j, i["rejoinServer"]
                        elseif j > 0x98 then
                            j, _ = 66, e.c(_(g))
                        else
                            return
                        end
                    else
                        j, b = 0xd9, h[1][1][h[1][2]]
                        b, c = "AutoReconnect", b["isOn"]
                    end
                elseif j <= 219 then
                    if j <= 0xd9 then
                        if j > 0xd7 then
                            c = c(b)
                            j = c and 167 or j + -161
                        else
                            b = h[1][1][h[1][2]]
                            k, f, i, c = {}, "Steal an Egg | MMB HUB", {}, b["sendWebhookEmbed"]
                            k["name"] = f
                            a = k
                            i["author"] = a
                            a = "Disconnected"
                            i["title"] = a
                            k = e._["string"]
                            _, a, k = h[3][1][h[3][2]], k["format"], "**Player** `%s`\n**Reason** %s"
                            f, g, _ = _["Name"], d, e._["tostring"]
                            j = g and j + -106 or 0xd9 - j
                        end
                    else
                        c = c(b)
                        j = c and 0xd7 or 0xca
                    end
                else
                    j, a = 0x34, a(k)
                    i["timestamp"] = a
                    i, b = true, i
                end
            elseif j <= 56 then
                if j <= 49 then
                    if j >= 0x2a then
                        if j <= 0x2a then
                            j = 0x930 / j
                            c(b, i)
                        else
                            c = true
                            h[2][1][h[2][2]], j, b = c, 0x29eb / j, h[1][1][h[1][2]]
                            b, c = "WebhookDisconnectAlerts", b["isOn"]
                        end
                    else
                        j, g = 111 - j, "Connection lost"
                    end
                elseif j <= 52 then
                    j = 0x2908 / j
                    c(b, i)
                else
                    return
                end
            elseif j > 109 then
                c = h[2][1][h[2][2]]
                j = c and 0x98 or 49
            elseif j > 0x42 then
                j = 155
            else
                a = a(k, f, e.d(_))
                i["description"] = a
                a = 0xe74c3c
                i["color"] = a
                j, f, k = j + 0xa6, "MMB HUB", {}
                k["text"] = f
                a = k
                i["footer"] = a
                k = e._["os"]
                k, a = "!%Y-%m-%dT%H:%M:%SZ", k["date"]
            end
        end
    end
end,
Ka = function (e, h)
    return function ()
        local _, b, c, d, f
        _ = 231
        repeat
            if _ >= 0xab then
                if _ >= 231 then
                    if _ >= 235 then
                        if _ > 235 then
                            _, b = 392 - _, b()
                            c, b = #b, 0
                            d = c > b
                        else
                            _, c = _ + -0xb6, c()
                            d = not c
                        end
                    else
                        _, c = 0x29, h[2][1][h[2][2]]
                        d = c["placingEnabled"]
                    end
                elseif _ > 0xab then
                    _ = d and _ + -185 or 0x35
                else
                    _, f = 0x1a9 - _, h[2][1][h[2][2]]
                    b = f["getUnplacedEggUids"]
                end
            elseif _ <= 41 then
                if _ >= 0x23 then
                    if _ > 35 then
                        d = d()
                        _ = d and _ + -6 or 246 - _
                    else
                        c = h[1][1][h[1][2]]
                        _, d = 0xcd, not c
                    end
                else
                    b = h[2][1][h[2][2]]
                    _, c = 0xeb, b["isPlotFull"]
                end
            elseif _ > 0x35 then
                return d
            else
                _ = d and 0xab or 191 - _
            end
        until false
    end
end,
zc = function (e, h)
    return function (d, c)
        local g, j, b, a, i
        j = 235
        while true do
            if j <= 0x80 then
                if j > 0x7f then
                    a = a(g)
                    i, a = a[c], true
                    b = i == a
                    return b
                elseif j <= 0x7e then
                    j, g = 0x80, h[1][1][h[1][2]]
                    g, a = d, g["multiSelected"]
                else
                    i = i(a)
                    b = not i
                    j = b and 156 or 0x7e
                end
            elseif j > 156 then
                j, a = 0x7f, h[1][1][h[1][2]]
                i, a = a["multiHasAny"], d
            else
                b = true
                return b
            end
        end
    end
end,
K = function (e, h)
    return function (d)
        local c, j, o, n, _, l, m, f, b, a, k
        j = 89
        while true do
            if j < 0x76 then
                if j < 80 then
                    if j >= 33 then
                        if j >= 0x28 then
                            if j > 0x28 then
                                j, n = 0x348 / j, true
                                m[c] = n
                            else
                                n, j, a = e._["pairs"], 0x78 - j, c
                            end
                        else
                            f, _ = n(a, k)
                            k = f
                            j = k == nil and 0x5f or 0xad
                        end
                    elseif j > 12 then
                        l = l(b)
                        b = "string"
                        j, o = j + 128, l == b
                    else
                        return m
                    end
                elseif j >= 0x59 then
                    if j >= 95 then
                        if j <= 0x5f then
                            return m
                        else
                            j, a = 0x5a3c / j, ""
                            n = c ~= a
                        end
                    else
                        m = h[1][1][h[1][2]]
                        n, j, c, m = {}, 143, m["getState"], d
                    end
                elseif j > 80 then
                    l = l(b)
                    b = "number"
                    o = l == b
                    j = o and 195 or 0x92
                else
                    n, a, k = n(a)
                    n, a, k = e.b(n, a, k)
                    f, _ = n(a, k)
                    k = f
                    j = k == nil and 0x1db0 / j or 0x3610 / j
                end
            elseif j > 205 then
                if j > 237 then
                    if j <= 241 then
                        j, a, k = 215, e._["typeof"], c
                    else
                        n = n(a)
                        a = "table"
                        j = n ~= a and 0xea69 / j or 40
                    end
                elseif j >= 0xd7 then
                    if j <= 0xd7 then
                        a = a(k)
                        k = "string"
                        n = a == k
                        j = n and 0x6e or 210
                    else
                        j, o = 270 - j, true
                        m[_] = o
                    end
                else
                    j = n and 0x46 or j + -0xc6
                end
            elseif j <= 0xad then
                if j <= 0x92 then
                    if j > 143 then
                        j = o and 237 or 0x21
                    elseif j <= 0x76 then
                        o = true
                        j, m[f] = j + -0x55, o
                    else
                        c = c(m, n)
                        n = {}
                        a, j, m, n = c, 0x188 - j, n, e._["typeof"]
                    end
                else
                    o = true
                    j = _ == o and 0x4fbe / j or 205
                end
            elseif j > 195 then
                b, j, l = f, 0x51, e._["typeof"]
            else
                l, j, b = e._["typeof"], 18, _
            end
        end
    end
end,
da = function (e)
    return function (d, c, b)
        local i, k, a, f
        a = {}
        a["name"] = d
        a["value"] = c
        f = false
        k = b ~= f
        a["inline"] = k
        i = a
        return i
    end
end,
C = function (e, h)
    return function (d, c)
        local a, i, _, b, g
        _ = 89
        repeat
            if _ < 0x7c then
                if _ <= 72 then
                    if _ <= 0x47 then
                        b = b(i, a)
                        _ = b and 211 or 196
                    else
                        b(i, a, g)
                        b = true
                        return b
                    end
                else
                    a, _, b = "RemoteFunction", 71, h[1][1][h[1][2]]
                    i, b = b, b.IsA
                end
            elseif _ < 0xc4 then
                b = e.c(b(i, a, g))
                return e.d(b)
            elseif _ <= 196 then
                a, g, b = d, c, h[1][1][h[1][2]]
                b, _, i = b.FireServer, 0x3720 / _, b
            else
                a, b, g = d, h[1][1][h[1][2]], c
                b, _, i = b.InvokeServer, 124, b
            end
        until false
    end
end,
ta = function (e, h)
    return function ()
        local d, b, c, f, _
        _ = 0x8e
        repeat
            if _ <= 199 then
                if _ < 142 then
                    if _ <= 0x3e then
                        _ = d and 0x83 or 250
                    else
                        f = h[1][1][h[1][2]]
                        _, b = 0x14a - _, f["eggInventoryCount"]
                    end
                elseif _ <= 142 then
                    d = h[2][1][h[2][2]]
                    _ = d and 217 or 0x3e
                else
                    b = b()
                    c = b >= d
                    return c
                end
            elseif _ < 0xe8 then
                c, d = h[2][1][h[2][2]], e._["tonumber"]
                _, c = 0x1c1 - _, c["MAX_INVENTORY"]
            elseif _ > 232 then
                _, c = 0x17d - _, e._["math"]
                d = c["huge"]
            else
                _, d = _ + -170, d(c)
            end
        until false
    end
end,
i = function (e)
    return function (d)
        local a, f, i, c, k, g, j, _, b
        j = 237
        repeat
            if j >= 0x70 then
                if j < 178 then
                    if j <= 114 then
                        if j <= 0x70 then
                            j, b = 75, e.c(b(i))
                        else
                            return
                        end
                    else
                        return
                    end
                elseif j <= 233 then
                    if j > 0xb2 then
                        j = 411 - j
                        f(_)
                    else
                        a, k = c(b, i)
                        i = a
                        j = i == nil and 326 - j or 0x34d8 / j
                    end
                else
                    c = not d
                    j = c and 0x72 or 0x17
                end
            elseif j >= 60 then
                if j <= 0x4b then
                    if j <= 60 then
                        f = f(_, g)
                        j = f and 0xc30 / j or j + 118
                    else
                        c, b, i = c(e.d(b))
                        c, b, i = e.b(c, b, i)
                        a, k = c(b, i)
                        i = a
                        j = i == nil and 148 or 0x1644 / j
                    end
                else
                    k = {[2] = 3, [3] = k}
                    j, k[1] = 0x3c, k
                    f, _, g = k[1][k[2]].IsA, k[1][k[2]], "AlignPosition"
                end
            elseif j <= 0x17 then
                i, j, b, c = d, 0xa10 / j, d.GetChildren, e._["ipairs"]
            else
                f, j, _ = e._["pcall"], j + 181, e:Sc{k}
            end
        until false
    end
end,
Jf = {}, ca = function (e, a)
    return function ()
        local d, c, _
        _ = 12
        repeat
            if _ < 0x93 then
                if _ < 37 then
                    c = a[2][1][a[2][2]]
                    d = not c
                    _ = d and 147 or 253
                elseif _ <= 37 then
                    d = e.c(d(c))
                    return e.d(d)
                else
                    d = false
                    return d
                end
            elseif _ <= 0xfc then
                if _ <= 0x93 then
                    d = false
                    return d
                else
                    d, _, c = e._["pcall"], 0x25, e:md{a[1]}
                end
            else
                c = a[1][1][a[1][2]]
                d = c["RequestDropHeldAreaEgg"]
                _ = d and _ + -1 or 0x54
            end
        until false
    end
end}
):Pf(...
)
