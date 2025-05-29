/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onMounted, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

class SalonDashboard extends Component {
    setup() {
        super.setup();
        this.orm = useService("orm");
        this.action = useService("action");
        this.state = useState({
            bookings: 0,
            orders: 0,
            recent: 0,
            clients: 0,
            chairs: []
        });

        onMounted(() => this.loadData());
    }

    async loadData() {
        const data = await this.orm.call(
            "salon.booking",
            "get_booking_count",
            [],
            {}
        );

        this.state.bookings = data.bookings;
        this.state.orders = data.orders;
        this.state.recent = data.recent;
        this.state.clients = data.clients;

        const chairs = await this.orm.call(
            "salon.chair",
            "search_read",
            [],
            { fields: ["id", "name"] }
        );

        this.state.chairs = chairs;
    }

    openView(model, domain) {
        this.action.doAction({
            type: "ir.actions.act_window",
            res_model: model,
            views: [[false, "tree"], [false, "form"]],
            domain: domain || [],
            context: {},
        });
    }
}

SalonDashboard.template = "sic_salon_management.SalonDashboard";
registry.category("actions").add("salon_dashboard", SalonDashboard);
